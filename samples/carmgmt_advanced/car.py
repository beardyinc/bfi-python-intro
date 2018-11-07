class Car:
    equipment = []

    def __init__(self, pwr: int, make: str, model: str, year: int = 2018):
        self.power = pwr
        self.make = make
        self.model = model
        self.year = year

    def drive(self, destination: str):
        print('driving to ' + destination)

    def start(self):
        print('vrouuuumm!')

    def add_equipment(self, eqipment):
        self.equipment.append(eqipment)

    def __repr__(self):
        return '{0} {1} ({2}) has {3} hp'.format(self.make, self.model, self.year, self.power)
