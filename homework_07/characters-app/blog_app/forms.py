from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(
        label='Заголовок',
        max_length=200,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 
                   'placeholder': 'Введите заголовок'
            }
        ), # Внутри bootstrap вроде
    )
    
    content = forms.CharField(
        label='Содержание',
        widget=forms.Textarea(
            attrs={'class': 'form-control', 
                   'placeholder': 'Введите текст',
                   'row': 5, # Ограничим кол-во строк (?) не работает так почему-то
            }
        ),   
    )
    
    rating = forms.IntegerField(
        label='Рейтинг',
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(
            attrs={'class': 'form-control',
                   'place_holder': 'Введите рейтинг' 
            }
        )
    )
    
    # Все это импортируем уже в views.py
    
    
# Можно еще так создавать:
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'rating', 'tags', 'author']
        labels = {
            'title': 'Заголовок',
            'content': 'Содержимое',
            'rating': 'Рейтинг',
            'tags': 'Теги',
            'author': 'Автор'
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите содержимое'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите рейтинг'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
        
