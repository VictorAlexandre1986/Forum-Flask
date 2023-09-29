# Endpoints

## Cadastrar Login
```
http://127.0.0.1:5000/api/v1/login/
```
```
{
	"id":1,
	"username":"Victor Alexandre",
	"password":"123465"
}
```

## Buscar Login por id
```
http://127.0.0.1:5000/api/v1/login/1
```

## Buscar todos os Logins
```
http://127.0.0.1:5000/api/v1/login/
```

## Deletar Login
```
http://127.0.0.1:5000/api/v1/login/1
```

## Atualizar Login
```
http://127.0.0.1:5000/api/v1/login/2
```
```
{
	"id":2,
	"username":"Victor Alexandre Braga",
	"password":"qwerty"
}
```

------------------------------------------------------

## Cadastrar usuario
```
http://127.0.0.1:5000/api/v1/usuario/
```
```
{
	"id":3,
	"nome_completo":"Victor Alexandre Braga",
	"dt_nasc": "1990-06-19",
	"email": "teste@email.com",
	"celular": "123456789",
	"id_login":1
}
```

## Buscar todos os usuarios
```
http://127.0.0.1:5000/api/v1/usuario/
```

## Buscar usuario por Id
```
http://127.0.0.1:5000/api/v1/usuario/2
```

## Deletar usuario
```
http://127.0.0.1:5000/api/v1/usuario/3
```

## Atualizar usuario
```
http://127.0.0.1:5000/api/v1/usuario/1
```
```
{
	"id":2,
	"nome_completo":"Xandão",
	"dt_nasc":"2023-09-11",
	"email":"xandinho@teste.com",
	"celular":"555555555",
	"id_login":1
}
```

----------------------------------------------

# Cadastrar pergunta
```
http://127.0.0.1:5000/api/v1/pergunta
```
```
{
	"id":4,
	"id_login":1,
	"titulo":"API FLASK",
	"pergunta":"Como criar uma",
	"contagem_voto":0	
}
```

# Buscar todas as perguntas
```
http://127.0.0.1:5000/api/v1/pergunta/
```

# Buscar pergunta por Id
```
http://127.0.0.1:5000/api/v1/pergunta/1
```

## Atualizar pergunta
```
http://127.0.0.1:5000/api/v1/pergunta/1
```
```
{
	"id":4,
	"id_login":1,
	"titulo":"API DJANGO",
	"pergunta":"Como criar uma",
	"contagem_voto":0	
}
```

## Deletar pergunta
```
http://127.0.0.1:5000/api/v1/pergunta/1
```

------------------------------------------------------

## Cadastrar resposta
```
http://127.0.0.1:5000/api/v1/resposta/
```
```
{
	  "id": 6,
    "id_login": 1,
    "resposta": "seila",
    "contagem_voto": 0,  
    "id_pergunta":1
}
```

## Buscar resposta por Id
```
http://127.0.0.1:5000/api/v1/resposta/1
```

## Buscar todas as respostas
```
http://127.0.0.1:5000/api/v1/resposta/
```

## Atualizar respostas
```
http://127.0.0.1:5000/api/v1/resposta/1
```
```
{
	  "id": 6,
    "id_login": 1,
    "resposta": "é isso",
    "contagem_voto": 0,  
    "id_pergunta":1
}
```

## Deletar resposta
```
http://127.0.0.1:5000/api/v1/resposta/1
```
