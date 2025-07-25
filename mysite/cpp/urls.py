from django.urls import path
from . import views

app_name = 'cpp'
urlpatterns = [
    path(
        'resposta/<int:id_resposta>/avalia/', 
        views.AvaliaRespostaView.as_view(), name='avalia'
    ),
    path(
        'turma/<int:id_turma>/nova-avaliacao/',
        views.NovaAvaliacaoView.as_view(), name='nova-avaliacao'
    ),
]