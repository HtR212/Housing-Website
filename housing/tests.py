from django.test import TestCase
from django.urls import reverse
from housing.models import StudentHousing
from housing.models import Review
from housing.models import SuggestedListings

# Create your tests here.
class DummyTestCase(TestCase):
    def setUp(self):
        x = 1
        y = 2
    
    def test_dummy_test_case(self):
        self.assertEqual(1, 1)

    def test_dummy_test_case_2(self):
        self.assertEqual(2, 2)

class StudentHousingTests(TestCase):
    def setUp(self):
        self.name1="Test_Housing_Name1"
        self.distToGrounds1 = 100
        self.parking1 = False
        self.minCost1 = 999
        self.maxCost1 = 4299
        self.averageRating1 = 0
        self.minCost2 = -999

    def test_create_StudentHousing(self):
        """
        Creates a StudentHousing object with the given details
        """
        return StudentHousing.objects.create(name=self.name1, distToGrounds=self.distToGrounds1, 
        parking=self.parking1, minCost=self.minCost1, maxCost=self.maxCost1, averageRating=self.averageRating1)

    def test_create_StudentHousing_Wrong_Param(self):
        """
        valid_parameters(self) should return False if the following conditions are not all true:
        self.distToGrounds > 0 and self.minCost > 0 and self.maxCost > 0 and self.averageRating >= 0 and self.averageRating <= 5
        """
        incorrect_param_object = StudentHousing(name=self.name1, distToGrounds=self.distToGrounds1, 
        parking=self.parking1, minCost=self.minCost2, maxCost=self.maxCost1, averageRating=self.averageRating1)
        self.assertIs(incorrect_param_object.valid_parameters(), False)

class StudentHousingScrollViewTests(TestCase):
    def test_no_listings(self):
        """
        If no listings exist, an appropriate message is displayed
        """
        response = self.client.get(reverse('housing:studentHousingList'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No housing options are available.")
        self.assertQuerysetEqual(response.context['studentHousing_list'], [])

    def test_wrong_params(self):
        """
        Listings with invalid parameters are not displayed
        """
        StudentHousing.objects.create(name="Incorrect Params", distToGrounds=1, 
        parking=True, minCost=-10, maxCost=-1000, averageRating=6)
        response = self.client.get(reverse('housing:studentHousingList'))
        self.assertContains(response, "No housing options are available.")
        self.assertQuerysetEqual(response.context['studentHousing_list'], [])

    def test_wrong_params2(self):
        """
        Listings with invalid parameters are not displayed
        """
        StudentHousing.objects.create(name="Incorrect Params", distToGrounds=1, 
        parking=False, minCost=10, maxCost=0, averageRating=3)
        response = self.client.get(reverse('housing:studentHousingList'))
        self.assertContains(response, "No housing options are available.")
        self.assertQuerysetEqual(response.context['studentHousing_list'], [])


# Test for Housing List Detail View
class StudentHousingDetailViewTests(TestCase):
    def setUp(self):
        self.name1="Test_Housing_Name1"
        self.distToGrounds1 = 100
        self.parking1 = False
        self.minCost1 = 999
        self.maxCost1 = 4299
        self.averageRating1 = 0
        self.minCost2 = -999

    def test_detail_view(self):
        """
        The detailed view of a listing should include the address
        """
        validListing = StudentHousing.objects.create(name=self.name1, distToGrounds=self.distToGrounds1, 
        parking=self.parking1, minCost=self.minCost1, maxCost=self.maxCost1, averageRating=self.averageRating1, address="1308 Wertland St, Charlottesville, VA 22903")
        url = reverse('housing:detail', args=(validListing.id,))
        response = self.client.get(url)
        self.assertContains(response, validListing.address)

class DisplayReviewTest(TestCase):
    def setUp(self):
        self.house = StudentHousing.objects.create(name="Test_Housing_Name1", distToGrounds=100,
                                                     parking=False, minCost=999,
                                                     maxCost=4299, averageRating=0,
                                                     address="1308 Wertland St, Charlottesville, VA 22903")
        self.rating = 5
        self.comment = "great"
        self.pub_date = "2021-11-08 12:20"

    def test_review_view(self):
        """
        Tests for correct display of a review
        """
        validReview = Review.objects.create(house=self.house, rating=self.rating, comment=self.comment, pub_date=self.pub_date)
        url = reverse('housing:detail', args=(validReview.id,))
        response = self.client.get(url)
        self.assertContains(response, validReview.rating)
        self.assertContains(response, validReview.comment)

class WrongReviewTest(TestCase):
    def setUp(self):
        self.house = StudentHousing.objects.create(name="Test_Housing_Name1", distToGrounds=100,
                                                       parking=False, minCost=999,
                                                       maxCost=4299, averageRating=0,
                                                       address="1308 Wertland St, Charlottesville, VA 22903")
        self.rating = 7
        self.comment = "great"
        self.pub_date = "2021-11-08 12:20"
    def test_wrong_params_review(self):
        """
        Reviews with invalid parameters are not displayed
        """
        invalidReview = Review.objects.create(house=self.house, rating=self.rating, comment=self.comment,
                                            pub_date=self.pub_date)
        self.assertIs(invalidReview.valid_parameters(), False)

class SuggestionSubmissionSuccess(TestCase):
    def setUp(self):
        self.listingName = "Carratt Apartments"
        self.listingAddress = "1904 Jefferson Park Avenue, Charlottesville, VA 22903"

    def test_good_suggestion(self):
        """
        Tests for successful submission of a suggestion
        """
        validsuggestion = SuggestedListings.objects.create(listingName=self.listingName, listingAddress=self.listingAddress)
        self.assertIs(validsuggestion.valid_parameters(), True)

    def test_bad_name_suggestion(self):
        """
        Tests that an invalid suggestion(one without a name or address) is not submitted
        """
        invalidsuggestion = SuggestedListings.objects.create(listingName="",
                                                           listingAddress=self.listingAddress)
        self.assertIs(invalidsuggestion.valid_parameters(), False)

    def test_bad_addr_suggestion(self):
        """
        Tests that an invalid suggestion(one without a name or address) is not submitted
        """
        invalidsuggestion = SuggestedListings.objects.create(listingName=self.listingName,
                                                           listingAddress="")
        self.assertIs(invalidsuggestion.valid_parameters(), False)

class SetCorrectLongLat(TestCase):
    def setUp(self):
        self.listingName = "Carratt Apartments"
        self.distToGrounds1 = 100
        self.parking1 = False
        self.minCost1 = 999
        self.maxCost1 = 4299
        self.averageRating1 = 0
        self.listingAddress = "1904 Jefferson Park Avenue, Charlottesville, VA 22903"

    def testLongLat(self):
        validhousing = StudentHousing.objects.create(name=self.listingName, distToGrounds=self.distToGrounds1,
        parking=self.parking1, minCost=self.minCost1, maxCost=self.maxCost1, averageRating=self.averageRating1, address=self.listingAddress)
        self.assertTrue(validhousing.lat)
        self.assertTrue(validhousing.long)