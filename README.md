Cats API
=============
Documentação do projeto
-----------------------
![Imagem da arquitetura](imgs/diagrama.png)


Documentação da API
-------------------
![Imagem da documentação da API](imgs/apis.png)

_importar as collections do postman para testar as APIs_


Instalação
----------
- Instale o docker e o docker-compose
- Clone o projeto, entre na pasta raiz (onde o arquivo docker-compose.yml se encontra) e rode o seguinte comando:
```
docker compose up -d
```
- Caso ocorra o seguinte erro:
```
 => ERROR [prometheus 1/1] FROM docker.io/prom/prometheus:v2.2
 > [prometheus 1/1] FROM docker.io/prom/prometheus:v2.2.1
failed to solve: rpc error: code = Unknown desc = failed to load cache key: invalid empty config file resolved for docker.io/prom/prometheus:v2.2
```

- Rode o seguinte comando e tente novamente
```
docker pull prom/prometheus:v2.2.1
```

Dashboard
---------
![Imagem das Dashboards](imgs/grafana.png)
_clique na imagem para aumentar_