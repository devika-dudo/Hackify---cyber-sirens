from django.shortcuts import render
from django.http import HttpResponse
from joblib import load
model1= load('./notebook/model1.joblib')

# Create your views here.
def questions(request):
    return render(request,'questions.html')

def forum(request):
    return render(request,'forum.html')

def predict(request):
    q1=request.GET['age']
    q2=request.GET['q2']
    q3=request.GET['q3']
    q4=request.GET['q4']
    q5=request.GET['q5']
    q6=request.GET['q6']
    q7=request.GET['q7']
    q8=request.GET['q8']
    q9=request.GET['q9']
    q10=request.GET['q10']
    q11=request.GET['q11']
    q12=request.GET['q12']
    q13=request.GET['q13']
    q14=request.GET['q14']
    y_pred=model1.predict([[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14]])
    print(y_pred)
    return render(request,'predict.html')