# Translates to and from JSON any format which we cn send on Http
# Equivalent of list and dictionaries
# Serializer will deserialze combinations

from rest_framework import serializers
from .models import Language

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        # fields = ('id', 'name', 'paradigm') ModelSerializer
        fields = ('url', 'name', 'paradigm')
