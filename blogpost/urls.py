

from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('blog/add', views.create_blog, name='addblog'),
        path('blog/update/<int:id>', views.update_blog, name='update'),
        path('auth/', views.auth, name='auth'),
        path('login/', views.signin, name='signin'),
        path('logout/', views.signout, name='logout'),
        path('auth/signup', views.register, name='register'),
        path('blog/delete/<int:id>', views.delete_blog, name="delete"),
]
