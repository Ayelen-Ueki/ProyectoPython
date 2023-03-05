from django.urls import path
from AppCafeReview.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ("verReviews/", view_reviews, name="view_reviews"), 
    path("crearReview/", create_review, name="create_review"),
    path("buscarReview/", search, name="search"), 
    path("resultadoReviews/", results, name="results"),
    path("borrarReviewss/<reviewer>", delete_review, name="delete_review"), 
    path("editarReview/<reviewer>", edit_review, name="edit_review"),
    path("registroUsuario/", register_user, name="register_user"),
    path("inicioSesionUsuario/", login_user, name="login_user"),
    path("logout/", logout.view.as_view('logout'), name="logout")
]