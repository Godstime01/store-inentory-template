from django.forms import ModelForm

from .models import Item

class AddForm(ModelForm):
          class Meta:
                    model = Item
                    field = "__all__"
                    

class EditForm(ModelForm):
          class Meta:
                    model = Item
                    field = "__all__"

