from classes.doctor import Doctor
from classes.patient import Patient
from classes.queue import Queue


if '__main__' == __name__:
    def enqueueR(list_person, specialty, pref, conv):
        indice = None
        for i, queue in enumerate(pref):
            if queue.specialty == specialty.lower():
                indice = i
                break
        
        if indice is None:
            print(f'Nenhuma fila encontrada para {specialty}')
            return

        for p in list_person:
            if p.specialty != specialty.lower():
                continue

            if p.type in ['IDOSO', 'PCD', 'GESTANTE']: 
                pref[indice].enqueue(p)
            else:
                conv[indice].enqueue(p)

        return pref, conv

    d1 = Doctor('Miguel', 'Clínico geral')
    print(d1)
    print()

    queue_pref = [
        Queue('Clínico Geral'),
        Queue('Pediatria'),
        Queue('Ortopedia'),
        Queue('Geriatria')
    ]

    queue_conv = [
        Queue('Clínico Geral'),
        Queue('Pediatria'),  
        Queue('Ortopedia'),
        Queue('Geriatria')
    ]
    
    p3 = Patient('Cleber', 'PACIENTE', 'Clínico geral')
    p1 = Patient('Joao', 'Pcd', 'Clínico geral')
    p2 = Patient('Maria', 'Gestante', 'Clínico geral')
    print(p1)
    print()



    enqueueR([p1, p2, p3], 'Clínico geral', queue_pref, queue_conv)
    print("\nFila preferencial:", queue_pref[0])
    print("Fila convencional:", queue_conv[0])

    ####SIMPLIFIED DEQUEUE
    print()
    print('Chamando')
    call = queue_pref[0].dequeue() or queue_conv[0].dequeue()
    print(call)
    call = queue_pref[0].dequeue() or queue_conv[0].dequeue()
    print(call)
    call = queue_pref[0].dequeue() or queue_conv[0].dequeue()
    print(call)
    call = queue_pref[0].dequeue() or queue_conv[0].dequeue()
    print(call)

    # for p in [p1, p2, p3]:
    #     if p.type in ['IDOSO', 'PCD', 'GESTANTE']: 
    #         if p.specialty == "Clínico geral":
    #             queue_pref[0].enqueue(p)
            
    #         queue_pref[0].enqueue(p)
    #     else:
    #         queue_conv[0].enqueue(p)

############DEQUEU################

    # for speciality_queue in queue_pref:
    #     if not speciality_queue.isEmpty():
    #         speciality_queue.dequeue()






    

