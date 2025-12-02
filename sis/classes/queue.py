class Queue:

    def __init__(self, specialty):
        self.specialty = specialty.lower()  #para criar um objeto - fila- especifico
        self.queue = []
    
    def enqueue(self, patient):
        self.queue.append(patient)
    

    def dequeue(self):
        if not self.queue:
            return None

        return self.queue.pop(0)    
    
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        if not self.queue:
            return True
        return False
    


    def __str__(self):
        if self.queue:
            patients = '\n'.join(str(p) for p in self.queue)
            return f'{self.specialty}:\n{patients}'
        return f'\nFila está vazia'
    


        