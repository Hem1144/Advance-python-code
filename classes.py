# Class is a blueprint for your objects.
# First letter of class should be capital
# It can contain Attributes(variables defined inside the class) and Methods(functions defined inside the class).


class Remover:
    a = 10

    def __init__(self, my_list):
        self.my_list = my_list

    def duplicates_remover(self):
        unique_data = []
        seen = []

        for item in self.my_list:
            if item not in seen:
                unique_data.append(item)
                seen.append(item)

        return unique_data

    def __str__(self):
        return "I am initialized inside the class Remover"


obj1 = Remover([10, "apple", 10, "banana", "apple", 20.5, 20.5])
obj2 = Remover([1, 2, 2, 3, 4, 4, 5])
# print(obj.duplicates_remover())
# print(Remover([1, 2, 2, 3, 4, 4, 5]).duplicates_remover())
print(obj1.duplicates_remover())
print(obj2.duplicates_remover())


