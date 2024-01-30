from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

# Create your views here.
def catalogo(request):
    var = False
    if request.method == 'GET':
        produtos =  Produto.objects.filter(disponivel=True)
        return render(request, 'catalogo.html', {'produtos': produtos})
    elif request.method == 'POST':
        pesquisa = request.POST.get('pesquisa')
        pesquisa = pesquisa.split()
        produtos = Produto.objects.filter(disponivel=True)
        print(pesquisa)
        for i in range(len(pesquisa)):
            if produtos.filter(nome__contains=pesquisa[i]):
                var = True
                produtos = produtos.filter(nome__contains=pesquisa[i])
        if var == False and pesquisa != []:
            produtos = produtos.filter(nome__contains=pesquisa[0])
        return render(request, 'catalogo.html', {'produtos': produtos})
