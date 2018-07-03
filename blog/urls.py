from django.urls import path
from . import views  

urlpatterns = [
    path('', views.allBlog, name='allBlog'),
    path('<int:blog_id>/',views.detail, name='detail')
] 
