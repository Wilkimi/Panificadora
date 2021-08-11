import os

#### MENU ####
while (True): #loop infinito
###print imprime na tela o menu
  print('1 - Nova Venda')
  print('2 - Gerar Relatório')
  print('3 -  Sobre')
  print('4 - Sair')

  #variável, pegar a opção do usuário
  opcao = input('Digite a opção desejada:')
    
  #verificar qual opção o usuário esccolheu "If"
  if (opcao == '1'):
    os.system('clear') #limpa a tela 
    print('Nova venda')
    sal_qt = int(input('Digite a quantidade de pães de Sal:'))
    leite_qt = int(input('Digite a quantidade de pães de leite:'))
    milho_qt = int(input('Digite a quantidade de pães de milho:'))
    total = sal_qt + leite_qt + milho_qt
    print('Total de pães: %.0f deu R$%.2f' % (total, total*0.25))

    input('\n\nPressione ENTER para continuar:')
    os.system('clear')
  elif(opcao == '2'):
    print('Relatório')
  elif(opcao == '3'):
    print('Sobre')
  elif(opcao == '4'):
    print('Sair')
    break #INTERROMPE A EXECUÇÃO DO LOOP
  else:
    print('Opção Ivalida, tente Novamente')

print('Programa Finalizado')
