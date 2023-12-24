# django_cadastro_de_usuarios
Sistema web de cadastro de usuários, com Framework Django e integração com Banco de dados

inspirado em https://www.youtube.com/watch?v=-m5ywU8SW9E&list=WL&index=4

1 criar a rota, `O link` (urls.py)
2 criar o mque fazer quando chegar naquele link (views.py)
3 criar o exibir quando chegar no link (html e css)

1 no arquivo urls.py  em sys_cadastro vamos criar a rota para a pagina inicaal
![Alt text](v.png)

obs cadastrar o app_cad_usuarios no arquivo settings.py

2 no arquivo views.py  em app_cad_usuarios vamos criar a função home
![Alt text](vv.png)

3 criando os templates html e a pasta dos templates
![Alt text](vvv.png)

visulizar projeto
python manage.py runserver

nas páginas do bootstrap vamos buscar uma navbar para compor nossa home buscar um formulario de imput etc

agora a etapade criação da views de cadastro ligando o banco de dados com as informações do formulario
![Alt text](vvvv.png)
![Alt text](vvvvv.png)

agora vamos fazer o migrations e o migrate
python manage.py makemigrations
python manage.py migrate

agora vamos criar a view que recebe os dados do formulario
![Alt text](vvvvvv.png)

criando o template usuarios.html
![Alt text](vvvvvvv.png)

antes, passar {% csrf_token %} dentro do form no home.html
python manage.py makemigrations
python manage.py migrate 

teste web
python manage.py runserver

fizemos a estilização da pagina de usuarios

e faremos um template base pra não precisar reescrever todas as informaçoes e componetes do bootstrap ./tmplates/usuarios/base.html
