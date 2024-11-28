from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome),
    path('home/', views.ors_home),
    path('welcome/', views.welcome),
    path('signup/', views.user_signup),
    path('signin/', views.user_signin),
    path('save/',views.user_save),
    path('test/', views.test_list),
    path('list/', views.user_list),
    path('delete/<int:id>/', views.delete_user),
    path('edit/<int:id>/', views.edit_user),
    path('logout/', views.logout),

    path('create/', views.create_session),
    path('access/', views.access_session),
    path('destroy/', views.destroy_session),
    path('set/', views.setCookies),
    path('get/', views.getCookies),

]
