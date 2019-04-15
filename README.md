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
 - [MongoDB] ^3.4
 - [SPTrans] Token API Olho Vivo
 
 Exemplo de dados coletados em tempo real que serão armazanedos no banco NoSQL
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
