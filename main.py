import requests
#import json
#import threading
#import time
import datetime
from pprint import pprint, pformat
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

def codigosLinha(linha):
    return session.get(sptrans_url + '/Linha/Buscar?termosBusca=' + linha).json()

def paradasLinha(linha):
    return session.get(sptrans_url + '/Parada/BuscarParadasPorLinha?codigoLinha=' + linha).json()

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
            salvarLogs(posicao)
            salvarLogs("----------------")
        if(config.salvar_banco_dados):
            salvarDados(posicao)

def salvarDados(dado):
    banco = MongoClient(config.url_mongodb)
    db = banco['agili']
    collection = db['posicoes']
    collection.insert_one(dado)

def salvarLogs(dado):
    pprint(dado)
    with open(config.log_file, 'a') as file:
        file.write(pformat(str(dado)) + '\n')


# Init #
autenticar()

if type(config.linhas) != list:
    salvarLogs("A variável linhas deve ser uma lista")
    quit()
if len(config.linhas) < 1:
    salvarLogs("Não há linhas para serem monitoradas")
    quit()

for linha in config.linhas:
    codigos_linha = codigosLinha(linha)
    if(len(codigos_linha) > 0):
        for codigo in codigos_linha:
            posicoes_veiculos = posicoesVeiculos(codigo['cl'])
            prepararDados(codigo, posicoes_veiculos)
    else:
        salvarLogs("A linha {} não foi encontrada no sistema".format(linha))