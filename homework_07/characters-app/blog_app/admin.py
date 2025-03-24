from django.contrib import admin
from .models import Post, Tag, Comment, Author, AuthorProfile

# 1 - добавляем модель поста
@admin.register(Post)
class PostAdmin(admin.ModelAdmin): # Так по-умолчанию
    list_display = ('title', 'author', 'rating', 'created_at')
    ordering = ('created_at', 'author',) # По приоритету будет порядок 
    #(можно делать '-created_at', чтобы был обратный порядок. Но это можно менять также на самой странице с постами)

    # Можно делать фильтрацию 
    list_filter = ('author', 'rating') # На странице будут графы, где мы сможем выбирать конкретного автора сбоку

    # Можно использовать поиск (задать по чему именно сможем искать)
    search_fields = ('title', 'content') 
    search_help_text = ('Поиск по title или content')

    # Можно указать поля, которые мы можем менять через админку (Чтобы с админки нельзя было менять другое, например rating)
    # fields = ['title', 'content', 'created_at', 'rating']
    readonly_fields = ['created_at', 'rating'] # Можно еще указать то, что будет видно, но нельзя менять

    # Можно сгруппировать поля (это заменяет fields)
    fieldsets = [
        (None, 
         {'fields': ['title', 'author']}),
        
        ('Содержимое', 
         {'fields': ['content']}),
        
        ('Служебная информация', 
         {'fields': ['created_at', 'rating']}),         
    ]
    
    ### Создание экшнов
    @admin.action(description='Установить рейтинг 100')
    def set_rating_100(self, request, queryset):
        for post in queryset:
            post.rating = 100
            post.save()
        self.message_user(request, message='Rating set go 100')
        # После этого мы должны зарегистирровать экшн
        
    actions = [set_rating_100]

# Второй способ но с указанием настроек - СТАРАЯ ВЕРСИЯ
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('username', 'fullname', 'email', 'created')
    ordering = ('-created',)
    search_fields = ('username', 'email')
    search_help_text = ('Поиск по username или email')
    
    # В админке можно добавлять какие-либо действия:
    def profile_bio(self, obj):
        return obj.profile.bio if obj.profile else 'No bio'
    profile_bio.short_description = 'Bio'
    
admin.site.register(Author, AuthorAdmin)

@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ['author', 'phone', 'bio']
    ordering = ['author']
    search_fields = ['author']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'content', 'author']
    fields = ['content', 'post', 'author']
    readonly_fields = ['post', 'author']
    
    
    @admin.action(description='Удалить комментарии')
    def delete_all_comments(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, message=f'Удалено {count} комментариев')
    
    actions = [delete_all_comments]