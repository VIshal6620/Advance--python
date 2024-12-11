from django.urls import path

from.import views


urlpatterns = [
    path('',views.welcome),
    path('welcome/', views.welcome),
    path('signUp/', views.user_signup),
    path('login/', views.user_signin),
    path('save/',views.user_save),
    path('list/',views.user_list),
   # path('testList/',views.test_list),
    path('ORS/edit/<int:id>/',views.edit_user),
    path('ORS/delete/<int:id>/',views.delete_user),
    path('ORS/logout/',views.logout),

]