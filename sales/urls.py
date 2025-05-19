from django.urls import path
from .views import 세일목록,세일상세,세일_입력, 세일_업데이트,세일_지우기,세일_입력View, 세일목록View,세일상세View,세일_업데이트View,세일_지우기View

app_name = "홈페이지11111111111" # urls 프로젝트 수준과 연결하기 위해서 app_name이 필요하다.

urlpatterns = [
    path('', 세일목록View.as_view(), name='목록'),
    path('<int:pk>/', 세일상세View.as_view(), name='상세'), # pk로 연결할 수 있다.
    path('<int:pk>/업데이트/', 세일_업데이트View.as_view(), name='업뎃'),
    path('<int:pk>/지우기/', 세일_지우기View.as_view(), name='지우기'),
    path('ma_monde/', 세일_입력View.as_view(), name='생성'),

]