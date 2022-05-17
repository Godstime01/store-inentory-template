from django.shortcuts import render

from .models import Item
from .forms import AddForm, EditForm
# Create your views here.

def dashboard(request):
          items = Item.objects.all()
          return render(request, 'dashboard.html', {'items': items})

def add_product(request):
          if request.method == "POST":
                    form = AddForm(request.post)
                    
                    if form.is_valid():
                              form.save()
          else:
                    form = AddForm()
          return render(request, 'add_item.html', {'form': form})

def edit_product(request, pk):
          item = Item.objects.get(pk = pk)
          if request.method == "POST":
                    form = EditForm(request.post, instance=item)
                    
                    if form.is_valid():
                              form.save()
          else:
                    form = EditForm(instance=item)
          return render(request, 'update.html', {'form': form})

def delete_product(request, pk):
          item = Item.objects.get(pk = pk)
          item.delete()
          return render(request, 'update.html')