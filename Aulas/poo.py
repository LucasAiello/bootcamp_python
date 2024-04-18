import functools
'''
from abc import ABC, abstractmethod


class Bicicleta:
    
    def __init__(self, cor, modelo, ano, valor):
        self.__cor = cor
        self.__modelo = modelo
        self.__ano = ano
        self.__valor = valor
        
    @property
    def cor(self):
        return self.__cor
    
    @property
    def valor(self, valor):
        self.__valor = valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @valor.deleter
    def valor(self):
        self.__valor = 0



    def Andar(self):
        print("Estou andando hihi")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    
    def __del__(self):
        pass
        
bici = Bicicleta("Cinza", "Sei la", "2020", 500)
bici.Andar()
bici.valor = 100
del bici.valor
print(bici.cor)
Bicicleta.Andar(bici)
print(bici)


class Animal:

    def __init__(self, cor, patas):
        self.cor = cor
        self.patas = patas
    
    def falar(self):
        print("Nao sei");

class Cachorro(Animal):
    def __init__(self, cor, patas, raca):
        super().__init__(cor, patas)
        self.raca = raca

    def falar(self):
        print("Miau!")

dog = Cachorro("Marrom", 4, "Bulldog")

dog.falar()
dog.cor = "Cinza"
print(dog.cor)

  
class Controle(ABC):
    @abstractmethod
    def ligar(self):
        ...

    @abstractmethod
    def desligar(self):
        ...

    @property
    @abstractmethod

    def marca(self):
        ...


class ControleTV(Controle):
    ...

c = ControleTV()
'''

def eita(nome):
    print(f"Eita! {nome}")

def lucas(funcao):
    funcao("Lucas")

lucas(eita)


def calcular(operacao):
    def soma(a,b):
        return a+b
    def subtrai(a, b):
        return a-b
    
    if operacao == "+":
        return soma
    elif operacao == "-":
        return subtrai


resultado = calcular("-")(5,5)
print(resultado)

def decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        retorno = funcao(*args, **kwargs)
        return retorno

    return envelope

@decorador
def vish(nome):
    print(f"Vish! {nome.upper()}")

#vish = decorador(vish)
vish("Lucas")
print(vish.__name__)

class Iterador:
    def __init__(self, nome: str):
        self.nome = nome
        self.cont = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            c = self.nome[self.cont]
            self.cont += 1
            return c
        except IndexError:
            raise StopIteration
        
        
for i in Iterador("Abobora"):
    print(i)