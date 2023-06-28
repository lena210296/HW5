from math import sqrt

from django.shortcuts import render


def triangle_view(request):
    if request.method == 'GET':
        return render(request, 'form.html')
    elif request.method == 'POST':
        cathetus1 = request.POST.get('cathetus1')
        cathetus2 = request.POST.get('cathetus2')

        try:
            cathetus1 = float(cathetus1)
            cathetus2 = float(cathetus2)
        except ValueError:
            error_message = "Invalid cathetus values provided."
            return render(request, 'form.html', {'error_message': error_message})

        if cathetus1 <= 0 or cathetus2 <= 0:
            error_message = "Cathetus values should be greater than 0."
            return render(request, 'form.html', {'error_message': error_message})

        hypotenuse = sqrt(cathetus1 ** 2 + cathetus2 ** 2)
        return render(request, 'result.html', {'hypotenuse': hypotenuse})


# Create your views here.
