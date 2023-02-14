from django.urls import path
from AppCafeReview.views import *

urlpatterns = [
    path ("verReviews/", view_reviews), 
    path("crearReview/", create_review),
    path("buscarReview", search), 
    path("resultadoReviews/", results),
]