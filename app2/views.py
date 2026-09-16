from django.shortcuts import render

def vista1_app2(request):
    return render(request, 'app1/vista1_app1.html')

def vista2_app2(request):
    return render(request, 'app1/vista2_app1.html')