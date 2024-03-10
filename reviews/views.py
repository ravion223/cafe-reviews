from django.shortcuts import redirect, render
from .models import Review

# Create your views here.

def get_all_reviews(request):
    reviews = Review.objects.all()

    context = {
        "reviews": reviews
    }

    return render(
        request,
        "reviews/reviews_list.html",
        context
    )


def review_form(request):
    if request.method == "GET":
        return render(request, "reviews/review_form.html")
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")

    review = Review.objects.create(
        author = request.user,
        title = title,
        content = content
    )
    
    return redirect("reviews-list")