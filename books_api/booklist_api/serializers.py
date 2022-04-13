from rest_framework import serializers
from .models import Book


# serializers.ModelSerializer just tells django to convert sql to JSON
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # tell django which model to use
        # tell django which fields to include
        fields = ('id', 'title', 'author', 'year', 'description',)
