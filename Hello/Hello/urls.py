from django.contrib import admin
from django.urls import path

from home import views
admin.site.site_header = "Django Sample"
admin.site.site_title = "Django Website"
admin.site.index_title = "Welcome to our sample website"


urlpatterns = [
    path("", views.index, name='home'),
    path('admin/', admin.site.urls),
    path('contact/', views.contact),
    path('service/', views.service),
    path('about/', views.about)
]
