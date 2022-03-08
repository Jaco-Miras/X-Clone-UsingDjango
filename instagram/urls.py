from django.urls import path
from . import views
from insta.settings import DEBUG, STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-post'),
    path('edit/<int:post_id>', views.edit_post),
    path('delete/<int:post_id>', views.delete_post),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)