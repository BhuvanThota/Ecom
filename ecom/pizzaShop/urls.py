from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('order/<int:id>', views.edit_order, name='edit_order'),
    
    path('orderpizzas/', views.orderpizzas, name='orderpizzas'),

    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),

]
