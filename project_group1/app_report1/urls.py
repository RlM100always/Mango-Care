from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about, name='about'),

    path('diseases/', views.disease_list_view, name='disease_list'),  # ✅ Fixed
    path('diseases/add/', views.disease_create_view, name='disease_form'),
    path('diseases/<int:id>/', views.disease_detail_view, name='disease_details'),
    path('diseases/<int:id>/edit/', views.disease_update_view, name='disease_edit'),
    path('diseases/<int:id>/delete/', views.disease_delete_view, name='disease_delete'),
]
