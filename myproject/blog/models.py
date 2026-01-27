from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length =20)
    def __str__(self):
        return f"{self.caption}" 
    
class Author(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
   
    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
    

class Posts(models.Model):
    title = models.CharField(max_length = 100)
    excerpt = models.CharField(max_length = 200)
    content = models.TextField(validators = [MinLengthValidator(10)])
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to = "posts", null = True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL ,related_name="posts" , null = True)
    slug = models.SlugField(unique=True, db_index=True)
    tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name= "comments")
    
    def __str__(self):
        return f"Comment by {self.user_name} on {self.post}"
    

    
    