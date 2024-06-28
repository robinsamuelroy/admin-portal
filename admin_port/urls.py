from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='admin_login'),  # Login page
    path('admin_portal/', views.admin_portal, name='admin_portal'),  # Admin portal after login
     path('logout/', views.user_logout, name='admin_logout'),  # Logout page


    # Admin Portal URLs for Customer and Invoice
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/new/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/new/', views.invoice_create, name='invoice_create'),
    path('invoices/<int:pk>/edit/', views.invoice_edit, name='invoice_edit'),
    path('invoices/<int:pk>/delete/', views.invoice_delete, name='invoice_delete'),
]
