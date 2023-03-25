from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy

from webapp.forms import ProductForm
from webapp.models import Product
from webapp.models.products import CategoryChoice


class ProductDetail(DetailView):
    template_name = 'product.html'
    model = Product
    extra_context = {'choices': CategoryChoice.choices}

class GroupPermissionCreateMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'moderator']).exists()

class ProductCreateView(GroupPermissionCreateMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'product_create.html'
    model = Product
    form_class = ProductForm
    success_message = 'Продукт создан'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

class GroupPermissionEditMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'moderator']).exists()


class ProductUpdateView(GroupPermissionEditMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'product_update.html'
    form_class = ProductForm
    model = Product
    success_message = 'Продукт обновлён'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

class GroupPermissionDeleteMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['Admin', 'Manager', 'TeamLead']).exists()

class ProductDeleteView(GroupPermissionDeleteMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    success_message = 'Продукт удалён'
