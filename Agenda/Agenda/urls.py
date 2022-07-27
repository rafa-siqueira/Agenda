from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('agenda/', views.lista_eventos, name='agenda'),
    path('agenda/teste', views.teste, name='teste'),
    path('agenda/cadastro', views.cadastro, name='cadastro'),
    path('agenda/submit', views.submit_cadastro, name='agenda_submit'),
    path('agenda/lista', views.json_lista_evento, name='lista'),
    path('agenda/evento/', views.evento, name='evento'),
    path('agenda/evento/submit', views.submit_evento, name='evento_submit'),
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento),
    path('agenda/evento/visualizar/<int:id_evento>', views.visualizar, name='visualizar'),
    path('', RedirectView.as_view(url='/agenda/'), name='home'),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
]
