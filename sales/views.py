from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Sale, Person
from .forms import SaleForm, SaleModelForm


# Create your views here.
# 브라우저에 어떤것을 보여줄것인가
# 함수로 원하는 페이지를 만들 수 있다.그리고 이걸 urls.py에 등록하면 이 함수가 보여주는 페이지로 이동한다.
def 세일목록(request):
    사람 = Sale.objects.all()
    context = {
        "사람키": 사람
    } 
    return render(request, "folder/세일목록.html", context) # context는 딕셔너리 형태

def 세일상세(request, pk):

    사람 = Sale.objects.get(id=pk)

    context = {
        "사람키": 사람
    } 

    return render(request, "folder/세일상세.html", context) # context는 딕셔너리 형태

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

def 세일_업데이트(request, pk):
    사람 = Sale.objects.get(id=pk)

    폼 = SaleForm()
    if request.method == "POST":
        폼 = SaleForm(request.POST)
        if 폼.is_valid():
            first_name = 폼.cleaned_data['first_name']
            last_name = 폼.cleaned_data['last_name']
            age = 폼.cleaned_data['age']
            person = Person.objects.first()

            사람.first_name = first_name
            사람.last_name = last_name
            사람.age = age
            사람.save()
            
            print("세일이 입력 되었습니다")

            return redirect("/홈페이지") # 홈페이지로 바로 이동

  
    context = {
        "폼키": 폼,
        "사람키": 사람
    }
    return render(request, "folder/세일_업데이트.html", context)

""" 
def 세일_입력(request):
    폼 = SaleForm()
    if request.method == "POST":
        print("포스트 메소드로 왔네요")
        폼 = SaleForm(request.POST)
        if 폼.is_valid():
            print("유효하네요")
            print(폼.cleaned_data)
            first_name = 폼.cleaned_data['first_name']
            last_name = 폼.cleaned_data['last_name']
            age = 폼.cleaned_data['age']
            person = Person.objects.first()

            # 입력받은 값으로 세일 생성
            Sale.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                person = person

            )

            print("세일이 입력 되었습니다")

            return redirect("/홈페이지") # 홈페이지로 바로 이동

    context = {
        "폼키": 폼
    }
    return render(request, "folder/세일_입력.html", context) 
 """