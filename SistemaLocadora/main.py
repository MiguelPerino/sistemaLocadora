from classes.Car import Cars
from classes.Client import Client
from classes.Rent import Rent
import datetime
 

def showMenu():
    print("\n===== MENU PRINCIPAL =====")
    print('1 - Cadastrar carro')
    print('2 - Cadastrar cliente')
    print('3 - Registrar aluguel')
    print('4 - Ver carros disponíveis')
    print('5 - Ver carros indisponíveis')
    print('6 - Ver alugueis')
    print('7 - Sair do programa')
    print("==========================\n")


current_year = datetime.datetime.now().year
all_cars = []
def registerCar():

    while True:
        
        while True:
            try:
                code = int(input('Informe o código do carro: '))
                break
            except ValueError:
                print('')

        model = input('Digite o modelo do carro: ')

        while True:
            try:
                year = int(input('Informe o ano do carro: '))
                if year > current_year:
                    raise ValueError
                break
            except ValueError:
                print('Ano está errado, tem que ser um válido')
        
        available = input('Está disponível? (s/n): ').lower()
        if available in ['sim', 's', 'si']:
            available = True
        else:
            available = False

        car = Cars(code, model, year, available)
        all_cars.append(car)
        #deseja adicionar outro

        add_another = input('Deseja adicionar outro carro? (s/n): ').lower()
        if add_another not in ['sim', 's']:
            print('Voltando para o menu principal!')
            break

all_clients = []    
def registerClient():
    codes = set()
    while True:

        while True:
            try:
                code = int(input('Informe o código do cliente: '))
                if code in codes:
                    for c in all_clients:
                        if c.code == code:
                            print(f'Código já cadastrado em outro cliente, cujo qual chama: {c.name}')
                break

            except ValueError:
                print('Entrada para código inválida.')
        
        codes.add(code)

        name = input('Digite o nome do cliente: ')

        while True:
            try:
                cnh = int(input('Informe a cnh do cliente: '))
                break
            except ValueError:
                print('Entrada para CNH inválida.')

        client = Client(code, name, cnh)
        all_clients.append(client)

        again = input('Deseja adicionar outro cliente? (s/n): ')
        if again not in ['sim', 's', 'si']:
            print('Voltando para o Menu Principal.')
            break

def generateID():
    return len(all_rents) + 1

all_rents = []
def registerRent(clients, cars):
    if not clients:
        print('Nenhum cliente registrado, não é possível fazer o registro de aluguel.')
        return
    
    if not cars:
        print('Nenhum carro registrado, não é possível fazer o registro de aluguel.')
        return
    
    id_rent = generateID()

    print('\n=== CLIENTES ===')    
    for c in all_clients:
        print(f'Nome: {c.name} | Code: {c.code}')

    while True:
        try:
            code = int(input('Informe o código do cliente: '))
            break
        except ValueError:
            print('Entrada inválida para código do cliente.')
        
    client = None
    for c in all_clients:
        if c.code == code:
            client =  c
            break
    
    if not client:
        print('\nCliente não encontrado no sistema.')
        return

    availables_cars = [car for car in all_cars if car.available]
    if not availables_cars:
        print('\nNenhum carro disponível.')
        return
    
    print('\n=== CARROS DISPONÍVEIS ===')
    for c in availables_cars:
        print(c)

    while True:
        try:
            car_code = int(input('\nInforme o código do carro: '))
            break
        except ValueError:
            print('\nEntrada inválida para código do carro.')
    
    selected_car = None
    for c in availables_cars:
        if c.code == car_code:
            selected_car = c
            break
    
    if not selected_car:
        print('\nNenhum carro encontrado com este código\n')
        return

    start = datetime.date.today()

    while True:
        try:
            days = int(input('Informe a quantidade de dias que deseja alugar: '))
            if days <= 0:
                raise ValueError
            break
        except ValueError:
            print('Entrada inválida para dias alugados.')  

    if not selected_car.rent():
        print('Carro indisponível.')
        return

    rent = Rent(id_rent, client, selected_car, days)
    all_rents.append(rent)
    #Ver questao dos dias, informar pro usuario ate que dia tem que devolver 

    return_date = start + datetime.timedelta(days=days) 

    print(f'\nAluguel registrado com sucesso!')
    print(f'Data de início: {start}')
    print(f'Data de devolução: {return_date}')

if __name__ == '__main__':
    while True:
        showMenu()
        while True:    
            try:
                op = int(input('Informe a opção desejada: '))
                if op < 1 or op > 7:
                    raise ValueError
                break
            except ValueError:
                print('\nApenas números que estão de acordo com o menu referente (de 1 a 7).\n')

        if op == 1:
            registerCar()
        elif op == 2:
            registerClient()
        elif op == 3:
            registerRent(all_clients, all_cars)
        elif op == 4:
            ...
        elif op == 5:
            ...
        elif op == 6:
            ...
        elif op == 7: 
            print('\nSaindo do programa, até mais...')
            break