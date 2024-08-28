from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', )

def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
    # Get value for checkbox
    djcheckbox = request.POST.get('removepunch','off')
    djcheckbox2 = request.POST.get('fullcaps','off')
    djcheckbox3 = request.POST.get('nocaps','off')
    djcheckbox4 = request.POST.get('newlineremover','off')
    djcheckbox5 = request.POST.get('extraspaceremover','off')
    djcheckbox6 = request.POST.get('countcharacter','off')
    # Check all the checkboxes
    if djcheckbox == "on":
        analyzetext = ""
        punctuations = '''`~!@#$^&*()-_{}[]\/'".,;:<>?%'''
        for char in djtext:
            if char not in punctuations:
                analyzetext = analyzetext + char

        wow = {'purpose':'Removed Punctuations', 'analyzed_text':analyzetext}     
        djtext = analyzetext

    if djcheckbox2 == "on":
        analyzetext = ""
        text = djtext.upper()
        for char in text:
                analyzetext = analyzetext + char

        wow = {'purpose':'Removed Punctuations and UPPER CASE', 'analyzed_text':analyzetext}        
        djtext = analyzetext 

    if djcheckbox3 == "on":
        analyzetext = ""
        text = djtext.lower()
        for char in text:
                analyzetext = analyzetext + char

        wow = {'purpose':'Removed Punctuations and UPPER CASE', 'analyzed_text':analyzetext}        
        djtext = analyzetext    

    if djcheckbox4 == "on":
        analyzetext = ""

        for index , char in enumerate(djtext):
            if char != '\n' and char != '\r':
                analyzetext = analyzetext + char

        wow = {'purpose':'Removed Punctuations and UPPER CASE and New Line Remover', 'analyzed_text':analyzetext}        
        djtext = analyzetext    

    if djcheckbox5 == "on":
        analyzetext = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzetext = analyzetext + char       
                
        wow = {'purpose':'Extra Space Remover', 'analyzed_text':analyzetext} 
        djtext = analyzetext

    if djcheckbox6 == "on":
        analyzetext2 = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " ":
                pass
            else:
                analyzetext2 = analyzetext2 + char

        analyzetext = len(analyzetext2)        

        wow = {'purpose':'Character Counter', 'analyzed_text':f'The Number of character in our text is: {analyzetext}'}        

    if djcheckbox != "on" and djcheckbox2 != "on" and djcheckbox3 != "on" and djcheckbox4 != "on" and djcheckbox5 != "on" and djcheckbox6 != "on":     
        return HttpResponse("ERROR! You have not selected any operation. Please select any operation and try again.")
    
    return render(request, 'analyze.html', wow)    