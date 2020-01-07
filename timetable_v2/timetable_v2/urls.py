from django.urls import path
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    path('', include('quickstart.urls')),
    path('admin/', admin.site.urls),

]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]