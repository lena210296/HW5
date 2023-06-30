from math import sqrt

from django.shortcuts import render, get_object_or_404, redirect

from triangle.forms import TriangleForm
from .models import Person
from .forms import PersonForm


def triangle_view(request):
    if request.method == 'GET':
        form = TriangleForm()
        return render(request, 'form.html', {'form': form})
    elif request.method == 'POST':
        form = TriangleForm(request.POST)

        if form.is_valid():
            cathetus1 = form.cleaned_data['cathetus1']
            cathetus2 = form.cleaned_data['cathetus2']

            if cathetus1 <= 0 or cathetus2 <= 0:
                error_message = "Cathetus values should be greater than 0."
                return render(request, 'form.html', {'form': form, 'error_message': error_message})

            hypotenuse = sqrt(cathetus1 ** 2 + cathetus2 ** 2)
            return render(request, 'result.html', {'hypotenuse': hypotenuse})

        return render(request, 'form.html', {'form': form})


def person_add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()

    return render(request, 'person_add.html', {'form': form})


def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm(instance=person)

    return render(request, 'person_edit.html', {'person': person, 'form': form})


def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons})

# Create your views here.
