#!/usr/bin/env python
class Vehicles:
    carname='Fer'
    color='red'
    price=60000
    def descrip(self):
	desc_string = "%s has a %s color worth %s" % (self.carname, self.color , self.price)
	return desc_string

car1 = Vehicles()
car2 = Vehicles()

car2.carname = 'Merc'
car2.color = 'silver'
car2.price = 10000
print(car1.descrip())
print(car2.descrip())
