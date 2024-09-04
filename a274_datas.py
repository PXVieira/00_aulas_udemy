from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import system

system("cls")
# dta_str = "2024-09-03 19:25:41"
# data = datetime.now()
# data2 = datetime.strptime(dta_str, )
fmt_data = "%d/%m/%Y"
fmt_hora = "%H:%M:%S"
data = datetime.now()
# print(data.strftime(fmt_data), "←-→", data.strftime(fmt_hora))

valor_emprestimo = 1_000_000
data_emprestimo = datetime(day=20, month=12, year=2020)
anos_emprestimo = relativedelta(years=5)
final_emprestimo = data_emprestimo + anos_emprestimo

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < final_emprestimo:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcelas = valor_emprestimo / numero_parcelas
n = 1
print("-".center(40, "-"))
print(f"Voce pegou um emprestimo de {valor_emprestimo}")
print(
    f"Esse valor foi financiado em {anos_emprestimo.years} anos \n"
    f"Com o valor de {valor_parcelas:,.2f} por mês"
)
print("-".center(40, "-"))

for data in data_parcelas:
    print(f"{data.strftime(fmt_data)} Parcela {n:0>2}° → R$: {valor_parcelas:.2f}")
    n += 1
