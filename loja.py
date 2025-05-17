# Mensagem inicio
print("Bem-vindo à Loja de Açaí e Cupuaçu!")
print("Desenvolvido por Matheus Santos")

# Cardápio
print("-------------------Cardápio------------------")
print("---| Tamanho | Cupuaçu (CP) | Açaí (AC)  |---")
print("---|    P    |   R$  9.00   |  R$ 11.00  |---")
print("---|    M    |   R$ 14.00   |  R$ 16.00  |---")
print("---|    G    |   R$ 18.00   |  R$ 20.00  |---")
print("---------------------------------------------")

# Variável
total_pedido = 0

while True:
    sabor = input("Entre com o sabor desejado (CP/AC): ")
    if sabor not in ("CP", "AC"):
        print("Sabor inválido. Tente novamente.")
        continue

    tamanho = input("Entre com o tamanho desejado (P/M/G): ")
    if tamanho not in ("P", "M", "G"):
        print("Tamanho inválido. Tente novamente.")
        continue

    # Sabor e tamanho
    if sabor == "CP":
        preco = 9 if tamanho == "P" else 14 if tamanho == "M" else 18
    else:
        preco = 11 if tamanho == "P" else 16 if tamanho == "M" else 20
    # Soma total
    total_pedido += preco
    print(
        f"Você pediu um {'Cupuaçu' if sabor == 'CP' else 'Açaí'} no tamanho {tamanho}: R$ {preco:.2f}")

    if input("Deseja mais alguma coisa? (S/N): ").upper() == "N":
        break

# Total do pedido
print("\nTotal do pedido: R$", f"{total_pedido:.2f}")