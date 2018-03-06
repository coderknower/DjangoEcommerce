from django.conf.urls import url


from .views import ProductListViewClass, ProductDetailSlugView


urlpatterns = [

    #url(r'^featured/$', ProductFeaturedListView.as_view()),
    #url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    url(r'^products/$', ProductListViewClass.as_view()),
    #url(r'^productsfbv/$', product_list_view_function),
    #url(r'^products/(?P<pk>\d+)/$', ProductDetailViewClass.as_view()),
    #url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view_function),



]
