from django.shortcuts import render


def perfil_uno (request):
    data={"nombre":"mario", "año":1900, "correo":"mario@bros.com"}
    return render(request, "perfil/p1.html", data)


def perfil_dos (request):
    data={"nombre":"luigi", "año":1905, "correo":"luigi@bros.com", "foto":"luigi.jpg"}
    return render(request, "perfil/p2.html", data)