preçounitario = float(input('preço unitario:'))
quantidadevendida = int(input('informe a quantidade vendida:'))
percentual_de_desconto = float(input('informe o percentual de desconto:'))


subtotal = preçounitario * quantidadevendida
valordedesconto = subtotal * percentual_de_desconto/100
preco_final = subtotal - valordedesconto

print("Preço final da venda: R$ %.2f" % preco_final)

