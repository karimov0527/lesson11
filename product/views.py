from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Waters
from .forms import Water_Form

# Create your views here.

class Waters_list(LoginRequiredMixin,View):
    login_url = 'account:login'
    def get(self, request):
        t = request.GET.get('q')
        user = request.user
        if t:
            page_obj = Waters.objects.filter(Q(name__icontains=t) | Q(price__icontains=t))
        else:
            products = Waters.objects.all()
            paginator = Paginator(products, 3)  
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)
        return render(request, 'list.html', {'page_obj': page_obj, 'user': user})


def home_page(request):
    return render(request, 'home.html')

class Waater_add(LoginRequiredMixin,View):
    login_url = 'account:login'
    def get(self,request):
        form = Water_Form()
        return render(request,"add_product.html",{'form':form})
    def post(self,request):
        form = Water_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request,"add_product.html",{'form':form})
    

class Product_detail(View):
    def get(self,request,pk):
        product = Waters.objects.get(id = pk)
        return render(request,'detail.html',{'product':product})
    
    
class Product_update(View):
    def get(self,request,pk):
        medicine = get_object_or_404(Waters,id=pk)
        form = Water_Form(instance=medicine)
        return render(request,'product_update.html',{'form':form})
    
    def post(self,request,pk):
        medicine = get_object_or_404(Waters,id=pk)
        form = Water_Form(request.POST,request.FILES,instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request,'product_update.html',{"form":form})
               
               
class Product_delete(View):
    def get(self,request,pk):
        product = get_object_or_404(Waters,id=pk)
        return render(request,'product_delete.html',{'product':product})
    
    def post(self,request,pk):
        product = get_object_or_404(Waters,id=pk)
        product.delete()
        return redirect('list')
    


