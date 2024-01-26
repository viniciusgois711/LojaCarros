from django.urls import path

from . import views

app_name='app'
urlpatterns = [
    path('', views.login, name='login'),

    # path('estoque/', views.estoque, name='estoque'),
    path('gerenciamento/', views.gerenciamento, name='gerenciamento')

]