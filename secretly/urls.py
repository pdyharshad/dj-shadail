

from django.urls import path

from . import views

app_name = "secretly"

urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('get_message/<str:message_type>/<int:latest_id>/', views.get_message,
            name='get_message'),
        path('get_messagetype/', views.get_message_type,
            name='get_message_type'),

#        path('post_user/', views.post_user,
 #           name='post_user'),
        ]
