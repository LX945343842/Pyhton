from django.shortcuts import render
from django.http import HttpResponse
from .movie_top250 import get_data
from .models import movieinfo

def index(request,page=1):
    page = int(page)
    m_info = movieinfo.objects.all()
    if page>1:
        return render(request,'movies.html',{'m_info': m_info[(page-1)*25:page*25],'next':page+1,'up':page-1})
    else:
        return render(request,'movies.html', {'m_info': m_info[:25],'next':page+1})

def pa(request):
    get_data()
    return HttpResponse('ok!')

def detail(request,id):
    info = movieinfo.objects.get(pk=id)
    return render(request,'detail.html',{'name':info.mName,'director':info.mDirectors,'score':info.mScore,'quote':info.mQuote})