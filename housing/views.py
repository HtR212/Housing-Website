from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from .models import StudentHousing


# Create your views here.
def index(request):
    return render(request, 'housing/index.html')

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'housing/index.html', 
                  { 'mapbox_access_token': mapbox_access_token })


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
