"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
=======
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
>>>>>>> 1e18a8600c52a1323b6613e527b04a875c898382
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)
from django.contrib import admin
from django.urls import path

<<<<<<< HEAD

=======
>>>>>>> 1e18a8600c52a1323b6613e527b04a875c898382
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name = 'api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name = 'api-schema'),
        name = 'api-docs',
        )
]
