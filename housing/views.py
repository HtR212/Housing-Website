from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404
from .models import StudentHousing
from django.urls import reverse
from django.utils import timezone


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
        return StudentHousing.objects.filter(distToGrounds__gt=0).filter(minCost__gt=0).filter(maxCost__gt=0)\
            .filter(averageRating__gte=0).filter(averageRating__lte=5)
        # return StudentHousing.objects.all()


class DetailView(generic.DetailView):
    model = StudentHousing
    template_name = 'housing/studentHousingOption.html'

    def get_queryset(self):
        """
        Return all housing listings.
        """
        return StudentHousing.objects


def review_submit(request, housing_id):
    housing = get_object_or_404(StudentHousing, pk=housing_id)
    try:
        selected_choice = request.POST['rating']
    except KeyError:
        return render(request, 'housing/studentHousingOption.html', {
            'studentHousing': housing,
            'error_message': "You didn't select a rating.",
        })
    else:
        housing.review_set.create(rating=int(selected_choice), review=request.POST['review'], pub_date=timezone.now())
        return HttpResponseRedirect(reverse('housing:detail', args=(housing_id,)))
