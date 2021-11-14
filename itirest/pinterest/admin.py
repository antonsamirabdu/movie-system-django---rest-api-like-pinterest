from django.contrib import admin
from .models import Movie, Categories , Casts


admin.site.register(Movie)
admin.site.register(Casts)
admin.site.register(Categories)
# Register your models here.
