from django import forms
from menu.models import Food


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name', 'description', 'price', 'is_available', 'image', 'category')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم غذا'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'cols': 30, 'rows': 5}),
            'price': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'قیمت'}),
            'is_available': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }