from car import Car


class Manager:

    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

    def __repr__(self):
        return 'Car Manager has {0} cars.\n these are: {1}'.format(len(self), self.cars)

    def clear(self):
        self.cars.clear()

    def add(self, car: Car):
        self.cars.append(car)
