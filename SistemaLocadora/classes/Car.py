class Cars:
    def __init__(self, code, model, year, available=True):
        self.code = code
        self.model = model
        self.year = year
        self.available = available

    def rent(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_car(self):
        self.available = True

    def __str__(self):
        return f" Code: {self.code} | Carro: {self.model} | Ano: {self.year} | Disponibilidade: {self.available} "