from classes.doctor import Doctor
from classes.patient import Patient
from classes.queue import Queue
from time import sleep

if '__main__' == __name__:
    def enqueueR(patient, specialty, pref, conv):
        specialty = specialty.lower().strip()

        if specialty not in pref:
            print(f'Nenhuma fila encontrada para {specialty}')
            return
        
        if patient.type in ['IDOSO', 'PCD', 'GESTANTE']:
            pref[specialty].enqueue(patient)
        
        else:
            conv[specialty].enqueue(patient)

    
    doctors = []
    def register_doctor():
        print("\n=== Cadastro de Médico ===")
        while True:
            name = input('\nDigite o nome do médico: ').strip()
            specialty = input('Informe a especialidade: ').strip()

            exists = any(d.name.lower() == name.lower() and d.specialty.lower() == specialty.lower() for d in doctors)  #return true se tiver, false se nao
            if exists:
                print('Esse médico ja está cadastrado.')
                continue

            doctor = Doctor(name, specialty)
            doctors.append(doctor)
            print(f'Médico {name} | {specialty} cadastrado com sucesso!')

            again = input('\nDeseja cadastrar outro médico? (s/n): ').lower()
            if again not in ['sim', 's']:
                break
    print()

    queue_pref = {
        "clínico geral": Queue('Clínico Geral'),
        "pediatria": Queue('Pediatria'),
        "ortopedia": Queue('Ortopedia'),
        "geriatria": Queue('Geriatria')
    }

    queue_conv = {
        "clínico geral": Queue('Clínico geral'),
        "pediatria": Queue('Pediatria'),  
        "ortopedia": Queue('Ortopedia'),
        "geriatria": Queue('Geriatria')
    }

    print()
    patients = []
    def register_patient():
        while True:
            #verificar specialty
            name = input('Digite o nome do paciente: ')
            p_type = input('Digite seu tipo [Idoso, PCD, Gestante, Paciente]: ')
            specialty = input('Informe a especialidade desejada: ')

            exists = any(p.name == name.lower() and p.type == p_type.upper() and p.specialty == specialty.lower() for p in patients)
            if exists:
                print('Paciente já cadastrado.')
                continue

            patient = Patient(name, p_type, specialty)
            patients.append(patient)
            print(f'Paciente {name} cadastrado com sucesso!')

            #se eu so passar specialty aqui
            # enqueueR(patient, queue_conv[patient.specialty], queue_pref[patient.specialty])
            enqueueR(patient, specialty, queue_pref, queue_conv)
            again = input('\nDeseja cadastrar outro paciente? (s/n): ').lower()
            if again not in ['sim', 's']:
                break

    def callPatient(pref, conv):
        op_specialty = input('Informe a especialidade para chamar o próx paciente: ').lower().strip()

        if op_specialty not in pref:
            print('Não tem fila para esta especialidade.')
            return

        if not pref[op_specialty].isEmpty():
            return pref[op_specialty].dequeue()
        
        elif not conv[op_specialty].isEmpty():
            return conv[op_specialty].dequeue()

        print('Nenhum paciente na fila dessa especialidade.')
        return


    def changeDoctor(all_doctors):  #printar o nome dos médicos antes de perguntar qual deseja alterar
        print()
        for d in all_doctors:
            print(d)

        found = False
        name_to_change = input('\nInforme o nome do médico que deseja alterar: ')
        for doctor in all_doctors:
            if doctor.name == name_to_change:
                change = input('\nO que deseja alterar? (nome/especialidade): ').lower().strip()
                if change == 'nome':
                    name = input('Informe o novo nome: ')
                    doctor.name = name
                    print('\nNome alterado com sucesso')

                elif change == 'especialidade':
                    specialty = input('Informe a nova especialidade: ')
                    doctor.specialty = specialty
                    print('\nEspecialidade alterada com sucesso')
                
                else:
                    print('Para alterar, tem que ser apenas Nome e Especialidade.')
                    return
                
                found = True
                break
            
        if not found:
            print('\nDoutor com este nome não foi encontrado.')
            return


    def removeDoctor(all_doctors):
        to_change = input('Informe o nome do médico que deseja remover: ').lower()
        found = False
        for doctor in all_doctors:
            if to_change == doctor.name:
                all_doctors.remove(doctor)
                print(f'Doutor {to_change} removido com sucesso')
                found = True
                return
            
        if not found:
            print('Médico não encontrado.')
            return
        
    print()
    def showMenu():
        print()
        print('Menu Principal')
        print('1- Gerenciar médico') 
        print('2- Pegar senha')
        print('3- Ver médicos disponíveis')
        print('4- Ver fila preferencial')
        print('5- Ver fila convencional')
        print('6- Chamar paciente para ser atendido')  
        print('0- Sair')

    while True:
        showMenu()
        option = int(input('Digite a opção desejada: '))

        match option:
            case 1:
                print()
                print('Menu Doutor')
                print('1 - Registrar médico')
                print('2 - Alterar médico')
                print('3 - Excluir registro')
                op = int(input('Informe a opção desejada: '))
                if op == 1:
                    register_doctor()
                elif op == 2:
                    changeDoctor(doctors)                    
                elif op == 3:
                    removeDoctor(doctors)                    
                
            case 2:
                register_patient()
            case 3:
                print()
                print('Médicos cadastrados: ')
                for d in doctors:
                    print(d)
                input('\nPressione Enter para voltar ao Menu Principal')
                sleep(1)
            case 4:
                print()
                
                print('Fila preferencial: ')
                for k, q in queue_pref.items():
                    if not q.isEmpty():
                        print(q)

                input('\nPressione Enter para voltar ao Menu Principal')
                sleep(1)                        
            case 5:
                print()
                print('Fila convencional: ')
                for k, q in queue_conv.items():
                    if not q.isEmpty():
                        print(q)

                input('\nPressione Enter para voltar ao Menu Principal')
                sleep(1)                        
            
            case 6:
                print(callPatient(queue_pref, queue_conv))
            
            case 0:
                print()
                print('Saindo do sistema...')
                sleep(0.5)
                break