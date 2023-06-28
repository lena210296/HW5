from math import sqrt

from django.shortcuts import render


def triangle_view(request):
    if request.method == 'POST':
        cathetus1 = float(request.POST.get('cathetus1'))
        cathetus2 = float(request.POST.get('cathetus2'))

        if cathetus1 <= 0 or cathetus2 <= 0:
            error_message = "Cathetus values should be greater than 0."
            return render(request, 'form.html', {'error_message': error_message})

        hypotenuse = sqrt(cathetus1 ** 2 + cathetus2 ** 2)
        return render(request, 'result.html', {'hypotenuse': hypotenuse})
    else:
        return render(request, 'form.html', {'error_message': None})

# Create your views here.
