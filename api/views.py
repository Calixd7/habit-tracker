from core.models import Habit, Record
from api.serializers import HabitSerializer, RecordSerializer
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView)
from rest_framework.exceptions import PermissionDenied


# Create your views here.


class HabitListView(ListCreateAPIView):
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            return Habit.objects.for_user(self.request.user)

        return self.request.user.habits.all()

class RecordCreateView(CreateAPIView):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()
    def perform_create(self, serializer):
        serializer.save()

class RecordDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecordSerializer

    def get_queryset(self):
        return Record.objects.filter(habit__user=self.request.user)

