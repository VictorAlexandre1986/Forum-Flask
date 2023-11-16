# Forum de perguntas e respostas
Forum feito em Python utilizando o framework Flask, foi utilizado clean architecture para desenvolver esse projeto.Para rodar esse projeto é necessário seguir as seguintes etapas. 

É necessário criar um ambiente virtual com:
``` 
python -m venv venv
```
Depois acessar o ambiente virtual:
```
.\venv\Scripts\activate
```
Instalar as dependencias:
```
pip install -r requirements.txt
```

## Tecnologias utilizadas

<ul>
  <li>Python</li>
  <li>Flask</li>
  <li>SQLAlchemy</li>
  <li>Pydantic</li>
  <li>Alembic</li>
  <li>Sqlite</li>
</ul>

## Para rodar o alembic caso seja necessário novas migrações:

```
alembic init nome_do_seu_projeto
```

```
alembic revision --autogenerate -m "titulo da migração"
```

```
 alembic upgrade head
```


