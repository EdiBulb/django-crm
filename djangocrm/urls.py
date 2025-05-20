from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from sales.views import 첫화면, 첫화면View, 회원가입View
from django.contrib.auth.views import LoginView, LogoutView # django에 있는 로그인, 로그아웃 기능 사용

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', 첫화면View.as_view()),
    path('홈페이지/', include('sales.urls', namespace="홈페이지")), # sales 수준을 연결시켜줌
    path('로그인/', LoginView.as_view(), name='로긴'),
    path('로그아웃/', LogoutView.as_view(), name='록아웃'),
    path('회원가입/', 회원가입View.as_view(), name='가입'),

]
