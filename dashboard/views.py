from django.shortcuts import render
from .models import Traps
# Create your views here.
def home(request):
    #traps=Trap.objects
    traps = Traps.objects.all()
    print("Hi")
    print(traps)
    return render(request, 'traps/home.html', {'traps':traps})
