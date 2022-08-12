from django.urls import path
from .views import partidaView


urlpatterns = [
    path('partidas',partidaView.as_view())
]
 