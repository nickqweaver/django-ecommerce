from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import BaseProduct
from django.http import Http404

# Create your views here.


class IndexView(ListView):
    template_name = "product/index.html"
    context_object_name = 'product_list'

    def get_queryset(self):
        return BaseProduct.objects.all()


class ProductDetailView(DetailView):
    model = BaseProduct
    template_name = "product/product_detail.html"


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    try:
        product = BaseProduct.objects.get(context.id)
    except BaseProduct.DoesNotExist:
        raise Http404

    # Allows template to access the object via product key
    context['product'] = product
    return context
