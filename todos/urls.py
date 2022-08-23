from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('Login/', views.Login, name="Login"),
    path('Signup/', views.Signup, name="Signup"),
    path('Logout/', views.Logout, name="Logout"),
    path('Todo/', views.Todo, name="Todo"),
    path('Createtodo/', views.Createtodo, name="Createtodo"),
    path('Clear/', views.Clear, name="Clear"),
    path('Search/', views.Search, name="Search"),
    path('Edit/<int:Todo_id>', views.Edit, name="Edit"),
    path('Updatetodo/<int:Todo_id>', views.Updatetodo, name="Updatetodo"),
    path('Uncompleted/', views.Uncompleted, name="Uncompleted"),
    path('Deletetodo/<int:Todo_id>', views.Deletetodo, name="Deletetodo"),
    path('Redotodo/<int:Todo_id>', views.Redotodo, name="Redotodo"),
    path('Completed/<int:Todo_id>', views.Completed, name="Completed"),
]
