from classes.Car import Cars

class Rent:
    def __init__(self, id, client, car, days):
        self.id = id
        self.client = client
        self.car = car
        self.days = days
        self.active = True


    def finish(self):
        self.active = False
        self.car.return_car()

    def __str__(self):
        return f"Aluguel: {self.id} | Carro: {self.car.model} | Cliente: {self.client.name} | Ativo: {self.active}"
    
