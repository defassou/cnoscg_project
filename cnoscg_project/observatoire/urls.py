from operator import index
from . import views
from django.urls import path
from .views import recherche_observateur, recherche_api, list_observateur, detail_observateur

urlpatterns = [
    path("", views.index, name="index"),
    path("recherche/", views.recherche_observateur, name="recherche"),
    path("recherche_api/", views.recherche_api, name="recherche_api"),

    path("list_observateur/", views.list_observateur, name="list_observateur"),
    path("detail_observateur/<str:pk>", detail_observateur, name="detail_observateur"),

    path('add_observateur/', views.update_observateur, name='update_observateur'),
    path('update_observateur/<str:pk>', views.update_observateur, name='update_observateur'),
    path('delete_observateur/<str:pk>', views.delete_observateur, name='delete_observateur'),

]