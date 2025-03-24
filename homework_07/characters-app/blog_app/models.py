from django.db import models

class Author(models.Model):
    username     = models.CharField(max_length=50, unique=True, null=False)
    fullname     = models.CharField(max_length=100, unique=False, blank=True, null=True)
    email        = models.EmailField(max_length=70, unique=True, blank=True, null=True)
    
    last_changed = models.DateTimeField(auto_now=True, null=True, blank=True) # auto_now - будет автоматически изменяться при сохранениях объекта
    created      = models.DateField(auto_now_add=True) # auto_now_add - только 1 раз запишется при первом сохранении
    
    def __str__(self):
        return self.username

class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile') # one<->one (у одного автора один профиль)
    bio    = models.TextField()
    phone  = models.CharField(max_length=25)
    
    def __str__(self):
        return self.author.username

class Post(models.Model):
    title       = models.CharField(max_length=200)
    content     = models.TextField()
    tags        = models.ManyToManyField('Tag', related_name='posts') # Достаточно только такой 
    author      = models.ForeignKey(Author,  related_name='posts', on_delete=models.CASCADE)
    rating      = models.IntegerField(default=0)

    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class Tag(models.Model): 
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    content = models.TextField()                            # Содержимое
    created_at = models.DateTimeField(auto_now_add=True)    # Дата создания (сразу флагом делаем, чтоб автоматом при создании)
    
    # попробуем many->one (много комментариев -> 1 пост)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', related_name='comments', on_delete=models.CASCADE) # Можно теперь author.comments все получить комментарии
    
    
    def __str__(self):
        return self.content  

    
    
