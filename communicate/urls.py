from django.urls import path

from .views import messageView, messageListView, messageCreateView

app_name = 'communicate'

urlpatterns = [
    path('', messageView.MessageView.as_view(), name='message'),
    path('list/', messageListView.MessageListView.as_view(), name='list'),
    path('create/', messageCreateView.MessageCreateView.as_view(), name='create'),
]