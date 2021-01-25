from django.shortcuts import render, get_object_or_404, redirect
from .models import Habit, Record
from .forms import HabitForm, RecordForm
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required
   


# @login_required
def habit_list(request):
    habits = Habit.objects.all()
    return render(request, "core/habit_list.html", {"habits": habits})

# @login_required
def habit_detail(request, pk):
    habit = get_object_or_404 (habits, pk=pk)

    return render(request, "habits/habit_detail.html", {"habit": habit})

# @login_required
def habit_create(request):
    if request.method == "GET":
        form = HabitForm()

    else:
        form = HabitForm(data=request.POST)

        if form.is_valid():
            habit = form.save(commit=False)
            

            form.save()

            success(request, "Your Habit was created!")
            return redirect(to='habit_list')

    return render(request, "core/habit_create.html", {"form": form})

# @login_required
def habit_update(request, pk):
    habit = get_object_or_404(habits, pk=pk)

    if request.method == 'GET':
        form = HabitForm(instance=habit)

    else:
        form = HabitForm(data=request.POST, instance=habit)

        if form.is_valid():
            form.save()
            success(request, 'Your habits has been updated!')
            return redirect(to='habit_list')

    return render(request, 'core/habit_update.html', {'form': form})

# @login_required
def habit_delete(request, pk):
    if request.method == 'GET':
        return render(request, 'core/habit_delete.html')

    else:
        habit = get_object_or_404(habits.all(), pk=pk)
        habit.delete()
        success(request, 'Your Habit has been deleted!')
        return redirect(to='habit_list')

# @login_required
def record_create(request, habit_pk):
    habit = get_object_or_404(habits, pk=habit_pk)

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

# @login_required   
def record_update(request, record_pk):
    record = get_object_or_404(Record.objects.filter(), pk=record_pk)
    if request.method == "GET":
        form = RecordForm(instance=record)
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = record.save()
            return redirect("record_detail", pk=record.pk)
    return render(request, "core/record_create.html", {"record": record, "form": form})

# @login_required
def record_delete(request, record_pk):
    record = get_object_or_404(Record.objects.filter(), pk=record_pk)
    record.delete()

    return redirect(to="habit_detail", pk = record.habit )
