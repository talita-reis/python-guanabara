'''
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares
Se o valor digitado for ímpar, desconsidere-o.'''

soma = 0
num = input('Digite 6 numeros inteiros: ')
seis_num = num.split(" ")
for n in seis_num:
    n = int(n)
    par =  n % 2 == 0
    if par == True:
        soma += n
print(f'a soma dos numeros pares e igual a {soma}')
