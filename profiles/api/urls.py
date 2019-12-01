from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles.api.views import (
    AvatarUpdateView, ProfileViewset, ProfileStatusViewset)

# profile_list = ProfileViewset.as_view({'get': 'list'})
# profile_detail = ProfileViewset.as_view({'get': 'retrieve'})

router = DefaultRouter()
router.register(r"profiles", ProfileViewset)
router.register(r'status', ProfileStatusViewset, basename='status')

urlpatterns = [
    path('', include(router.urls)),
    path('avatar/', AvatarUpdateView.as_view(), name="avatar-uodate"),
    # path('profiles/', profile_list, name='profile-list'),
    # path('profiles/<int:pk>/', profile_detail, name='profile-detail'),
]
