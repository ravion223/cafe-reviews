from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_reviews, name = "reviews-list"),
    path('review-form/', review_form, name = "review-form"),
]