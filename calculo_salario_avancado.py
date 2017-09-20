#Recupera valor digitado pelo usuário e armazena na variável
valor_hora = float(input("Digite o valor por hora: "))
#Recupera valor digitado pelo usuário e armazena na variável
numero_horas = float(input("Digite o número de horas trabalhadas: "))
#Cálculos realizados
salario_bruto = valor_hora * numero_horas
imposto_renda = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
descontos = imposto_renda + inss + sindicato
salario_liquido = salario_bruto - descontos
#Mensagens exibidas na tela
print("+ Salário Bruto : R$ ",salario_bruto)
print("- IR ( 11% ) : R$ ",imposto_renda)
print("- INSS ( 8% ) : R$ ",inss)
print("- Sindicato ( 5% ) : R$ ",sindicato)
print("= Salário Líquido : R$ ",salario_liquido)
