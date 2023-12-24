from django.shortcuts import render
# importando a classe do banco usuarios depois de feito o magrations e o migrate
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #1. Salvar os dados da tela no banco de dados
    #Instanciando a classe Usuario
    novos_usuarios = Usuario()
    #Recebendo os dados do formulário
    novos_usuarios.nome = request.POST.get('nomeform')
    novos_usuarios.idade = request.POST.get('idadeform')
    #Salvando os dados
    novos_usuarios.save()