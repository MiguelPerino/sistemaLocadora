class Patient:

    def __init__(self, name, type, specialty):
        self.name = name.lower()
        self.type = type.upper()
        self.specialty = specialty.lower()
    

    def __str__(self):
        return f'Patient: {self.name} | Type: {self.type} | Specialty required: {self.specialty}'
        