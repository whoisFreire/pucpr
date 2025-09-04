from limpar_console import limpar_console

lista_estudantes = []

def estudantes(opcao):
  limpar_console()
  if(opcao == "Inclusão"):
    estudante = input("Informe o nome do estudante:  ")
    input('Pressione ENTER para continuar.')
    lista_estudantes.append(estudante)
  if(opcao == "Listagem"):
    if(len(lista_estudantes) > 0):
      print("==== Listagem ====\n")
      for estudante in lista_estudantes:
        print(estudante)
    else:
      print("Não há estudantes cadastrados")
    input("\n\npressione ENTER para continuar.")    
  
  return