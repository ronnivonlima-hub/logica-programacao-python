usuario_correto = "admin"
senha_correta = "python123"

while True:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso!")
        break
    else:
        print("Usuário ou senha incorretos. Tente novamente.")