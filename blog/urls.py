from . import views
from django.urls import path


# the first slug is called a path converter which converts the text into a slug field and the second one is a
# keyword name and the keyword name matches
# the 'slug' parameter in the get method 'post = get_object_or_404(queryset, slug=slug)'
# in the blog/views.py file, that's how we link them together
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
