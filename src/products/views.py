from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product



class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name="product/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context



def Product_Detail_View(request, pk= None , *args , **kwargs):
    instance= get_object_or_404(Product, pk = pk)
    #queryset= Product.objects.all()
    context={
        'object': instance
        }
    return render(request, "product/detail.html",context)


