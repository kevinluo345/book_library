from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MainMenu(models.Model):
    item = models.CharField(max_length=300, unique=True)
    link = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.item

class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    publishdate = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

# adding a rating feature
class Rating(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('book', 'user')  # prevents duplicate ratings per user/book

    def __str__(self):
        return f"{self.user.username} rated {self.book.name} - {self.value}"

#---------------------------- ADDED ----------------------------#
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    reviewer_name = models.CharField(max_length=120)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} rated {self.book.name} {self.rating}"


class Message(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'book')
        ordering = ['-added_at']
    
    def __str__(self):
        return f"{self.user.username} favorited {self.book.name}"