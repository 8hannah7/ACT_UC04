from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

layout = """
<h1> Proyecto Web (LP3) | roxana  </h1>
<hr>
<ul>
        <li>
        <a href="/intregrantes"> Integrantes</a>
        </li>
        <li>
        <a href="/saludo"> Mensaje de saludo</a>
        </li>
        <li>
       
</ul>
</hr>
"""
def index(request):
    estudiante=['roxana condori condori',                
                'Antony vasques'
                'fernando acuña',                
                ]
    estudiantes = []

    return render(request,'index.html', {
        'titulo':'integrantes',
        'autor':' @hannah0807',
        'mensaje':'Proyecto web con Django (Desde el view)',
        'estudiantes':estudiantes
    })
def saludo(request):
    
    return render(request,'saludo.html',{
        'titulo':'saludo',
        'autor':'hannah'
    }
    
    )

