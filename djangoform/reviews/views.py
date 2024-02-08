from typing import Any
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import ReviewForm
from . models import review
from django.views.generic import View,TemplateView,UpdateView,ListView,DetailView,DeleteView
from django.views.generic.edit import DeleteView


# Create your views here.

# def home(request):

#     if request.method == "POST":
#         un = request.POST['username']
#         if un == '':
#             return render(request,'reviews/home.html',{'error':True})
#         print(un)
#         return HttpResponse('Thank You')
#     return render(request,'reviews/home.html',{'error':False})

# def home(request):

#     if request.method == "POST":
#         a = ReviewForm(request.POST)
#         a.save()
#         return HttpResponse('Thank You')
        
#     else:
#         a= ReviewForm()
#     return render(request,'reviews/home.html',{'form':a})


# def update(request,pk):
#     if request.method == "POST":
#         data =review.objects.get(id = pk)
#         a = ReviewForm(request.POST,instance = data)
#         a.save()
#         return HttpResponse('Update Successful')
#     else:
#         a = ReviewForm()
#     return render(request,'reviews/home.html',{'form':a})

class AddView(View):
    def get(self,request):
        a= ReviewForm()
        return render(request,'reviews/home.html',{'form':a})
        

    def post(self,request):
            a = ReviewForm(request.POST)
            a.save()
            return redirect('reviews:success')
    

class SuccessView(TemplateView):
    template_name = "reviews/success.html"

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context["message"] = "Data Stored Successfully to Database Table"
        return context


class EditView(UpdateView):
    template_name = 'reviews/home.html'
    model = review
    fields =['username','feedback','ratings']
    success_url = '/create'


class DispView(ListView):
    model = review
    template_name = 'review/list.html'

class DataView(DetailView):
    model = review
    template_name = 'reviews/details.html'


class DropView(DeleteView):
    model = review
    template_name = 'reviews/delete.html'
    success_url = '/display'


     

  


