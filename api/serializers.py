from core.models import Habit, Record
from rest_framework import serializers


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    
    class Meta:
        model = Habit
        fields = [
            'pk',
            'user',
            'date',
            'name',
            'target',
            'noun',
            'public',
        ]

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record 
        fields = [
            'pk',
            'outcome', 'habit',
        ]

