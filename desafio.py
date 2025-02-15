# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VWaajck8LqYc9T2_V4bcYSJb6PR8ZpK9
"""

"""ROOTEIRO DE RESOLUÇÃO:
passo 1: ler a api.
passo 2: criar uma função que define um numero primo.
passo 3: criei uma um pilha para inverter os números.
passo 4: definir um loop que percorre e verifica os três números.
passo 5: dentro do loop tem um if que mescla as duas condicões
		e as compara dando o retorno. """


import requests

# URL da API que retorna os dígitos de Pi
url = 'https://api.pi.delivery/v1/pi?start=0&numberOfDigits=1000'

try:
    resposta = requests.get(url)
    resposta.raise_for_status()  # Verifica se houve erros na requisição
    digitos_pi = resposta.json()['content']  # Obtém os dígitos de Pi da resposta

    # Função para verificar se um número é primo
    def numero_primo(n):
        if n <= 1:     # 0 nem 1 são número primos (primeira codição)
            return False
        for i in range(2, int(n ** 0.5) + 1): # o intervalo de tempo começa pelo 2 pq é o inicio dos números primos, depois calcula a raiz quadrada, adicição do 1 faz
            if n % i == 0:            # exemplo vamos supor que: n = 4, (4*0.5)+1 = 3, ou seja, sempre vai ser número primo
                return False             # se resto da divição de for igual a 0 significa que ele não é primo
        return True

    def reveter_numero_pilha(n):

        lista_num = list(str(n))
        pilha = []
        for digit in lista_num:
            pilha.append(digit) #adicina numero na lista

        investe_num = ''
        while pilha:
            investe_num += pilha.pop() #remove o numero

        return int(investe_num)

    # Verifica os dígitos de Pi em grupos de três
    for i in range(len(digitos_pi) - 2):
        sequencia = digitos_pi[i:i+3]
        if all(numero_primo(int(num)) for num in sequencia) and sequencia == str(reveter_numero_pilha(int(sequencia))):
            print(f'A primeira sequência de três números primos que são palíndromos é: {sequencia}')
            break
    else:
        print('Não há sequência de três números primos que são palíndromos')

except requests.exceptions.HTTPError as err:
    print('Erro ao acessar a API:', err)
except requests.exceptions.RequestException as err:
    print('Erro na requisição:', err)
except Exception as err:
    print('Erro desconhecido:', err)