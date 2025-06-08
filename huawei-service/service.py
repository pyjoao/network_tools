import csv

def generate_service_ports(csv_file, output_file):
    with open(csv_file, mode='r') as file, open(output_file, mode='w') as out_file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extrai os campos necessários
            fsp = row['F/S/P']
            vlan = row['VLAN']
            gemport = row['GEMPORT']
            ont_id = row['ONT-ID']
            
            # Gera a string no formato desejado
            service_port = f"service-port vlan {vlan} gpon {fsp} ont {ont_id} gemport {gemport} multi-service user-vlan {vlan} tag-transform translate\n"
            out_file.write(service_port)

# Nomes dos arquivos
csv_file = 'data.csv'
output_file = 'script_service.txt'

# Gerar o arquivo de saída
generate_service_ports(csv_file, output_file)

print(f"Arquivo '{output_file}' gerado com sucesso!")