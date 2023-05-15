from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.GroupListView.as_view(), name='group_list'),
    path('create/', views.GroupCreateView.as_view(), name='group_create'),
    path('<int:pk>/', views.GroupUpdateView.as_view(), name='group_update'),
    path('<int:pk>/delete/', views.GroupDeleteView.as_view(), name='group_delete'),
]
