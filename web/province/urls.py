from django.conf.urls import  url
from province import views

urlpatterns = [
    url(r'^lihat$', views.ListProvinceView.as_view(), name='province'),
    url(r'^tambah/$', views.TambahProvince.as_view(), name='tambah'),
    url(r'^simpan/$', views.SimpanProvince.as_view(), name='simpan'),
    url(r'^edit/(?P<id>\d+)$', views.EditProvince.as_view(), name='edit'),
    url(r'^hapus/(?P<id>\d+)$', views.HapusProvince.as_view(), name='hapus'),
    url(r'^update/$', views.UpdateProvince.as_view(), name='update'),
    
]