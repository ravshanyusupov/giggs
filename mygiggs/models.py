from django.db import models

# Create your models here.


class Car(models.Model):
     name = models.CharField(max_length=100)
     color = models.CharField(max_length=100)
     engine = models.IntegerField(blank=True, null=True)
     content = models.CharField(max_length=255)
     # photo = models.ImageField(upload_to="photo/%Y/%M/%D")
     slug = models.SlugField(unique=True, blank=True)
     type_id = models.ForeignKey('Sort', on_delete=models.CASCADE)

     def __str__(self):
         return self.name


class Sort(models.Model):
    type = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.type