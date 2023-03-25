from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic import RedirectView, ListView


class IndexView(ListView):
    pass


class IndexRedirectView(RedirectView):
    pattern_name = 'index'
