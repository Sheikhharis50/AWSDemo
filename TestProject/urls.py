
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<name>', hello),
    # path('savetodb/<name>', saveToDb),
    path('', index)
]
