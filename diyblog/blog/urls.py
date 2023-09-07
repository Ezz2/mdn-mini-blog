from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs', views.BlogListView.as_view(), name='blogs-list'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers', views.BloggersListView.as_view(), name="bloggers-list"),
    path('blogger/<int:pk>', views.BloggersDetails.as_view(), name="blogger-detail"),
    path('<int:pk>/create', views.BlogCommentCreate.as_view(), name="create-comment"),
    path('signup', views.signup, name="signup"),
]
