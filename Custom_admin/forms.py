from Store.models import Product
from django import forms

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['image_1'].widget.attrs.update({'class': 'file-input'})
        self.fields['image_2'].widget.attrs.update({'class': 'file-input'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control'})
        self.fields['image_3'].widget.attrs.update({'class': 'file-input'})
        self.fields['Brad'].widget.attrs.update({'class': 'form-control input-sm'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['image_1'].widget.attrs.update({'class': 'file-input'})
        self.fields['image_2'].widget.attrs.update({'class': 'file-input'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control'})
        self.fields['image_3'].widget.attrs.update({'class': 'file-input'})
        self.fields['Brad'].widget.attrs.update({'class': 'form-control input-sm'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
