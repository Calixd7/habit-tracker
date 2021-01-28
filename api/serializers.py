from core.models import Habit, Record
from rest_framework import serializers


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    
    class Meta:
        model = Habit
        fields = [
            'user',
            'title',
            'name',
            'targe',
            'noun',
        ]

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record 
        fields = [
            'outcome', 'habit',
        ]