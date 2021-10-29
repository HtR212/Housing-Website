from django.test import TestCase

# Create your tests here.
class DummyTestCase(TestCase):
    def setUp(self):
        x = 1
        y = 2
    
    def test_dummy_test_case(self):
        self.assertEqual(1, 1)

    def test_dummy_test_case_2(self):
        self.assertEqual(2, 2)

