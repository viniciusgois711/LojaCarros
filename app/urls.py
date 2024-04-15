from django.urls import path

from . import views

app_name='app'
urlpatterns = [
    path('', views.login, name='login'),

    # path('estoque/', views.estoque, name='estoque'),
    path('manager/', views.gerenciamento, name='gerenciamento'),
    path('manager/add_veiculo', views.add_veiculo, name='add_veiculo'),
    path('manager/remove_veiculo/<int:id>', views.remove_veiculo, name='remove_veiculo'),
    path('manager/edit_veiculo/<int:id>', views.edit_veiculo, name="edit_veiculo"),
    path('manager/detalhes_veiculo/<int:id>', views.detalhes_veiculo, name="detalhes_veiculo")

]