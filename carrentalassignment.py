import datetime

class RentalCar:
    def __init__(self, cat, dayrental, kmprice):
        self.category = cat
        self.dayrental = dayrental
        self.kmprice = kmprice
        self.is_rented = False
        self.booking_number = None
        self.customer_name = None
        self.start_time = None
        self.mileage = None

    def calculate_rental_price(self, dn, kdrv):
        if self.category == 'Compact':
            return self.dayrental * dn
        elif self.category == 'Premium':
            return self.dayrental * dn * 1.2 + self.kmprice * kdrv
        elif self.category == 'Minivan':
            return self.dayrental * dn * 1.7 + (self.kmprice * kdrv * 1.5)
        else:
            return None

    def rent_car(self, bkno, cname, stime, mileage):
        if not self.is_rented:
            self.booking_number = bkno
            self.customer_name = cname
            self.rental_start_time = stime
            self.mileage = mileage
            self.is_rented = True
            return "Car rented successfully!"
        else:
            return "Car is already rented."
    def get_car_details(self):
        print('-------------------------------------')
        print('booking_number',self.booking_number)
        print('customer_name',self.customer_name)
        print('rental_start_time',self.rental_start_time)
        print('mileage',self.mileage)


    def return_car(self, return_time, current_mileage):
        if self.is_rented:
            rental_duration = (return_time - self.rental_start_time).days
            km_driven = current_mileage - self.mileage
            rental_price = self.calculate_rental_price(rental_duration, km_driven)
            self.is_rented = False
            self.booking_number = None
            self.customer_name = None
            self.rental_start_time = None
            self.car_mileage_at_pickup = None
            return f"Rental Price: ${rental_price:.2f}"
        else:
            return "Car is not rented."


# I have created rental car instances for each category
compact_car = RentalCar('Compact', 30, 0.15)
premium_car = RentalCar('Premium', 40, 0.20)
minivan_car = RentalCar('Minivan', 50, 0.25)

    # U1. Rental registration
booking_number = 77777
customer_name = "Mayur Bhavsar"
stime = datetime.datetime(2023, 7, 26)
mileage = 50000
response = compact_car.rent_car(booking_number, customer_name, stime, mileage)
print(response)
print('Fetching Car details.....')
compact_car.get_car_details()




    # U2. Car Return
return_time = datetime.datetime(2023, 7, 28)
current_mileage = 50450
price_response = compact_car.return_car(return_time, current_mileage)
print(price_response)


