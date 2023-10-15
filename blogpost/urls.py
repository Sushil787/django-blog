

from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('blog/', views.show_blogs),
        path('blog/', views.create_blog),
        path('auth/', views.auth, name='auth'),
        path('login/', views.signin, name='signin'),
        path('logout/', views.signout, name='logout'),

        path('auth/signup', views.register, name='register'),
        path('blog/<int:id>', views.delete_blog),
        path('blog/<int:id>', views.update_blog)
]
