from django.urls import path
from .views import SignUpView, ProfileView, ProfileEditView

urlpatterns = [
        path("signup/", SignUpView.as_view(), name="signup"),
        path("edit-profile/", ProfileEditView.as_view(), name="profile_edit"),
        path("<str:username>/", ProfileView.as_view(), name="profile"), # user profile 
        ]
