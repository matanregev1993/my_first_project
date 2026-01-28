class vehicleParent():


    def price_calculator(self,price,tax):
        total_price = price * (100+tax)/100
        print (f"the total price is {total_price}")
        return total_price