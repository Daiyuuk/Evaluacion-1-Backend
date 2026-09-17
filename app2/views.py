from django.shortcuts import render

def vista1_app2(request):
    return render(request, 'app2/vista1_app2.html')

def vista2_app2(request):
    return render(request, 'app2/vista2_app2.html')