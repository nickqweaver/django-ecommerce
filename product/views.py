from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Product
from django.http import Http404

# Create your views here.


class IndexView(ListView):
    template_name = "product/index.html"
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    try:
        product = Product.objects.get(context.id)
    except Product.DoesNotExist:
        raise Http404

    context['product'] = product
    return context
