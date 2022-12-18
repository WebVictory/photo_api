from django.db import models

class Photo(models.Model):
    photo = models.ImageField(upload_to="images",)
    geo_location = models.CharField("Геолокация",max_length=100, blank=True,null=True)
    description = models.TextField("Описание", blank=True,null=True)
    created_at = models.DateTimeField("Дата", auto_now_add=True)

class PhotoPeople(models.Model):
    photo = models.ForeignKey("Photo", on_delete=models.CASCADE,related_name='photo_people')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name