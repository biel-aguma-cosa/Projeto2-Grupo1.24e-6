from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'qualifications' : [
            {'name':'python'     , 'value':0},
            {'name':'java'       , 'value':1},
            {'name':'javascript' , 'value':2},
        ]
    }
    return render(request,'index.html',context)