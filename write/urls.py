from django.urls import path, include
from . import views


urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:write_id>', views.detail, name='detail'),
    path('<int:write_id>/upvote', views.upvote, name='upvote'),
]
