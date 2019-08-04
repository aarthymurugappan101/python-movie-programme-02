class Movie:
    listofmovies = []
    def __init__(self,name,category,description,price):
        self.__name = name
        self.__category = category
        self.__description = description
        self.__price = price


    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setCategory(self,category):
        self.__category = category

    def getCategory(self):
        return self.__category

    def setDescription(self,description):
        self.__description = description

    def getDescription(self):
        return self.__description

    def setPrice(self,price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def GetPricewithGST(self):
        return round(float(self.__price)*1.07,2)
