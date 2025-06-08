import csv

def gerar_comandos_ont():
    # Solicitar o número inicial da ONT-ID ao usuário
    try:
        ont_id_inicial = int(input("Digite o número inicial da ONT-ID: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        return

    # Abrir arquivo de saída para escrita
    with open('script_native.txt', mode='w') as arquivo_saida:
        try:
            with open('data.csv', mode='r') as arquivo_csv:
                leitor_csv = csv.DictReader(arquivo_csv)
                
                # Processar cada linha do CSV
                for linha in leitor_csv:
                    # Extrair os valores necessários
                    f_s_p = linha['F/S/P']
                    vlan = linha['VLAN']
                    
                    # Extrair o último número após a última barra
                    f = f_s_p.split('/')[-1]  # [-1] pega o último elemento
                    
                    # Gerar os comandos
                    comando1 = f'ont port native-vlan {f} {ont_id_inicial} eth 1 vlan {vlan} priority 0'
                    comando2 = 'quit'
                    
                    # Escrever no arquivo
                    arquivo_saida.write(comando1 + '\n')
                    arquivo_saida.write(comando2 + '\n\n')
                    
                    # Imprimir na tela também
                    print(comando1)
                    print(comando2)
                    print()  # Linha em branco entre os blocos
                    
                    # Incrementar a ONT-ID
                    ont_id_inicial += 1
                    
            print("\nComandos salvos com sucesso em 'script_native.txt'")
                
        except FileNotFoundError:
            print("Arquivo 'data.csv' não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

# Executar a função principal
if __name__ == "__main__":
    gerar_comandos_ont()