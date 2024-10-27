# auto_evaluation/urls.py
from django.contrib import admin
from django.urls import path, include
from submissions import views as submissions_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submissions/', include('submissions.urls')),  # Include the submissions app URLs
    path('', submissions_views.home, name='home'),  # Set the root URL to the home view
]
