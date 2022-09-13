from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Books

def index(request):
  mybook = Books.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mybook': mybook
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

  
def addrecord(request):
  z = request.POST['second']
  x = request.POST['first']
  y = request.POST['last']
  book = Books(bookcode=z, booktitle=x, author=y)
  book.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  book = Books.objects.get(id=id)
  book.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mybook = Books.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mybook': mybook
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  z = request.POST['second']
  x = request.POST['first']
  y = request.POST['last']
  book = Books.objects.get(id=id)
  book.bookcode = z
  book.booktitle = x
  book.author = y
  book.save()
  return HttpResponseRedirect(reverse('index'))