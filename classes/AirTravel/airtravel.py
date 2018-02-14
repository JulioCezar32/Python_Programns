class Flight:

    def __init__(self,number):
        if not number[:2].isalpha():
            #the first two number needs to be a letter
            raise ValueError("No Airline Code in '{}'".format(number))

        if not number[:2].isupper():
            #all airline Code must start with upper case letter
            raise ValueError("Invalid Airline Code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:])<=9999):
            raise ValueError("Invalid Route Number '{}'".format(number))

        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def __str__(self):
        return "Your Flight Number is {0}".format(self._number)


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_seats = num_rows
        self._num_seats_per_row =  num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def num_seats(self):
        return self._model * self._num_sets_per_row

    def seating_plan(self):
        return (range(1,self._num_seats_per_row + 1),"ABCDEFGHIJ"[:self._num_seats_per_row + 1])
