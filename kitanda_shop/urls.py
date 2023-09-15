from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "kitanda_shop"  # Substitua 'kitanda' pelo nome do seu app

urlpatterns = [
    path("", views.LandingPageView.as_view(), name="landing_page"),
    path("loja/<str:name>/", views.LojaView.as_view(), name="loja"),
    path("loja/comprar/<str:name>/", views.ComprarView.as_view(), name="comprar"),
    path("checkout/<uuid:id>/", views.CheckoutView.as_view(), name="checkout"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("login/", views.loginView.as_view(), name="login"),
    path("register/", views.registerView.as_view(), name="register"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
