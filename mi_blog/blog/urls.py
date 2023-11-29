from django.urls import path, include
from .views import DetailPostView, LikePost, Featured, DeletePostView, Index, Busqueda

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', DetailPostView.as_view(), name='detail_post'),
    path('<int:pk>/like', LikePost.as_view(), name='like_post'),
    path('featured/', Featured.as_view(), name='featured'),
    path('<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('Busqueda/', Busqueda, name='blog-search-post'),
]