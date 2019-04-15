Agili - Mapeamento do transporte público de São Paulo
===========================================

Descrição
---------
Este projeto visa coletar dados dos veículos de transporte público de São Paulo para a realização de um estudo de Big Data.

A análise da coleta dos dados deverá responder basicamente as seguintes perguntas:
 - Quais linhas e rotas estão com muita ou pouca demanda?
 - Quais são os horários que em que estas linhas/rotas podem ser otimizadas?
 - Existe alguma redundância de rota que poderia ser otimizada?
 - Como a implementação de rotas dinâmicas pode ajudar a melhorar o transporte público?

Requisitos
----------

 - [Python] ^3.6
 - [Python > Requests]
 - [Python > PyMongo]
 - [MongoDB] ^3.4 (opcional)
 - [SPTrans] Token API Olho Vivo
 
 Exemplo de dados coletados em tempo real que serão armazenados no banco NoSQL
----------
   ```
{
    "_id" : ObjectId("5cb409b50091fa6d974b83a9"),
    "linha" : "N101",
    "codigo_linha" : 35050,
    "circular" : false,
    "sentido" : 2,
    "letreiro_ida" : "TERM. LAPA",
    "letreiro_volta" : "TERM. PQ. D. PEDRO II",
    "id_veiculo" : "11349",
    "acessivel" : true,
    "latitude" : -23.5173575,
    "longitude" : -46.6815965,
    "data_hora" : ISODate("2019-04-15T04:33:45.000Z")
}
  ```

Notas
-----
- Este script está sendo executado a cada 1 minuto em uma instancia do Google Cloud Plataform (CentOS 7) com um agendador de tarefas
- Todos os dados dos veículos de 3 linhas diferentes estão sendo armazenados para estudos de Big Data
- O script foi escrito em Python de forma funcional para que seja o mais didático possível
- Caso deseje obter um token para visualizar o funcionamento do script acesse http://www.sptrans.com.br/desenvolvedores/api-do-olho-vivo-guia-de-referencia/
- Caso deseje configurar o script apenas para visualizar o output dos dados sem utilizar banco de dados configure a opção ```salvar_banco_dados = False``` no arquivo [config.py]
- Caso deseje acessar de forma visual alguma linha da SPTrans acesse http://olhovivo.sptrans.com.br

[config.py]:https://github.com/nkramirez/agili/blob/master/config.py
