# menu_principal.py
import os
import subprocess
import sys


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    limpar_tela()
    print("\n" + "=" * 42)
    print(" " * 12 + "SCRIPT GENERATION")
    print("=" * 42 + "\n")
    print("1) Adoção ONT")
    print("2) Native VLAN")
    print("3) Service Port")
    print("4) Remoção")
    print("5) Sair\n")
    print("=" * 42 + "\n")

def executar_script(script_nome):
    try:
        if not os.path.exists(script_nome):
            print(f"\nErro: O arquivo {script_nome} não foi encontrado!")
            input("\nPressione Enter para voltar ao menu...")
            return
        
        if sys.platform.startswith('win'):
            comando = ['python', script_nome]
        else:
            comando = ['python3', script_nome]
        
        subprocess.run(comando)
        input("\nPressione Enter para voltar ao menu...")  # Pausa após execução
    except Exception as e:
        print(f"\nOcorreu um erro ao executar {script_nome}: {str(e)}")
        input("\nPressione Enter para voltar ao menu...")

def main():
    while True:  # Loop infinito até o usuário escolher sair
        exibir_menu()
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            executar_script('add.py')
        elif opcao == '2':
            executar_script('native.py')
        elif opcao == '3':
            executar_script('service.py')
        elif opcao == '4':
            executar_script('service.py')
        elif opcao == '5':
            print("\nEncerrando o programa...")
            break  # Sai do loop while
        else:
            print("\nOpção inválida! Por favor, escolha 1, 2 ou 3.")
            input("\nPressione Enter para tentar novamente...")

if __name__ == "__main__":
    main()
