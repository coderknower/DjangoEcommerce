from django.conf.urls import url


from .views import ProductListViewClass, ProductDetailSlugView


urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    url(r'^$', ProductListViewClass.as_view(), name='list'),

]
