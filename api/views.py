from core.models import Habit, Record
from api.serializers import HabitSerializer, RecordSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView


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

