from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
	people = models.Person.objects.all()
	return render(request, 'index.html', {'people': people})
	


