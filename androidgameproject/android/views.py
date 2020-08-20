from django.shortcuts import render
from android.models import User,Games,File,allview,videomodel,gmaeimg
from django.shortcuts import redirect
from android.forms import DocumentForm,videoform
from django.http import HttpResponse


# Create your views here.
def gamepro(request):
    Files=File.objects.all()
    vid=videomodel.objects.all()
    pic=gmaeimg.objects.all()
    return render(request,'index.html',{'Files':Files,'vid':vid,'pic':pic})

def gamevi(request):
    Files=File.objects.all()
    vid=videomodel.objects.all()
    pic=gmaeimg.objects.all()
    return render(request,'in.html',{'Files':Files,'vid':vid,'pic':pic})


def searchmatch(query, item):
    if  gmaeimg.objects.filter(title__icontains=query):
        return True
    else:
        return False


def search(request):
    query=request.GET.get('search')
    prot =  gmaeimg.objects.filter(title__icontains=query)
    pic=[item for item in prot if searchmatch(query,item)]
    return render(request,'search.html',{'pic':pic})

def imageview(request, myid):
    prod=File.objects.filter(id= myid)
    return render(request,'image.html',{'prodd':prod})

def allimageview(request):
    allresult=allview.objects.all()
    return render(request,'allview.html',{'allresult':allresult})

def userview(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/all')

    form = DocumentForm()
    return render(request, 'userform.html', {
        'form': form
    })


def videoview(request):
    if request.method == 'POST':
        form = videoform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/game')

    form = videoform()
    return render(request, 'video.html', {
        'form': form
    })


