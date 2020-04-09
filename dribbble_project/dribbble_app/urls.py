from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'dribbble_app'
urlpatterns = [
    path('', views.index, name='index'),
    # path('blog/', views.blog, name='blog'),
    # path('mentee/', views.mentee, name='mentee'),
    # path('mentor/', views.mentor, name='mentor'),
    # path('author/', views.author, name='author'),
    # path('form/', views.forms, name='form')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)