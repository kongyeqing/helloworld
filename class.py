class People:

    def __init__(self, name, gender, age, race):
        super().__init__()
        self.name = name
        self.gender = gender
        self.age = age
        self.race = race

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

peter = People('Peter', 'M', '24', 'Asian')
may = People('May', 'F', '23', 'White')
peter.set_name('James Peter')
print(peter.get_name())

