from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Author
from .forms import PostForm, PostModelForm

def index(request):
    return render(request, template_name='blog_app/index.html')

def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    
    return render(request, template_name='blog_app/post_list.html', context=context)

def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    
    return render(request, template_name='blog_app/author_list.html', context=context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, template_name='blog_app/post_detail.html', context=context)
   
def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {'author': author}
    return render(request, template_name='blog_app/author_detail.html', context=context) 

def about(request):
    return HttpResponse("<h1>About page</h1><br>Ebat about nahuy")

#--------------------------------------------------------------------------------------
def add_post1(request):
    """
    form = PostForm()
    """
    if request.method == 'POST':
        form = PostForm(request.POST) # Засовываем данные из запроса
        
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            rating = form.cleaned_data['rating']
            author = Author.objects.first() # Пока не знаем как узнать автора
            
            Post.objects.create(title=title, content=content, rating=rating, author=author)
            return redirect('post_list') # Перенаправление на другую страницу
        
        else:
            return ('Data is not valid', 422)
        
    else:
        form = PostForm() # Если будет не POST, а GET, тогда мы вернем страницу, в которой заполняется форма 
        context = {'form': form}
        
    return render(request, 'blog_app/add_post.html', context)
            
def add_post2(request):
    """
    form = PostModelForm()
    """
    if request.method == 'POST':
        form = PostModelForm(request.POST) # Засовываем данные из запроса
        
        if form.is_valid():
            # Можно сразу сохранить форму в БД
            form.save()
            
            return redirect('post_list') # Перенаправление на другую страницу
        
        else:
            return ('Data is not valid', 422)
        
    else:
        form = PostModelForm() # Если будет не POST, а GET, тогда мы вернем страницу, в которой заполняется форма 
        context = {'form': form}
        
    return render(request, 'blog_app/add_post.html', context)
        
        