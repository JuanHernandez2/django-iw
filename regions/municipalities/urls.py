from django.urls import path

from . import views

app_name = "municipalities"
urlpatterns = [
    path('', views.index, name='index'),
    path('municipality/<int:m_id>/', views.detail_municipalities, name='detail_municipalities'),
    path('region/<int:r_id>/', views.detail_regions, name='detail_regions'),
    path('add/municipality/', views.add_municipality, name='add_municipality'),
    path('municipality/edit/<int:m_id>', views.edit_municipality, name='edit_municipality'),
    path('municipality/delete/<int:m_id>', views.delete_municipality, name='delete_municipality'),
    path('region/edit/<int:r_id>', views.edit_region, name='edit_region'),
    path('region/delete/<int:r_id>', views.delete_region, name='delete_region'),
    path('add/region/', views.add_region, name='add_region')
]