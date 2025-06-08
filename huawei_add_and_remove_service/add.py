import csv

def process_ont_sn(ont_sn):
    return ont_sn.split()[0]

def generate_commands(csv_file, start_number):
    commands = []
    client_counter = start_number
    
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            ont_sn_processed = process_ont_sn(row['Ont SN'])
            p_value = row['F/S/P'].split('/')[-1]
            vlans = row['VLAN'].strip() if 'VLAN' in row and row['VLAN'].strip() else 'DEFAULT'
            
            # Formata o número do cliente com 2 dígitos (01, 02, etc.)
            client_number = f"{client_counter:02d}"
            command = (
                f"ont add {p_value} sn-auth {ont_sn_processed} "
                f"omci ont-lineprofile-id {vlans} ont-srvprofile-id {vlans} "
                f"desc cliente{client_number}"
            )
            commands.append(command)
            client_counter += 1
    
    return commands

def main():
    csv_file = 'data.csv'
    output_file = 'script_add_ont.txt'
    
    # Pede ao usuário o número inicial da sequência
    while True:
        try:
            start_number = int(input("Digite o número inicial para a sequência de clientes (ex: 1 para cliente01): "))
            if start_number >= 0:
                break
            print("Por favor, digite um número positivo.")
        except ValueError:
            print("Por favor, digite um número válido.")
    
    commands = generate_commands(csv_file, start_number)
    
    with open(output_file, 'w') as f:
        for cmd in commands:
            f.write(cmd + '\n')
    
    print("\nComandos gerados:")
    for cmd in commands:
        print(cmd)
    
    print(f"\nComandos salvos em {output_file}")

if __name__ == "__main__":
    main()
