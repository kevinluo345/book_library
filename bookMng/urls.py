from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('book_detail/<int:pk>', views.book_detail, name='book-detail'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),

    # make a path for book_rating
    path('book_rating/<int:book_id>', views.book_rating, name='book_rating'),
    path('about', views.about, name='about'),

    # alias for legacy link
    path('aboutus', views.about, name='aboutus'),
    path('person/<slug:slug>/', views.person_profile, name='person'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    #--------------------------- ADDED ---------------------------#
        # Search
    path("search/", views.search, name="search"),

    # Cart
    path("cart/", views.cart_view, name="cart-view"),
    path("cart/add/<int:pk>/", views.cart_add, name="cart-add"),
    path("cart/remove/<int:pk>/", views.cart_remove, name="cart-remove"),
    path("cart/clear/", views.cart_clear, name="cart-clear"),
    
    # Favorites
    path("favorites/", views.favorites, name="favorites"),
    path("favorite/toggle/<int:book_id>/", views.favorite_toggle, name="favorite-toggle"),
]
