import ipaddress

def exibir_menu():
    print("\n" + "="*40)
    print("CALCULADORA DE BLOCOS IP".center(40))
    print("="*40)
    print("1. Calcular bloco IPv4")
    print("2. Calcular bloco IPv6")
    print("3. Sair do programa")
    print("="*40)

def calcular_ipv4():
    try:
        print("\n" + "-"*40)
        print("CÁLCULO DE BLOCO IPv4".center(40))
        print("-"*40)
        
        endereco = input("Digite o endereço IPv4 (ex: 192.168.1.0): ")
        
        # Opção para o usuário escolher como informar a máscara
        print("\nFormato da máscara:")
        print("1. Prefixo em bits (ex: 24)")
        print("2. Máscara decimal (ex: 255.255.255.0)")
        formato_mascara = input("Escolha o formato (1 ou 2): ")
        
        if formato_mascara == '1':
            prefixo = int(input("Digite o prefixo em bits (ex: 24): "))
            if prefixo < 0 or prefixo > 32:
                raise ValueError("Prefixo deve estar entre 0 e 32")
            mascara = ipaddress.IPv4Network(f"0.0.0.0/{prefixo}").netmask
        elif formato_mascara == '2':
            mascara = input("Digite a máscara decimal (ex: 255.255.255.0): ")
            # Converte máscara decimal para prefixo
            prefixo = ipaddress.IPv4Network(f"0.0.0.0/{mascara}").prefixlen
        else:
            raise ValueError("Opção inválida para formato de máscara")
        
        rede = ipaddress.IPv4Network(f"{endereco}/{prefixo}", strict=False)
        
        print("\nRESULTADOS:")
        print(f"Endereço de rede: {rede.network_address}")
        print(f"Prefixo: /{rede.prefixlen}")
        print(f"Máscara de rede: {rede.netmask}")
        print(f"Endereço de broadcast: {rede.broadcast_address}")
        print(f"Primeiro IP utilizável: {rede.network_address + 1}")
        print(f"Último IP utilizável: {rede.broadcast_address - 1}")
        print(f"Total de hosts possíveis: {rede.num_addresses - 2}")
        
        input("\nPressione Enter para continuar...")
        
    except ValueError as e:
        print(f"\nERRO: {e}. Verifique os valores inseridos.")
        input("Pressione Enter para tentar novamente...")

def calcular_ipv6():
    try:
        print("\n" + "-"*40)
        print("CÁLCULO DE BLOCO IPv6".center(40))
        print("-"*40)
        
        endereco = input("Digite o endereço IPv6 (ex: 2001:db8::): ")
        prefixo = int(input("Digite o prefixo (ex: 64): "))
        
        rede = ipaddress.IPv6Network(f"{endereco}/{prefixo}", strict=False)
        
        print("\nRESULTADOS:")
        print(f"Endereço de rede: {rede.network_address}")
        print(f"Prefixo de rede: /{rede.prefixlen}")
        print(f"Primeiro IP utilizável: {rede.network_address + 1}")
        print(f"Último IP utilizável: {rede.broadcast_address - 1}")
        print(f"Total de hosts possíveis: {rede.num_addresses - 2}")
        print(f"Tamanho do bloco: 2^{128 - rede.prefixlen} = {2**(128 - rede.prefixlen):,} endereços")
        
        input("\nPressione Enter para continuar...")
        
    except ValueError as e:
        print(f"\nERRO: {e}. Verifique os valores inseridos.")
        input("Pressione Enter para tentar novamente...")

def main():
    while True:
        exibir_menu()
        opcao = input("\nDigite sua opção (1-3): ")
        
        if opcao == '1':
            calcular_ipv4()
        elif opcao == '2':
            calcular_ipv6()
        elif opcao == '3':
            print("\nFim!")
            break
        else:
            print("\nOpção inválida! Digite 1, 2 ou 3.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()