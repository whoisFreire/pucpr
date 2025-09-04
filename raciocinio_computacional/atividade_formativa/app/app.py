from menu_principal import menuPrincipal
from menu_operacoes import menu_operacoes
from limpar_console import limpar_console

while True:
  opcaoMenuPrincipal = menuPrincipal()
  
  if(opcaoMenuPrincipal == "Sair"):
    break

  menu_operacoes(opcaoMenuPrincipal)

  
limpar_console()
print("Finalizando aplicação...")
