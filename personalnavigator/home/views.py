from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def process(request):
    descript = request.POST.get("text", "No Text")
    ispunc = request.POST.get("removePunctuation", "off")
    allcaps = request.POST.get("allCaps", "off")
    newlineremove = request.POST.get("newLineRemove", "off")
    spaceremove = request.POST.get("spaceRemove", "off")
    analyzed = descript
    punctuations = '''~!@#$%^&*()[]\{}|;':",./<>?`-_—'''

    if descript == "No Text":
        descript = "Enter Some Text"

    punctext = ""
    if ispunc == 'on':
        analyzed = ""
        punctext = punctext + "Removed Punctuation"
        for char in descript:
            if char not in punctuations:
                analyzed = analyzed + char
        descript = analyzed

    if allcaps == 'on':
        punctext = punctext + " | " + "All Caps (UPPER CASE)"
        analyzed = descript.upper()
        print(analyzed)
        descript = analyzed

    if newlineremove == 'on':
        punctext = punctext + " | " + "New Line Remove"
        analyzed = ''.join(descript.splitlines())
        descript = analyzed

    if spaceremove == 'on':
        punctext = punctext + " | " + "Extra Space Remove"
        analyzed = " ".join(descript.split())
        descript = str(analyzed)

    if ispunc != 'on' and allcaps != 'on' and newlineremove != 'on' and newlineremove != 'on':
        punctext = "None"
    param = {
        'purpose': punctext,
        'analyzed_text': descript
    }
    return render(request, 'process.html', param)


def social(request):
    return render(request, 'social.html')
