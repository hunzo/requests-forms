from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('vps/', views.VPSHome, name="vps-form"),
    path('vpn/', views.VPNHome, name="vpn-form"),
    path('colo/', views.COLOHome, name="colo-form"),
    path('account/', views.ACCOUNTHome, name="account-form"),
    path('guest/', views.GUESTHome, name="guest-form"),
    path('domain/', views.DOMAINHome, name="domain-form"),
]
