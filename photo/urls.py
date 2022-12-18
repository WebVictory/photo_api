from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from photo import views

router = routers.DefaultRouter()
#список фото без мета-данных
router.register(r'photo_list', views.PhotoListViewSet, basename='photo_list')
#одно фото с мета-данными
router.register(r'photo', views.PhotoViewSet, basename='photo')
# поиск и автодополнение имени
router.register(r'search_name', views.SearchName, basename='search_name')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)