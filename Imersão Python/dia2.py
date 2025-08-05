numero = int(input("Digite um número:"))
if (numero % 5) == 0:
  print ("O número é múltiplo de 5")
else:
  print ("O número não é múltiplo de 5")


numero = int(input("Digite um número:"))
if (numero % 2)  == 0:
  print("Esse número é par")
else:
  print("Esse número é impar")


idadePessoa = int(input("Informe sua idade:"))
if (idadePessoa >= 16 and idadePessoa < 18):
  print("Você pode entrar, mas não irá poder consumir bebida alcoólica")
  print("Pulseira: azul")
elif (idadePessoa >= 18):
  print("Você pode entrar e pode consumir bebida alcoólica")
  openBar = input("Você comprou Open Bar?")
  if(openBar == "sim"):
    print("Seu ingresso é Open Bar!")
    print("Pulseira: amarela")
  elif (openBar == "não"):
    print("Seu ingresso não é Open Bar")
    print("Pulseira: Vermelha")
  else:
    print("Informe uma resposta válida!")
else:
  print ("Você não pode entrar na festa!")



for i in range(10):
  i+=1;
  print (i);


numero = int(input("Digite um número ou 0 para encerrar:"))
while numero != 0:
  print(f"O Número digitado foi: {numero}")
  numero = int(input("\nDigite outro número ou 0 para encerrar:"))
  print("\nEncerrando Programa...")