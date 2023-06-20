from django.urls import path
from . import views

urlpatterns = [

    # ==================== LOGIN/LOGOUT ==================== #
    path('login/', views.pagina_login, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.inicializar_homepage, name='homepage'),
    path('cliente/', views.carregar_cliente, name='cliente'),
    path('cliente/save/', views.salvar_cliente, name='save_cliente'),
    path('cliente/edit/', views.editar_cliente, name='edit_cliente'),
    path('cliente/delete/', views.deletar_cliente, name='delete_cliente'),
    path('cliente/query/', views.pesquisar_cliente, name='query_cliente'),

    # ==================== COLABORADOR ==================== #
    path('colaborador/', views.carregar_colaborador, name='colaborador'),
    path('colaborador/save/', views.salvar_colaborador, name='save_colaborador'),
    path('colaborador/edit/', views.editar_colaborador, name='edit_colaborador'),
    path('colaborador/delete/', views.deletar_colaborador, name='delete_colaborador'),
    path('colaborador/query/', views.pesquisar_colaborador, name='query_colaborador'),

    # ==================== PROCESSO ==================== #
    path('processo/', views.carregar_processo, name='processo'),
    path('processo/save/', views.salvar_processo, name='save_processo'),
    path('processo/edit/', views.editar_processo, name='edit_processo'),
    path('processo/delete/', views.deletar_processo, name='delete_processo'),
    path('processo/query/', views.pesquisar_processo, name='query'),

    # ==================== RELATORIOS ==================== #
    path('relatorios/', views.carregar_relatorios, name='relatorios'),
    path('relatorios/processos/', views.carregar_relatorio_processo, name='relatorio_processos'),
    path('relatorios/clientes/', views.carregar_relatorio_cliente, name='relatorio_clientes'),
    path('relatorios/colaboradores/', views.carregar_relatorio_colaborador, name='relatorio_colaboradores'),
]