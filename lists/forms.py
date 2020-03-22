from django import forms
from .models import Item

class ItemForm(forms.models.ModelForm):

    class Meta:

        EMPTY_ITEM_ERROR = "You can't have an empty list item"

        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }


    def save(self, for_list, commit=True ):
        self.instance.list = for_list
        return super().save()
