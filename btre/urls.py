"""btre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from pages import urls as pages_urls
from listings import urls as listings_urls
from accounts import urls as accounts_urls
from user_contacts import urls as contacts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(pages_urls)),
    path('listings/', include(listings_urls)),
    path('accounts/', include(accounts_urls)),
    path('contact/', include(contacts_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
