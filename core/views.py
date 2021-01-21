from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit, Record
from .forms import HabitForm, RecordForm

@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, "core/habit_list.html", {"habits": habits})

@login_required
def habit_detail(request, pk):
    habit = get_object_or_404(request.user.habits, pk=pk)
    records = Record.objects.filter(habit=habit.id)
    return render(request, "core/habit_detail.html", {"habit": habit, "records": records})

@login_required
def habit_create(request):
    if request.method == "GET":
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            form.save()
            return redirect("habit_detail", pk=habit.pk)
    return render(request, "core/habit_create.html", {"form": form})

@login_required
def habit_update(request, pk):
    habit = get_object_or_404(request.user.habits, pk=pk)

    if request.method == "GET":
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect("habit_detail", pk=habit.pk)
    return render(request, "core/habit_update.html", {"habit": habit, "form": form})

@login_required
def habit_delete(request, pk):
    habit = get_object_or_404(request.user.habits.all(), pk=pk)
    habit.delete()

    return redirect(to="habit_list")

@login_required
def record_create(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)

    if request.method == "GET":
        form = RecordForm()
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            habit_pk = habit.pk
            record.habit = habit_pk
            record.save()
            return redirect("habit_detail", pk=habit_pk)
    return render(request, "core/record_create.html", {"form": form})

@login_required   
def record_update(request, record_pk):
    record = get_object_or_404(Record.objects.filter(habit__user=request.user), pk=record_pk)
    if request.method == "GET":
        form = RecordForm(instance=record)
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = record.save()
            return redirect("record_detail", pk=record.pk)
    return render(request, "core/record_create.html", {"record": record, "form": form})

@login_required
def record_delete(request, record_pk):
    record = get_object_or_404(Record.objects.filter(habit__user=request.user), pk=record_pk)
    record.delete()

    return redirect(to="habit_detail", pk = record.habit )