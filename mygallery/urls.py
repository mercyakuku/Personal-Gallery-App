from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'index'),
    path('search/', views.search_image, name='search_image'),
    path('location/(\d+)', views.location_filter, name='location_filter'),
    path('image/(\d+)',views.categories, name = 'categories'),
]
    # re_path(r'^search/', views.search_results, name='search_results'),
    # re_path(r'location/(\d+)', views.get_location, name = 'get_location'),
    # re_path(r'delete/(\d+)', views.delete_image, name = 'delete_image'),

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
