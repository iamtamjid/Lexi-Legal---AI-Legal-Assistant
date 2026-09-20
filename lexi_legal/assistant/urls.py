from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('clients/add/', views.add_client_view, name='add_client'),
    path('clients/', views.existing_clients_view, name='existing_clients'),
    path('files/', views.all_files_view, name='all_files'),
    path('clients/<int:client_id>/', views.client_detail_view, name='client_detail'),
    path('clients/<int:client_id>/delete/', views.delete_client_view, name='delete_client'),
    path('logout/', views.logout_view, name='logout'),
    path('api/process_file/', views.process_file_api, name='process_file_api'),
]
