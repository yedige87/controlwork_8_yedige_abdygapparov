from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic import RedirectView, ListView

from webapp.forms import SearchForm
from webapp.models import Product
from webapp.models.products import CategoryChoice


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    ordering = ('name',)
    paginate_by = 5
    paginate_orphans = 1
    extra_context = {'choices': CategoryChoice.choices}
    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset().all()     #exclude(is_deleted=True)
        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(text__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context


class IndexRedirectView(RedirectView):
    pattern_name = 'index'
