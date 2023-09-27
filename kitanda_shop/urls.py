from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

app_name = "kitanda_shop"  # Substitua 'kitanda' pelo nome do seu app

urlpatterns = [
    path("", views.home, name="landing_page"),
    path("loja/<str:name>/", views.store, name="store"),
    path("product/<str:id>/", views.product, name="product"),
    path("cart/<str:name>/", views.cart, name="cart"),
    path("adress/<str:name>/", views.adress, name="adress"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
