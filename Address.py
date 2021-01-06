class Address:
    '''Adress Class 
    this class has two functions
    1 - City Name 
    2 - Country Name'''
    
    def __init__(self, city= 'ABC', country= 'ABC'):
        self.City = city
        self.Country = country

    @property
    def City(self):
        return self.__city_name
    @City.setter
    def City(self, city):
        if city.isalpha():
            self.__city_name = city
        else:
            raise AttributeError("Invalid city name")
        
    @property
    def Country(self):
        return self.__country_name     
    @Country.setter
    def Country(self, country):
        if country.isalpha():
            self.__country_name = country
        else:
            raise AttributeError("Invalid country name")