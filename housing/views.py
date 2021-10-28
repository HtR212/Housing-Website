from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from .models import StudentHousing


# Create your views here.
def index(request):
    return render(request, 'housing/index.html')

class HousingListView(generic.ListView):
    template_name = 'housing/studentHousingList.html'
    context_object_name = 'studentHousing_list'

    def get_queryset(self):
        """
        Return all housing listings.
        """
        return StudentHousing.objects.all()
