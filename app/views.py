from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"
    result = None
    common_result = None
    if request.method == "GET":
        if request.GET:
            form = CalcForm(request.GET)
            if form.is_valid():
                initial_fee = form.cleaned_data['initial_fee']
                rate = form.cleaned_data['rate']
                months_count = form.cleaned_data['months_count']
                common_result = initial_fee + initial_fee * rate
                result = common_result / months_count
        else:
            form = CalcForm()
    else:
        form = CalcForm(request.POST)

    context = {
        'form': form,
        'result': result,
        'common_result': common_result
    }

    return render(request, template, context)
