class PlayStation(object):
    #model = "PS4"
    #price = 99
    def __init__(self, model, price):
        "initialize properties"
        #pass
        self.model = model
        self.__price = price
    def set_price(self, price):
        self.__price = price
    def get_price(self):
        return self.__price
    def save_more(self):
            if self.amount >= self.__price:
                self.buying_message = "Yippee! You can buy your " + self.model
            elif self.amount > self.__price/2:
                self.buying_message = "You saved more than half, keep saving!"
            elif self.amount <= self.__price/2:
                self.buying_message = "You must save more, keep saving!"
model = "PS4"
price = 99
playstation1 = PlayStation(model, price)
playstation1.set_price(price)
#playstation1.amount=25
#playstation1.amount=50
playstation1.amount=100
playstation1.save_more()
print(playstation1.buying_message)