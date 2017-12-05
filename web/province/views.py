from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.contrib import messages
from orm.models import Province
from django.http import HttpResponse
from province.forms import ProvinceForm

class ListProvinceView(View):

    def get(self, request):
        template = 'province/index.html'
        provinces = Province.objects.all()

        data = {
               'list_Provinces': provinces,
        }
        return render(request, template, data)  


class TambahProvince(View):
    
    def get(self, request):
      template = 'province/add.html'

      form = ProvinceForm(request.POST or None)
      data = {
        'form': form,
       }
      return render(request, template, data)

class SimpanProvince(View):
    
    def post(self, request):
        template = 'province/add.html'

        form = ProvinceForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            province = Province()
            province.user = request.user
            province.name = form.cleaned_data['nama']
            province.save()
            messages.add_message(request, messages.SUCCESS, "Data Berhasil Disimpan")
            return redirect('province:province')
        else:           
            data = {
                'form': form,
            }
            messages.add_message(request, messages.WARNING, "Data Gagal Disimpan")
            return render(request, template, data)

class HapusProvince(View):
    def get(self, request, id):
        rgx = Province.objects.filter(pk=id)
        if rgx.exists():
            rgx = rgx.first()
            rgx.delete()
            messages.add_message(request, messages.SUCCESS, "Data Berhasil DiHapus")
        return redirect('province:province')

class EditProvince(View):
    template = 'province/edit.html'
    def get(self, request, id):
        
        province = Province.objects.get(pk=id)
        initial = {
            'id': province.pk,
            'nama': province.name,
        }

        form = ProvinceForm(initial=initial)
        data = {
            'form': form
        }
        return render(request, self.template, data)

class UpdateProvince(View):
    
    def post(self, request):
        form = ProvinceForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            province = Province.objects.get(pk=id)
            province.name = form.cleaned_data['nama']
            province.save(force_update=True)
            messages.add_message(request, messages.SUCCESS, "Data Berhasil Diubah")
            return redirect('province:province')
        else:
            messages.add_message(request, messages.WARNING, "Data Gagal Diubah")
            return redirect('province:province')

