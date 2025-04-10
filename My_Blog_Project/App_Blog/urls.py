from django.urls import path, re_path
from . import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    re_path(r'^details/(?P<slug>.+)/$', views.blog_details, name='blog_details'),
    path('like/<pk>/', views.like, name='like_post'),
    path('unlike/<pk>/', views.unlike, name='unlike_post'),
    path('my-blogs/', views.MyBlogs.as_view(), name='my_blogs'),
    path('update/<pk>', views.UpdateBlog.as_view(), name='update_blog'),
    

]