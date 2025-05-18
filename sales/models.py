from django.db import models
from django.contrib.auth.models import AbstractUser # 장고에서 제공하는 회원관리 모델


class 아이디(AbstractUser):
    pass # 다 갖다 쓴다.


# 데이터 베이스를 만든다
class Sale(models.Model):
   
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    person = models.ForeignKey("Person", on_delete=models.CASCADE) # foreignkey를 지정함. cascade는 person 지워지면 같이 지워지게 한다. 

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Person(models.Model):
    회원 = models.OneToOneField(아이디, on_delete=models.CASCADE) # 1대1로 회원 모델을 만들었다.

    def __str__(self):
        return self.회원.username