from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('picture', 'price', 'name', 'date_added', "weight", "producer", "note")

# Creating a form to add an article.


# Creating a form to change an existing article.
#         article = Product.objects.get()
#         form = ArticleForm(instance=article)
class ProductFormEdit(ModelForm):
    class Meta:
        model = Product
        fields = ('picture', 'price', 'name', 'date_added', "weight", "producer", "note")