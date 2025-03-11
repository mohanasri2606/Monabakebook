from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),  # Home page
    path('search/', views.search, name='search'),
    path("post/<str:slug>/", views.detail, name="detail"),
    path("about/", views.about, name="about"),  
    path("contact/", views.contact, name="contact"), 
    path("success/", views.success, name="success")
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
