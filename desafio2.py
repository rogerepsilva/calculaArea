#Entrada de dados
print("---------Bem vindo ao AreaCalculator-----------")
print("Vamos começar incluindo os dados do terreno")
largura = float(input("Qual é a largura do terreno? Em metros: "))
comprimento = float(input("Qual é o comprimento do terreno? Em metros:  "))
print(f"Processando...\n")
#Processamento de dados
perimetro = 2*(largura + comprimento)
area = largura * comprimento

#Saída de dados
print("- - - - -"*5)
print(f"\n\tCerto, você digitou a largura {largura:.1f} m e o comprimento {comprimento:.1f} m, realizando meus cálculos, seguem os resultados:\n\tA área total do terreno é: {area:.2f} m²\n\tO perímetro é: {perimetro:.2f} m.\n")
print("- - - - -"*5)