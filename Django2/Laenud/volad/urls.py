from django.urls import path
from . import views
from .views import SignUpView
from django.contrib.auth.views import LogoutView
from .views import delete_debt

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path("login/", views.login_view, name="login"),
    path('debt/list/', views.debt_list, name='debt_list'),
    path('debt/new/', views.create_debt, name='create_debt'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('delete/<int:debt_id>/', delete_debt, name='delete_debt'),
    path('logout/', LogoutView.as_view(), name='logout'),
]