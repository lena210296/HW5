from math import sqrt

from django.shortcuts import render

from triangle.forms import TriangleForm


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


# Create your views here.
