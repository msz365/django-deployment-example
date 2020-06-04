from django.conf.urls import url
from first_app import views
#Template Tagging
app_name = 'first_app'
urlpatterns =[

    url('other/', views.other, name='other'),
    url('relative/', views.relative, name='relative'),
    url('register/', views.register, name='register'),
    url('user_login/', views.user_login,name='user_login' )

]
