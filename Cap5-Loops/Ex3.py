# Peça a senha até o usuário acertar
senha_correta = "python123"
tentativas = 3

while tentativas > 0:
    senha = input(f"Digite a senha ({tentativas} tentativas): ")
    if senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta!")
        tentativas -= 1
else:
    print("Acesso bloqueado!")