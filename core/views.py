from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import PersonForm
from .models import Person


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def person_list(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()

    persons = Person.objects.order_by('position')

    context = {
        'form': form,
        'persons': persons,
    }
    return render(request, 'person_list.html', context)

      
