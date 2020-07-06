from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the index.")


class TournamentsView(TemplateView):
    template_name = 'tournaments/tournaments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tournaments'] = Tournament.objects.all()
        return context
