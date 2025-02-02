from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('psychological', views.psychological_page, name='psychological'),
    path('about', views.about_page, name='about'),
    path('info', views.info_page, name='info'),
    path("info/<int:pk>/", views.main_title_detail_view, name="info_detail"),
    path('processing', views.processing_image_page, name='processing'),
    path('process-image/', views.process_uploaded_image,
         name='process_uploaded_image'),
    path('all_processing', views.all_processing_page, name='all_processing'),
]
