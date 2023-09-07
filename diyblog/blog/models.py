from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class BlogAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")
    
    # def get_absolute_url(self):
    #     return reverse()
    
    def __str__(self):
        return self.user.username

class Blog(models.Model):
    blog_name = models.CharField(max_length=200)
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=150, help_text="Enter your blog text here.")
    post_date = models.DateField(default=date.today())
    
    class Meta:
        ordering = ['-post_date']
    
    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.blog_name

class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=100, help_text='Enter comment about blog here', verbose_name='Comment')
    post_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-post_date']
        
    def __str__(self):
        return self.description[:5]
