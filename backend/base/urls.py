from django.urls import path
from . import views


urlpatterns = [
    path('calendar/init/', views.google_calendar_init_view, name='user_credentials'),
    path('calendar/redirect/', views.google_calendar_redirect_view, name='handle_redirect')
]