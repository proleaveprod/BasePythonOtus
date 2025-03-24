from django.core.management.base import BaseCommand
from blog_app.models import Author, AuthorProfile, Post, Tag, Comment
from faker import Faker # Для создания липовой информации
import random

class Command(BaseCommand):
    help = 'Сгенерировать тестовые данные'
    
    def handle(self, *args, **kwargs): # Главная функция, которую мы будем выполнять
        self.stdout.write("Deleting data...")
        Author.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()
        Tag.objects.all().delete()
        
        self.stdout.write("Generating test data...")
        faker = Faker('ru_RU')

        AUTHORS = 20
        TAGS = 5
        POSTS = 100
        COMMENTS = 30
        
        authors = []
        for _ in range(AUTHORS):
            username = faker.user_name()
            fullname = faker.name() if random.random() < 0.7 else None
            email = faker.email() if random.random() < 0.5 else None
            
            author = Author.objects.create(
                username = username,
                fullname = fullname,
                email = email
            )
            authors.append(author)
            self.stdout.write(f"Created Author {username}")

        tags = []
        for _ in range(TAGS):
            name = faker.word()
            
            tag = Tag.objects.create(
                name = name
            )
            tags.append(tag)
            self.stdout.write(f"Created Tag {name}")
    
        posts = []
        for _ in range(POSTS): 
            title = faker.sentence(nb_words=5, variable_nb_words=True)[:-1]
            content = faker.paragraph(nb_sentences=30, variable_nb_sentences=True)
            author = random.choice(authors)
            rating = random.randint(0,100)
        
            post = Post.objects.create(
                title = title,
                content = content,
                author = author,
                rating = rating,
            )
            
            if random.random() < 0.6:
                post.tags.add(random.choice(tags))
            
            posts.append(post)
            self.stdout.write(f"Created Post {title}")
            
        comments = []
        for _ in range(COMMENTS):
            content = faker.sentence(nb_words=5, variable_nb_words=True)
            post = random.choice(posts)
            author = random.choice(authors)
            
            comment = Comment.objects.create(
                content = content,
                post = post,
                author = author,
            )
            
            comments.append(comment)
            self.stdout.write(f"Created Comment of Post {post.title}")
        
        
        self.stdout.write("Generating success")
        
        
    # Теперь можно запустить python manage.py generate_test_data
    
    
    # У django куча дополнений (django packageю Есть на djangopackages.org куча всякой хуеты такой)
    # Например admin styling