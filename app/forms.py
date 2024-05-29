from django import forms
from app.models import Product
from app.models import Comment
from app.models import Order

class ProductForms(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
    image = forms.ImageField()
    rating = forms.ChoiceField(choices =Product.RatingChoices.choices )
    discount = forms.IntegerField()




# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'email', 'body')

# class ProductModelForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         exclude = ()



class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username','email','comment']



class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer','phone_number']
    
