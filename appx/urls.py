
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from appx.views import NoteViewSet, UserViewSet, api_root

note_list = NoteViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

note_detail = NoteViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

user_list = UserViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

user_detail = UserViewSet.as_view(
    {
        'get': 'retrieve',
    }
)

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('notes/', note_list, name='note-list'),
    path('notes/<int:pk>/', note_detail, name='note-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
])
