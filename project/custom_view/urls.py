from django.urls import include, path
from . import views
app_name='custom_view'



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),


    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),


    path('blog_archive/', views.blog_archive, name='blog_archive'),




    path('Project/<int:project_id>/', views.project_single, name='project_single'),


    path('catagory/<int:category_id>/', views.catagory_detail, name='catagory_detail'),
    path('brand/<int:brand_id>/', views.brand_detail, name='brand_detail'),


    path('service/<int:service_id>/', views.Service_detail, name='Service_detail'),


    path('product/<int:Product_id>/', views.Product_detail, name='Product_detail'),

    path('about_us/', views.about_us, name='about_us'),



    path('career_page/', views.career_page, name='career_page'),

    path('job_detail/<int:job_id>/', views.job_detail, name='job_detail'),

]

