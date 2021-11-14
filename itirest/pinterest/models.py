from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering=('name',)


class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering=('name',)


class Casts(models.Model):
    first_name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255, null=True)
    profile_image = models.ImageField(upload_to='pinterest/actor/images')

    def __str__(self):
        return self.first_name


class CommonInfo(models.Model):

    title = models.CharField("Movie Name", max_length=255, unique=True)

    description = models.TextField()

    release_date = models.DateField(null=True, blank=True)

    categories = models.ManyToManyField('Categories')

    casts = models.ManyToManyField('Casts')

    poster = models.ImageField(upload_to='pinterest/images', null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Movie(CommonInfo):
    pass




class Series(CommonInfo):
    season = models.CharField(max_length=255)
    episode = models.CharField(max_length=255)




