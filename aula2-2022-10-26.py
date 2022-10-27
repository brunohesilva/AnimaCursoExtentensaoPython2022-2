nome = input ("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

print(f"Boa noite, seu nome é {nome}")

print("Sua idade informada é {}".format(idade))

dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

if idade >= 18:
  print("Voce é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("Voce é xóven ainda, xóven ainda ...")

genero = input("Informe o genero M=Masculino, F=Feminino, O=Outros")

if idade >= 18 and genero == "M":
  print("...e voce tambem precisa/precisou prestar servico militar obrigatorio")

print("vai ser ececutada de qualquer jeito")