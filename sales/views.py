from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Sale, Person
from .forms import SaleForm, SaleModelForm, 우리만의UserCreationForm
from django.views import generic
from django.urls import reverse


# Create your views here.
# 브라우저에 어떤것을 보여줄것인가
# 함수로 원하는 페이지를 만들 수 있다.그리고 이걸 urls.py에 등록하면 이 함수가 보여주는 페이지로 이동한다.

class 회원가입View(generic.CreateView):
    template_name = "회원가입/가입.html"
    form_class = 우리만의UserCreationForm
    def get_success_url(self):
        return reverse("로긴")
    


class 첫화면View(generic.TemplateView):
    template_name = "첫화면.html"

def 첫화면(request):
    return render(request, "첫화면.html")

class 세일목록View(generic.ListView):
    template_name = "folder/세일목록.html"
    queryset = Sale.objects.all()
    context_object_name = "사람키"

def 세일목록(request):
    사람 = Sale.objects.all()
    context = {
        "사람키": 사람
    } 
    return render(request, "folder/세일목록.html", context) # context는 딕셔너리 형태

class 세일상세View(generic.DetailView):
    template_name = "folder/세일상세.html"
    queryset = Sale.objects.all()
    context_object_name = "사람키"

def 세일상세(request, pk):

    사람 = Sale.objects.get(id=pk)

    context = {
        "사람키": 사람
    } 

    return render(request, "folder/세일상세.html", context) # context는 딕셔너리 형태


class 세일_입력View(generic.CreateView):
    template_name = "folder/세일_입력.html"
    form_class = SaleModelForm
    def get_success_url(self):
        return reverse("홈페이지:목록")

def 세일_입력(request):
    폼 = SaleModelForm()
    if request.method == "POST":
        폼 = SaleModelForm(request.POST)
        # valid한지 검증 해야한다.
        if 폼.is_valid():
            폼.save()


            return redirect("/홈페이지") # 홈페이지로 바로 이동

    context = {
        "폼키": 폼
    }
    return render(request, "folder/세일_입력.html", context) 


class 세일_업데이트View(generic.UpdateView):
    template_name = "folder/세일_업데이트.html"
    queryset=Sale.objects.all()
    form_class = SaleModelForm
    context_object_name = "사람키"
    def get_success_url(self):
        return reverse("홈페이지:목록")
    

def 세일_업데이트(request, pk):
    사람 = Sale.objects.get(id=pk)

    폼 = SaleModelForm(instance=사람)
    if request.method == "POST":
        폼 = SaleModelForm(request.POST, instance=사람)
        if 폼.is_valid():
            폼.save()
            

            return redirect("/홈페이지") # 홈페이지로 바로 이동

  
    context = {
        "폼키": 폼,
        "사람키": 사람
    }
    return render(request, "folder/세일_업데이트.html", context)


class 세일_지우기View(generic.DeleteView):
    template_name = "folder/세일_지우기.html"
    queryset = Sale.objects.all()
    def get_success_url(self):
        return reverse("홈페이지:목록")

def 세일_지우기(request, pk):
    사람 = Sale.objects.get(id=pk)
    사람.delete()
    return redirect("/홈페이지")
