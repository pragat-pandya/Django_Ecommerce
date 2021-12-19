from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path ("", views.index, name="index"),
    path("fanbook", views.fanbook, name="fanbook"),
    path("myaccount", views.user_account, name="myaccount"),
    path("myprofile", views.user_profile, name="myprofile"),
    path("login", views.user_login, name="login"),
    path("signup", views.user_signup, name="signup"),
    path("myorders", views.user_orders, name="myorders"),
    path("mypayments", views.user_payments, name="mypayments"),
    path("myaddresses", views.user_addresses, name="myaddresses"),
    path("wishlist", views.user_wishlist, name="wishlist"),
    path("categories", views.product_category, name="categories"),
    path("product", views.product, name="product"),
    path("men", views.products_for_men, name="men")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
