from django.shortcuts import render,HttpResponseRedirect
import re
# Create your views here.
def home(request):
    if request.method=='POST':
        print(request.POST)
        return HttpResponseRedirect('/answer/')
    else:
        return render(request,'textEditor/home.html')

def answer(request):
    if request.method=='POST':
        text = request.POST['text']
        if 'Spaces' in request.POST:
            text = re.sub(r'[\s]','S^S',text)
        if 'Alpha' in request.POST:
            text = re.sub(r'[^a-zA-Z]','d',text)    
    else :text = 'Nothing to show'   
    return render(request,'textEditor/answer.html',{'p':text})