class Car:
    def __init__(self):
        self.engine_on = False
    
    def start_engine(self):
        self.engine_on = True

    def drive_to(self, City):
        if self.engine_on:
            print("Едим в город {}.".format(City))
        else:
            print("машина не заведена, никуда е едем.")

car1 = Car()
car1.start_engine()
car1.drive_to("Астану")
car2 = Car()
car2.drive_to("Шымкен")