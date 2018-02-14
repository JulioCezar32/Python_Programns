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

    def __str__(self):
        return "Your Flight Number is {0}".format(self._number)
