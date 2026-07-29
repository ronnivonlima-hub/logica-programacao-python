idade = int(input("Idade: "))
possui_documento = input("Possui documento? (s/n): ")

if idade >= 18 and possui_documento.lower() == "s":
    print("Entrada autorizada.")
else:
    print("Entrada negada.")