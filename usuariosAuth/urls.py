from django.urls import path, include
from . import views
from info.views import superuser

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('AlterarSenha', views.AlterarSenha, name='AlterarSenha'),
    path('controle', superuser, name='controle'),
    path('cadastrarprodutos', views.cadastrarprodutos, name='cadastrarprodutos'),
    path('pgcadastrar', views.pgcadastrar, name='pgcadastrar'),
    path('detalhar_pedido/<int:carrinho_id>/', views.detalhar_pedido, name='detalhar_pedido'),
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('excluir_produto/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),
    path('confirmar_compra/<int:carrinho_id>/', views.confirmar_compra, name='confirmar_compra'),
]