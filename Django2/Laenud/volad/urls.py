from django.urls import path
from . import views
from .views import SignUpView


urlpatterns = [
    path('', views.login_view, name='login_view'),
    path("login/", views.login_view, name="login"),
    path('debt/list/', views.debt_list, name='debt_list'),
    path('debt/new/', views.create_debt, name='create_debt'),
    path('debt/<int:pk>/update_debt/', views.update_debt, name='update_debt'),
    path('debt/<int:pk>/delete_debt/', views.delete_debt, name='delete_debt'),
    path('signup/', SignUpView.as_view(), name='signup'),
]