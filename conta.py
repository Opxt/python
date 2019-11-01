class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self,valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_saque

    def saca(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor de {} passou do seu limite!".format(valor))

    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigo_bancos():
        return {"BB":"001","Caixa":"104","Bradesco":"234"}

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
