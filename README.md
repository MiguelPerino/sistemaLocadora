# 🚗 Sistema de Locadora de Veículos

Um sistema de gerenciamento de aluguel de carros desenvolvido em **Python**, utilizando conceitos de **Programação Orientada a Objetos (POO)**. O projeto permite o cadastro de veículos, clientes e o registro detalhado de locações com controle de disponibilidade.

---

## 🛠️ Funcionalidades

O sistema oferece um menu interativo com as seguintes opções:

* **Cadastrar Carro:** Registra veículos informando código, modelo, ano e status inicial de disponibilidade.
* **Cadastrar Cliente:** Registra clientes com nome, código único e CNH.
* **Registrar Aluguel:** Vincula um cliente a um veículo disponível, calculando automaticamente a data prevista para devolução.
* **Gestão de Frota:** Visualização de carros disponíveis e indisponíveis.
* **Histórico:** Consulta de aluguéis ativos e realizados.

---

## 🏗️ Estrutura do Projeto

O código está organizado em classes para facilitar a manutenção e escalabilidade:


* **`Cars`**: Gerencia os atributos do veículo e o método de locação/devolução.
* **`Client`**: Armazena as informações básicas do locatário.
* **`Rent`**: Controla o contrato de locação, ligando o cliente ao carro e definindo o período de uso.
* **`main.py`**: Ponto de entrada do sistema com a lógica do menu e validações.

---

## 🚀 Como Executar

### Pré-requisitos
* Python 3.x instalado.

### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
2. Navegue até a pasta do projeto:
   ```bash
   cd nome-do-repositorio

3. Execute o programa:
   ```bash
   python main.py

### 📝 Regras de Negócio e Validações
Validação de Ano: O sistema não permite cadastrar carros com ano superior ao atual.

Unicidade de Código: O sistema valida se um código de cliente já foi utilizado para evitar duplicidade.

Controle de Disponibilidade: Um carro só pode ser alugado se o seu atributo available for True. Ao alugar, o status muda automaticamente.

Cálculo de Datas: Utiliza a biblioteca datetime para projetar a entrega baseada nos dias de locação informados.

### 🛠️ Tecnologias Utilizadas
Python - Linguagem principal.

DateTime - Manipulação de datas e prazos.

###  Quem fez:
Miguel Costa Perino - MiguelPerino

✨ Este projeto foi desenvolvido para fins de estudo de Programação Orientada a Objetos.
