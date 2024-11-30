from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    
    path('api/v1/', include('authentication.urls')),
    
    path('', views.home, name='home'),
    
    path('admin/', admin.site.urls),
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('suppliers.urls')),
    path('', include('inflows.urls')),
    path('', include('products.urls')),
    path('', include('outflows.urls')),
]
