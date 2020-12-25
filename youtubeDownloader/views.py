from django.shortcuts import render
from django.http import JsonResponse
from django.http import FileResponse
from pytube import YouTube

# Create your views here.
def Downloader(request):
    template_name='downloader.html'
    if request.method=='POST':
        url=request.POST.get('link')
        res=request.POST.get('res')
        yt = YouTube(url)
        streams = yt.streams.filter(res=res).all()
        return FileResponse(open(streams[0].download(skip_existing=True),'rb'),as_attachment=True)
    else:
        return render(request,template_name)
