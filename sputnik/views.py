from django.shortcuts import render

from news.models import article, covid
from events.models import event


def index(request):
    merop = event.objects.order_by('-date')[0:3]
    merop2 = event.objects.order_by('-date')[3:6]
    merop3 = event.objects.order_by('-date')[6:9]
    info = covid.objects.all
    articles = article.objects.order_by('-date_a')[:2]
    return render(request, "index.html", {'merop': merop,'merop2': merop2,'merop3': merop3, 'info': info, 'articels': articles})

    

def info(request):
    return render(request, "information.html")

def document(request):
    return render(request, "document.html")


