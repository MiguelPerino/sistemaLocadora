class Doctor:

    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty.lower()
    
    def __str__(self):
        return f'Doctor {self.name} | {self.specialty}'
        