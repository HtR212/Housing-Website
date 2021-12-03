from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404
from .models import StudentHousing, Review, UserReview, UserFavorite, User, SuggestedListings
from django.urls import reverse
from django.utils import timezone
from django.db.models import Avg


# Create your views here.
def index(request):
    context = {'studentHousingList': StudentHousing.objects.filter(distToGrounds__gt=0).filter(minCost__gt=0).filter(maxCost__gt=0)\
            .filter(averageRating__gte=0).filter(averageRating__lte=5)}
    if request.user.is_authenticated:
        try:
            u = User.objects.get(email=request.user.email)
            u.userName = request.user.username
            u.save()
        except User.DoesNotExist:
            User.objects.create(email=request.user.email, userName=request.user.username)
    return render(request, 'housing/index.html', context)


class HousingListView(generic.ListView):
    template_name = 'housing/studentHousingList.html'
    context_object_name = 'studentHousing_list'

    def get_queryset(self):
        """
        Return all housing listings.
        """
        return StudentHousing.objects.filter(distToGrounds__gt=0).filter(minCost__gt=0).filter(maxCost__gt=0)\
            .filter(averageRating__gte=0).filter(averageRating__lte=5)


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
        selected_choice = int(request.POST['rating'])
        if selected_choice is None:
            raise ValueError()
    except (KeyError, ValueError):
        return render(request, 'housing/studentHousingOption.html', {
            'studenthousing': housing,
            'error_message': "You didn't select a rating.",
        })
    else:
        r = housing.review_set.create(rating=selected_choice, comment=request.POST['comment'], pub_date=timezone.now())
        housing.averageRating = round(housing.review_set.aggregate(Avg('rating'))['rating__avg'], 1)
        housing.save()
        User.objects.get(email=request.user.email).userreview_set.create(review_id=r.id)
        return HttpResponseRedirect(reverse('housing:detail', args=(housing_id,)))


def user_review_list(request):
    review_list = Review.objects.filter(id__in=User.objects.get(email=request.user.email).userreview_set.values_list('review_id', flat=True))
    context = {'review_list': review_list}
    return render(request, 'housing/userReviewList.html', context)


class SuggestionView(generic.CreateView):
    model = SuggestedListings
    template_name = "housing/submission.html"
    fields = ['Name', 'Address']
    success_url = 'success/'


def successful_submission_view(request):
    return render(request, 'housing/successfulSubmission.html')


def profile_view(request):
    context = {'currentuser': User.objects.get(email=request.user.email)}
    return render(request, 'housing/profile.html', context)


def edit_profile_view(request):
    context = {'currentuser': User.objects.get(email=request.user.email)}
    return render(request, 'housing/profileEdit.html', context)


def submit_profile_view(request):
    u = User.objects.get(email=request.user.email)
    # school_year_choices = {'FR': "Freshman", 'SO': "Sophomore", 'JR': "Junior", 'SR': "Senior", 'GR': "Graduate", 'OT': "Other"}
    try:
        gender = (request.POST['gender'])
        age = int(request.POST['age'])
        school_year = request.POST['schoolYear']
        major = (request.POST['major'])
    except KeyError:
        return render(request, 'housing/profileEdit.html', {
            'currentuser': u,
            'error_message': "Unknown error",
        })
    else:
        u.gender = gender
        u.age = age
        u.schoolYear = school_year
        u.major = major
        u.save()
        return HttpResponseRedirect(reverse('housing:profile'))
