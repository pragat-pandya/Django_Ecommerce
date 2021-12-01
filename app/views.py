from django.http import request
from django.shortcuts import render

# Create your views here.

# Landing page of the website.
def index (request):
    # Further cookie based behaviour to be coded here.
    return render(request, "app/index.html")

# Fanbook View
def fanbook (request):
    return render (request, "app/fanbook.html")

# My Account View
def user_account (request):
    return render(request, "app/myaccount.html")

# My Profile VIEW
def user_profile (request):
    return render (request, "app/myprofile.html")

# Login and Signup VIEW
def user_login (request):
    return render (request, "app/login.html")

# SIGNUP View
def user_signup (request):
    return render (request, "app/signup.html")

# MyOrders view
def user_orders (request):
    return render (request, "app/myorders.html")

# MyPayments view
def user_payments (request):
    return render (request, "app/mypayments.html")

# MyAddresses views
def user_addresses (request):
    return render (request, "app/myaddresses.html")

# MyWishlist view
def user_wishlist (request):
    return render (request, "app/wishlist.html")

# Category views
# After models are setup might take arguments.
def product_category (request):
    return render (request, "app/category_listing.html")


# Product PAGE
def product (request):
    return render (request, "app/product_details.html")
