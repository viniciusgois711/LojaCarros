from django.urls import path

from . import views

app_name='app'
urlpatterns = [
    path('', views.login, name='login'),

    # path('estoque/', views.estoque, name='estoque'),
    path('manager/', views.gerenciamento, name='gerenciamento'),
    path('manager/add_veiculo', views.add_veiculo, name='add_veiculo'),

]