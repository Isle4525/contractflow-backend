from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, token_obtain_pair, token_refresh

from .views import RegisterCompanyView, MeView, RegisterContractorView

urlpatterns = [
    path('auth/register/', RegisterCompanyView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me/', MeView.as_view(), name='me'),
    path('auth/register-contractor/', RegisterContractorView.as_view(), name='register-contractor'),
]