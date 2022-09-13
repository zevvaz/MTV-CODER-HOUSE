from django.urls import path
from FamiliaApp_.views import familia


urlpatterns = [
    path('familia/', familia),
]