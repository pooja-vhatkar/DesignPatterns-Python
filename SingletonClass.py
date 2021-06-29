from abc import ABCMeta, abstractmethod

class IPerson():
    __metaclass__ = ABCMeta
    @abstractmethod
    def print_data(self):
        '''to be implemented in child class'''
    

class PersonDetails(IPerson):
    __instance = None

    @staticmethod
    def get_obj():
        if PersonDetails.__instance is not None:
            PersonDetails("Default Name",0)
        return PersonDetails.__instance

    
    def __init__(self , person_name , age):
        if PersonDetails.__instance != None:
            raise Exception("Only one object can be created of Singleton class")
        else:
            self.person_name = person_name
            self.age = age
            PersonDetails.__instance = self

    @staticmethod
    def print_data():
        print(PersonDetails.__instance.person_name ,PersonDetails.__instance.age)


pr_details = PersonDetails("Pooja", 30)
pr_details.print_data()

pr_details1 = PersonDetails("Test",12)