from django.test import TestCase
from django.urls import reverse
from housing.models import StudentHousing
from housing.models import Review
from housing.models import SuggestedListings
from housing.models import User
from housing.models import UserReview
from housing.models import UserFavorite

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

    def test_StudentHousing_str(self):
        """
        StudentHousing toString returns object name
        """
        test_object = StudentHousing(name=self.name1, distToGrounds=self.distToGrounds1, 
        parking=self.parking1, minCost=self.minCost1, maxCost=self.maxCost1, averageRating=self.averageRating1)
        self.assertEqual(str(test_object), test_object.name)

    def test_create_StudentHousing_Right_Param(self):
        """
        valid_parameters(self) should return True if the following conditions are  all true:
        self.distToGrounds > 0 and self.minCost > 0 and self.maxCost > 0 and self.averageRating >= 0 and self.averageRating <= 5
        """
        corret_param_object = StudentHousing(name=self.name1, distToGrounds=self.distToGrounds1, 
        parking=self.parking1, minCost=self.minCost1, maxCost=self.maxCost1, averageRating=self.averageRating1)
        self.assertIs(corret_param_object.valid_parameters(), True)


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

class ReviewTest(TestCase):
    def setUp(self):
        self.house = StudentHousing.objects.create(name="Test_Housing_Name1", distToGrounds=100,
                                                       parking=False, minCost=999,
                                                       maxCost=4299, averageRating=0,
                                                       address="1308 Wertland St, Charlottesville, VA 22903")
        self.rating = 7
        self.comment = "great"
        self.pub_date = "2021-11-08 12:20"
        self.user = User.objects.create(email="projectB07@virginia.edu")

    def test_review_str(self):
        exampleReview = Review(house=self.house, rating=self.rating, comment=self.comment, pub_date=self.pub_date)
        self.assertEqual(str(exampleReview), str(exampleReview.pub_date)+' '+str(exampleReview.rating)+' '+exampleReview.comment[:10])

    def test_wrong_params_review(self):
        """
        Reviews with invalid parameters are not displayed
        """
        invalidReview = Review.objects.create(house=self.house, rating=self.rating, comment=self.comment,
                                            pub_date=self.pub_date)
        self.assertIs(invalidReview.valid_parameters(), False)

    def test_right_params_review(self):
        """
        Reviews with valid parameters are displayed
        """
        validReview = Review.objects.create(house=self.house, rating=4.5, comment=self.comment,
                                            pub_date=self.pub_date)
        self.assertIs(validReview.valid_parameters(), True)

class SuggestionSubmissionSuccess(TestCase):
    def setUp(self):
        self.listingName = "Carratt Apartments"
        self.listingAddress = "1904 Jefferson Park Avenue, Charlottesville, VA 22903"

    def test_SuggestedListing_str(self):
        """
        SuggestedListings toString returns listingName
        """
        exampleSuggestion = SuggestedListings(listingName=self.listingName, listingAddress=self.listingAddress)
        self.assertIs(str(exampleSuggestion), exampleSuggestion.listingName)

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

class LongLatTests(TestCase):
    def setUp(self):
        self.listingName = "Carratt Apartments"
        self.distToGrounds = 100
        self.parking = False
        self.minCost = 999
        self.maxCost = 4299
        self.averageRating = 0
        self.listingAddress1 = "1904 Jefferson Park Avenue, Charlottesville, VA 22903"
        self.listingAddress2 = "12345 Jefferson Park Avenue #873 Charlottesville VA"

    def testLongLatCorrect(self):
        validhousing = StudentHousing.objects.create(name=self.listingName, distToGrounds=self.distToGrounds,
        parking=self.parking, minCost=self.minCost, maxCost=self.maxCost, averageRating=self.averageRating, address=self.listingAddress1)
        self.assertEqual(validhousing.lat, 38.027074)
        self.assertEqual(validhousing.long, -78.511567)

class SuccessfulSubmissionView(TestCase):
    def test_successfulSubmission_View(self):
        """
        Making sure that appropriate message is displayed once a listing has been suggested
        """
        response = self.client.get(reverse('housing:success'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Thanks for the suggestion. We will take it into consideration and add it to our potential listing as soon as we can!")
        
class UserModelTests(TestCase):
    def setUp(self):
        self.userEmail = "projectB07@virginia.edu"
    
    def test_User_str(self):
        exampleUser = User(email=self.userEmail)
        self.assertEqual(str(exampleUser), exampleUser.email)

class UserReviewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="projectB07@virginia.edu")
        
    def test_UserReview_str(self):
        exampleUserReview = UserReview(user=self.user, review_id=1)
        self.assertEqual(str(exampleUserReview), str(exampleUserReview.review_id))

class UserFavoriteTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="projectB07@virginia.edu")

    def test_UserFavorite_str(self):
        exampleUserFavorite = UserFavorite(user=self.user, favorite_housing_id=1)
        self.assertEqual(str(exampleUserFavorite), str(exampleUserFavorite.favorite_housing_id))

### Testing Views & Integration Tests
class NotLoggedInFlow(TestCase):
    def setUp(self):
        self.name1="Test_Housing_Name1"
        self.distToGrounds1 = 100
        self.parking1 = False
        self.minCost1 = 999
        self.maxCost1 = 4299
        self.averageRating1 = 0
        self.minCost2 = -999
        self.validListing = StudentHousing.objects.create(name=self.name1, distToGrounds=self.distToGrounds1, 
        parking=self.parking1, minCost=self.minCost1, maxCost=self.maxCost1, averageRating=self.averageRating1, address="1308 Wertland St, Charlottesville, VA 22903")

    def test_NotLoggedIn_NavBar(self):
        url = reverse('housing:index')
        response = self.client.get(url)
        self.assertContains(response, "Explore!")
        self.assertContains(response, "Homepage")
        self.assertContains(response, "Browse Listings")
        self.assertContains(response, "Login")
        self.assertNotContains(response, "Logout")
        self.assertNotContains(response, "Manage comments")
        self.assertNotContains(response, "Suggest a Listing")

    def test_NotLoggedIn_Flow(self):
        url = reverse('housing:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login with Google")
        
        url = reverse('housing:studentHousingList')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.validListing.name)

        url = reverse('housing:detail', args=(self.validListing.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.validListing.distToGrounds)
        self.assertContains(response, "Please login to submit a review")