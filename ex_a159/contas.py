import abc


class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo=0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor): ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f"(DEPÓSITO R$: {valor:.2f})")

    def detalhes(self, msg=""):
        print(f"Seu saldo é R$: {self.saldo:.2f} {msg}")


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.detalhes(f"(SAQUE R$: {valor:.2f})")
            return self.saldo

        print("Não foi possível sacar o valor desejado!")
        self.detalhes(f"(SAQUE NEGADO R$: {valor:.2f})")


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f"(SAQUE R$: {valor:.2f})")
            return self.saldo

        print("Não foi possível sacar o valor desejado!")
        print(f"Seu limite é R$: {-self.limite:.2f}")
        self.detalhes(f"(SAQUE NEGADO R$: {valor:.2f})")


if __name__ == "__main__":
    print("-" * 50)
    print(f'{"CONTA POUPANÇA":^50}')
    print("-" * 50)
    cc1 = ContaPoupanca(111, 222, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(100)
    cc1.sacar(1)
    print("-" * 50)
    print(f'{"CONTA CORRENTE":^50}')
    print("-" * 50)
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(100)
    cc1.sacar(1)
    print("-" * 50)
