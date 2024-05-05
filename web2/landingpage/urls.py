
from django.urls import path,include
from . import views

urlpatterns = [
    path('questions',views.questions,name='questions'),
    path('predict', views.predict,name='predict'),
    path('forum', views.forum),
]
