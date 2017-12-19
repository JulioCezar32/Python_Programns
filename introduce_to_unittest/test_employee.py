import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupclass\n")

    @classmethod
    def tearDownClass(cls):
        print('terDownClass')

    def setUp(self):
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Julio', 'Cezar', 100000)
        print("SetUp")

    def tearDown(self):
        print("SetDown")

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com.br')
        self.assertEqual(self.emp_2.email, 'Julio.Cezar@email.com.br')

        self.emp_1.first = 'John'
        self.emp_2.second = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com.br')
        self.assertEqual(self.emp_2.email, 'Julio.Jane@email.com.br')
        print("test_email")

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Julio Cezar')

        self.emp_1.first = 'John'
        self.emp_2.second = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Julio Jane')
        print("test_fullname")

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 105000)

        print("test_apply_raise")

    def test_monthly_schedule_true(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "You answer was sent with success"

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('htpp://company.com/Schafer/May')
            self.assertEqual(schedule, 'You answer was sent with success')

    def test_monthly_schedule_false(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('htpp://company.com/Cezar/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
