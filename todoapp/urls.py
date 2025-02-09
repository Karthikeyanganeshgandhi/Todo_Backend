from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('feature/',views.feature,name='feature'),
    path('contact/',views.contact,name='contact'),
    path('account/',views.account,name='account'),
    path('register/',views.register,name='register'),
    path('contacts/',views.contacts,name='contacts'),
    path('custom_logout/',views.custom_logout,name='custom_logout'),

]