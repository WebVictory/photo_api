from rest_framework import mixins
from rest_framework import viewsets, permissions
from photo.models import Photo, PhotoPeople
from photo.serializers import PhotoSerializer, PhotoListSerializer, PhotoPeopleSerializer


class PhotoListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint working with photo
    """
    serializer_class = PhotoListSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Photo.objects.all()
    filterset_fields = ['geo_location', 'created_at', 'photo_people__name']


# 3) получать фотографию по айди с метаданными.
# используем миксины чтобы убрать отображение списка
class PhotoViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

# автодополнение по поиску возможных имен людей присутствующих на фотографиях
class SearchName(mixins.ListModelMixin, viewsets.GenericViewSet):
    search_fields = ['^name']
    serializer_class = PhotoPeopleSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = PhotoPeople.objects.order_by("name").values('name').distinct()