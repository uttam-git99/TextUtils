#create by me
from django.http import HttpResponse
from django.shortcuts import render
def index(requst):
    return render(requst,"index.html")

def analyze(requst):
    djtext1 = requst.POST.get('text','defult')
    djtext = requst.POST.get('text','defult')
    removepuc= requst.POST.get('removepuc','off')
    fullcap= requst.POST.get('fullcap','off')
    count= requst.POST.get('count','off')
    spaceremover= requst.POST.get('spaceremover','off')
    newlineremove= requst.POST.get('newlineremove','off')
    analyzed = djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepuc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':"removing ", 'analyzed_text':analyzed}
        djtext=analyzed

    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char !="/n" and char!= "/r":
                analyzed = analyzed + char
        params = {'purpose':"removing ", 'analyzed_text':analyzed}
        djtext=analyzed

    if fullcap == "on":
        analyzed = ""
        for char in djtext:
            analyzed= analyzed+char.upper()
        params = {'purpose': "UpperCase", 'analyzed_text': analyzed}

        djtext=analyzed

    if spaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] ==" " and djtext[index+1]=="  "):
                analyzed= analyzed+char
        params = {'purpose': "UpperCase", 'analyzed_text': analyzed}
        djtext=analyzed

    if count == "on":
        count1 = 0
        for char in djtext:
            if char not in punctuations:
                pass
                if char!=" " and char!="\n" and char!="\r":
                    count1=count1+1
        params = {'purpose': " ", 'analyzed_text':analyzed,'count':"No of character is:-  "+ str(count1)}
        djtext= analyzed

        analyzed=djtext1
    if (count == "off" and  spaceremover== "off" and removepuc== "off" and fullcap== "off" and newlineremove == "off"):
        params = {'purpose': "", 'analyzed_text':djtext1}
        return render(requst,'Error.html',params)

    return render(requst, 'analyze.html', params)



