from django.urls import path
from .views import 세일목록,세일상세,세일_입력, 세일_업데이트

app_name = "홈페이지11111111111" # urls 프로젝트 수준과 연결하기 위해서 app_name이 필요하다.

urlpatterns = [
    path('', 세일목록),
    path('<int:pk>/', 세일상세), # pk로 연결할 수 있다.
    path('<int:pk>/업데이트/', 세일_업데이트),
    path('make/', 세일_입력),

]