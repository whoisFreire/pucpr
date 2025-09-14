from limpar_console import limpar_console
from areas.estudantes import estudantes
import time


def menu_operacoes(opcao):
  limpar_console()

  area = opcao

  print(f"[{area}] Menu de Operações\n")
  print("1 - Incluir\n2 - Listar\n3 - Atualizar\n4 - Excluir\n9 - Voltar ao Menu Principal")

  selecao = int(input("\nInforme a opção desejada:  "))

  opcao = ""
  if(selecao == 1):
    opcao = "Inclusão"
    if(area == "Estudantes"):
      estudantes(opcao)
  elif(selecao == 2):
    opcao = "Listagem"
    if(area == "Estudantes"):
      estudantes(opcao)
  elif(selecao == 3):
    opcao = "Atualização"
    if(area == "Estudantes"):
      estudantes(opcao)
  elif(selecao == 4):
    opcao = "Exclusão"
    if(area == "Estudantes"):
      estudantes(opcao)
  elif(selecao == 9):
    opcao = "Voltar ao Menu Princial"
    return
  else:
    print("Digite uma opção válida\n")
    menu_operacoes()

  menu_operacoes(area)