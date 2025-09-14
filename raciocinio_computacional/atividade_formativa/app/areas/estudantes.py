from limpar_console import limpar_console

lista_estudantes = []

def estudantes(opcao):
  limpar_console()
  if(opcao == "Inclusão"):
    inclusao()
    input('Pressione ENTER para continuar.')
  if(opcao == "Listagem"):
    listagem()
    input("pressione ENTER para continuar.")
  if(opcao == "Atualização"):
    atualizacao()
    input("pressione ENTER para continuar.")
  if(opcao == 'Exclusão'):
    exclusao()
    input("pressione ENTER para continuar.")

  return

def inclusao():
  codigo = int(input("Informe o código do estudante: ")) 
  nome = input("Informe o nome do estudante: ")
  cpf = input("Informe o CPF do estudante: ")
  estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
  lista_estudantes.append(estudante)

def listagem():
  if(len(lista_estudantes) > 0):
    print("==== Listagem ====\n")
    for estudante in lista_estudantes:
      print(estudante["nome"])
  else:
    print("Não há estudantes cadastrados")
  print("\n\n")
    
def atualizacao():
  codigo= int(input("Informe o codigo do estudante: "))
  resultado = next(((indice, estudante) for indice, estudante in enumerate(lista_estudantes) if estudante.get('codigo') == codigo), None)

  if(resultado == None):
    limpar_console()
    print("Estudante não encontrado")
    return
  indice, estudante = resultado
  limpar_console()
  nome = input("Informe o nome: ")
  cpf = input("Informe o cpf: ")
  estudante["nome"] = nome
  estudante["cpf"] = cpf
  lista_estudantes[indice] = estudante

def exclusao():
  codigo = int(input("Informe o codigo do aluno: "))
  indice = next((indice for indice, estudante in enumerate(lista_estudantes) if estudante.get('codigo') == codigo), None)
  
  if(indice == None):
    print("Estudante não encontrado")
    return
   
  lista_estudantes.pop(indice)