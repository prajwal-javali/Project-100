class Car():
    def __init__(self, model, color, price, seats, width, height):
        self.model = model
        self.color = color
        self.price = price
        self.seats = seats
        self.width = width
        self.height = height

    def quotation(self):
        print("Thank You for Purchasing ", self.model," car")
        print("You have selected the following specifications")
        print("The color of the car is ", self.color)
        print("The width of the car is ", self.width)
        print("The height of the car is ", self.height)
        print("The number of seat you have selected was ", self.seats)
        print("The cost of the car is ", self.price)
        print("Tax included will be $3,000")
        self.price = self.price + int(3000)
        print("Your total cost will be ", self.price)

car1 = Car("Audi", "blue", int(50000), "5", "10", "15")
car2 = Car("Porsche", "yellow", int(100000), "4", "10", "15")
car3 = Car("BMW", "white", int(70000), "4", "5", "14" )
car1.quotation()
car2.quotation()
car3.quotation()