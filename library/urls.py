
from catalog import views
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('',views.beg127),
    path('accounts/',include('django.contrib.auth.urls')),

]
