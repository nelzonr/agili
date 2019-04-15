import requests
import json
import threading
import time
import datetime
from pprint import pprint
from pymongo import MongoClient

import config
sptrans_url = 'http://api.olhovivo.sptrans.com.br/v2.1'
session = requests.Session()

# Funções #
def autenticar():
    r = session.post(sptrans_url + '/Login/Autenticar?token=' + config.sptrans_token)
    if r.status_code != 200:
        quit("Serviço indisponível")
    if r.json() != True:
        quit("Token inválido")

def codigoLinha(linha):
    return session.get(sptrans_url + '/Linha/Buscar?termosBusca=' + linha).json()

def posicoesVeiculos(codigo_linha):
    return session.get(sptrans_url + '/Posicao/Linha?codigoLinha=' + str(codigo_linha)).json()

def prepararDados(linha, posicoes):
    if len(posicoes['vs']) < 1:
        return
    for veiculo in posicoes['vs']:
        data_hora = datetime.datetime.strptime(veiculo['ta'], "%Y-%m-%dT%H:%M:%SZ")
        posicao = {
            'linha': linha['lt'],
            'codigo_linha': linha['cl'],
            'circular': linha['lc'],
            'sentido': linha['sl'],
            'letreiro_ida': linha['tp'] if linha['sl'] == 1 else linha['ts'],
            'letreiro_volta': linha['ts'] if linha['sl'] == 1 else linha['tp'],
            'id_veiculo': veiculo['p'],
            'acessivel': veiculo['a'],
            'latitude': veiculo['py'],
            'longitude': veiculo['px'],
            'data_hora': data_hora
        }
        if(config.exibir_resultados):
            pprint(posicao)
            print("----------------")
        if(config.salvar_banco_dados):
            salvarDados(posicao)

def salvarDados(dado):
    banco = MongoClient(config.url_mongodb)
    db = banco['agili']
    collection = db['posicoes']
    collection.insert_one(dado)

# Init #
autenticar()

if type(config.linhas) != list:
    quit("A variável linhas deve ser uma lista")
if len(config.linhas) < 1:
    quit("Não há linhas para serem monitoradas")

for linha in config.linhas:
    codigo_linha = codigoLinha(linha)
    if(len(codigo_linha) > 0):
        for codigo in codigo_linha:
            posicoes_veiculos = posicoesVeiculos(codigo['cl'])
            prepararDados(codigo, posicoes_veiculos)
    else:
        print("A linha {} não foi encontrada no sistema".format(linha))
