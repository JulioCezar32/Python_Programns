#program to calculate the area of a geometrical object
#

type = input("What kind of object you want evaluate the area? (0) \n")
x = 0
while type != 'cicle' and type != 'triangle' and type != 'square':
	x = x + 1
	print('invalid Type, please insert again the type desired,\n try number:  {0}, \n type choosed: {1}'.format(x,type))
	type = input("What kind of object you want evaluate the area? \n")

if type == 'cicle':
	l1 = int(input("Now write the cicle radius \n"))

elif type == 'triangle':
	l1 = int(input("Now write the base of triagle to calculate\n"))
	l2 = input("second, write the height of triangle to evaluate\n")

elif type == ' square':
	l1 = input("Agora escreva o valor da lateral da square\n")
	l2 = input("second, write the valor of base of triangle choosed\n")


class Area():

	def __init__(self,*args,**kargs):
		self.type = type
		self.l1 = l1
		if self.type != 'cicle':
			self.l2 =l2

	def identify_the_object(self):

		if self.type == 'cicle':
			self.area = self.l1*3.14**2
			return self.area

		if self.type == 'triangle':
			self.area = self.l1 * self.l2 / 2
			return self.area

		if self.type == 'square':
			self.area = self.l1 * self.l2
			return self.area

	def __str__(self):
		self.result = identify_the_object()
		return self.result

if type == 'cicle':
	results = Area(l1,type).identify_the_object()
elif type == 'triangle':
	results = Area(l1.l2,type).identify_the_object()
elif type == ' square':
	results = Area(l1,l2,type).identify_the_object()

print("o valor final é {}".format(results))