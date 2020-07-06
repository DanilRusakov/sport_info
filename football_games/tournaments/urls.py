from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.TournamentsView.as_view(), name='tournaments'),
    # re_path(r'^tournaments/(?P<id>[0-9]{1,3})/', views.tournament_single),
]
