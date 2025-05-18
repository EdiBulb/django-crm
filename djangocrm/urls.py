from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from sales.views import 첫화면 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', 첫화면),
    path('홈페이지/', include('sales.urls', namespace="홈페이지")), # sales 수준을 연결시켜줌
]
