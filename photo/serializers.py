from rest_framework import serializers

from photo.models import Photo, PhotoPeople


class PhotoPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoPeople
        fields = [ 'name',]


class PhotoSerializer(serializers.ModelSerializer):
    photo_people = PhotoPeopleSerializer(many=True, required=False)
    class Meta:
        model = Photo
        fields = ['photo', 'geo_location', 'description','photo_people' ]


    def create(self, validated_data):
        #сохраняем фото
        photo = Photo.objects.create(**validated_data)
        # сохраням люей на фото
        photo_people = validated_data.pop('photo_people')
        if photo_people:
            for people_data in photo_people:
                PhotoPeople.objects.create(photo=photo, **people_data)
        return photo

    def update(self, instance, validated_data):
        # сохраняем фото
        photo_people = validated_data.pop('photo_people')
        photo = super(PhotoSerializer, self).update(instance, validated_data)
        #если данных немного можно просто удалять и создавать заново если данных много
        # то можно добвалять недостающие элементы
        # сохраням люей на фото
        if photo_people:
            photo.photo_people.all().delete()
            for people_data in photo_people:
                PhotoPeople.objects.create(photo=photo, **people_data)
        return photo

# 2) отображать список фотографий, без мета данных.
class PhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo']

