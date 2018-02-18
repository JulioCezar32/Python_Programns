# a simple example of a class to enterprise employee
import requests


class Employee:

    """A simple employee class"""
    raise_amt = 1.05

    def __init__(self, first, second, pay):
        self.first = first
        self.second = second
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com.br'.format(self.first, self.second)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.second)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'htpp://company.com/{self.second}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
