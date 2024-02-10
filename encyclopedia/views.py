import random
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from . import util
from markdown2 import Markdown
from django.shortcuts import redirect

def index(request):
   
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def newpage(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        if title in util.list_entries():
            return render (request, "encyclopedia/error.html", {
                "message" : 'Page already exist, try another'
        })
    
        util.save_entry(title,content)
        #redirecionar para pesquisa
        return redirect('template', name = title)

    return render(request, "encyclopedia/newpage.html")

def template(request, name):
    if util.get_entry(name) is None:
        return render (request, "encyclopedia/error.html", {
                "message" : 'Type name valid'
        })

    markdowner = Markdown()
    html_content = markdowner.convert(util.get_entry(name))

    return render(request, "encyclopedia/template.html", {
        "content": html_content,
        "name" : name
    })

def search(request):
    
    entries = util.list_entries()
    query = request.GET.get("q","")

    if query in entries:
        #redirecionar para pagina com a as informaçoes
        return redirect('template', name = query)
    
    results = [entry for entry in entries if query.lower() in entry.lower()]
    print(results)
    return render(request, "encyclopedia/index.html", {
    "entries": results
    })

def error(request, message):
    # Adicionar mensagem de erro erro como parametro
    return render(request, "encyclopedia/error.html", {
        "message": message
    })

def randompage(request):
    entry = util.list_entries()
    
    return redirect('template', name = random.choice(entry))

def edit(request):
    if request.method == "GET":
        name = request.GET.get("name","")
        print(name)
        return render(request, "encyclopedia/editpage.html", {
            "name": name,
            "value": util.get_entry(name)
        })

    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        return redirect('template', name = title)



