from rest_framework import serializers
from ...models import Movie


class MovieSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True, read_only=True)
    casts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('title', 'description', 'categories', 'release_date', 'casts', 'poster',)
