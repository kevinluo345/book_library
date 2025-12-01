from django.contrib import admin

# Register your models here.


from .models import MainMenu
from .models import Book
from .models import Rating, Review, Message, Favorite



admin.site.register(MainMenu)
admin.site.register(Book)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(Message)
admin.site.register(Favorite)

