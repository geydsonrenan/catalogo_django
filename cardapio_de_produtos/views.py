from django.shortcuts import render, redirect

def redirecionar(request):
    return redirect('/catalogo')