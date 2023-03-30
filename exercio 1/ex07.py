valor_duplicata = float(input("Digite o valor da duplicata: "))
dias_atraso = int(input("Digite o número de dias de atraso: "))

multa_dia = 0.05  # multa de 5% ao dia de atraso

# calcula o valor da multa
multa = valor_duplicata * dias_atraso * multa_dia

# calcula o valor final da duplicata
valor_final = valor_duplicata + multa

print(f"O valor final da duplicata é: R$ {valor_final:.2f}")