from django.contrib import admin
from django.urls import path
#precisa importar o arquivo views do app_cad_usuarios para chmarsua função
from app_cad_usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rota, View responsável, Nome de referencia
    #facebook.com
    #path(''),
    #facebook.com/eu
    #path('eu/'),
                 # home é o nome da função de defini em views de app_cad_usuarios
    path('', views.home, name="home"),
    path('usuarios/', views.usuarios, name="listagem_usuarios"),

]
