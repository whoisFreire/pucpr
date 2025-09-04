import time
from limpar_console import limpar_console
def menuPrincipal():
  limpar_console()
  print("sistema para gestão de dados acadêmicos\n")
  print("Menu Principal\n")
  print("1 - Estudantes\n2 - Disciplinas\n3 - Professores\n4 - Turmas\n5 - Matrículas\n9 - Sair")

  selecao = int(input("\nInforme a opção desejada:  "))

  opcao = ""
  if(selecao == 1):
    opcao = "Estudantes"
  elif(selecao == 2):
    desenvolvimento()
    return menuPrincipal()
  elif(selecao == 3):
    desenvolvimento()
    return menuPrincipal()
  elif(selecao == 4):
    desenvolvimento()
    return menuPrincipal()
  elif(selecao == 5):
    desenvolvimento()
    return menuPrincipal()
  elif(selecao == 9):
    opcao = "Sair"
  else:
    limpar_console()
    input('Informe uma opção válida.\n\nDigite ENTER para continuar.')
    return menuPrincipal()
  
  return opcao

def desenvolvimento():
  limpar_console()
  print('EM DESENVOLVIMENTO')
  input('Pressione ENTER para continuar.')