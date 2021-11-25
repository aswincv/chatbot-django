from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import login, logout
from chat.views import index, user_button_calls

urlpatterns = [
    path('', index),
    path('accounts/button-calls/', user_button_calls),
    path('accounts/login/', login),
    path('accounts/logout/', logout),
    path('admin/', admin.site.urls),
]
