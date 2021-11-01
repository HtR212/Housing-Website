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
        return StudentHousing.objects.filter(distToGrounds__gt=0).filter(minCost__gt=0).filter(maxCost__gt=0).filter(averageRating__gte=0).filter(averageRating__lte=5)
        # return StudentHousing.objects.all()


class DetailView(generic.DetailView):
    model = StudentHousing
    template_name = 'housing/studentHousingOption.html'

    def get_queryset(self):
        """
        Return all housing listings.
        """
        return StudentHousing.objects
