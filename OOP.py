class Shopping_List:
    def __init__(self, foodname, amount):
        self.foodname = foodname
        self.amount = amount
        self.price = 0
        self.totalprice = 0

    def get_price(self):
        return self.price

    def nett_price(self, amnt):
        self.price = amnt

    def price_list(self):
        if self.foodname == "Dry Cured Iberian Ham" :
            self.nett_price(177.80)

        elif self.foodname == "Wagyu Steaks" :
            self.nett_price(450.00)

        elif self.foodname == "Matsutake Mushrooms" :
            self.nett_price(272.00)

        elif self.foodname == "Kopi Luwak Coffee" :
            self.nett_price(306.50)

        elif self.foodname == "Moose Cheese" :
            self.nett_price(487.20)

        elif self.foodname == "White Truffles" :
            self.nett_price(3600.00)

        elif self.foodname == "Blue Fin Tuna" :
            self.nett_price(3603.00)

        elif self.foodname == "Le Bonnotte Potatoes" :
            self.nett_price(270.81)

    def food_cost(self):
        self.price_list()
        self.totalprice = self.price * self.amount
        return self.totalprice