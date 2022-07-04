from django.urls import path,include
from .views import Home
app_name = 'core'

urlspatterns = [
    path('/', Home.as_view()),
    path('', include('core.urls', namespace='core')),
]