from django.shortcuts import render
from .models import Car
from .forms import NameForm
from django.http.response import HttpResponseRedirect
# Create your views here.
def index(request):
    ctx = {
            "car" : Car.objects.get(pk=1)
        }
    return render(request,"index.html",ctx)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})