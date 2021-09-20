# I HAVE CREATED THIS FILE - MANN
from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    return render(req, 'index.html')

def analyze(req):
    # GET THE TEXT
    djtext = req.POST.get('text', 'default')

    # CHECK CHECKBOX VALUES
    removepunc = req.POST.get('removepunc', 'off')
    fullcaps = req.POST.get('fullcaps', 'off')
    newlineremover = req.POST.get('newlineremover', 'off')
    extraspaceremover = req.POST.get('extraspaceremover',  'off')
    charcounter = req.POST.get('charcounter', 'off')

    # NECESSARY VARIABLES
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
    analyzed = ""

    # CHECK WHICH CHECKBOXES ARE ON
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Line Character', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        analyzed = djtext.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcounter == "on":
        c = len(djtext)
        analyzed = analyzed + "\n" f"The number of characters in the given string are {c}"
        params = {'purpose': 'Counted The Number of Characters', 'analyzed_text': analyzed}

    if charcounter != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on" and removepunc != "on":
        return HttpResponse("Please select atleast one operation")

    return render(req, 'analyze.html', params)
