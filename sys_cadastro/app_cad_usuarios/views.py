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
    # exibor os usuarios já cadastrados na tela
    usuarios = {
        #aqui ele espera que seja um dicionario
        'usuarios': Usuario.objects.all()
    }
    #retornar os dados para a tela
    return render(request, 'usuarios/usuarios.html', usuarios)