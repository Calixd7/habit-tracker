from django import forms
from .models import Habit, Record

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = [
            'name',
            'target',
            'noun',
        ]

class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = [
            'habit',
            'outcome',

        ]
