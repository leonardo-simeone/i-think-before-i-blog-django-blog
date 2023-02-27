from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))

# The model for posts
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # One to many relationship one author can have many posts
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    # helper methods
    class Meta:
        ordering = ['-created_on']  # this means we're gonna order based on the created on date field and the minus means in descending order (newest to oldest)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

# The model for comments


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # one to many relationship one post can have many comments
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


    class Meta:
        ordering = ['created_on']  # ascending order so the oldest comments are listed first, since we want it ot be a conversation

        def __str__(self):
            return f'Comment {self.body} by {self.name}'
