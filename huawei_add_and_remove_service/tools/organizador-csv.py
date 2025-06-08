import csv
import os
import sys

# Colunas a serem removidas
COLUNAS_REMOVER = [
    'Number', 'Password', 'Loid', 'Checkcode', 'VendorID',
    'Ont Version', 'Ont SoftwareVersion', 'Ont EquipmentID', 'Ont autofind time'
]

def remover_colunas_indesejadas(rows):
    """Remove as colunas especificadas da lista de dicionários"""
    if not rows:
        return rows
        
    # Filtra apenas colunas que não estão na lista de remoção
    colunas_validas = [col for col in rows[0].keys() if col not in COLUNAS_REMOVER]
    
    # Cria nova lista mantendo apenas colunas válidas
    dados_filtrados = []
    for row in rows:
        dados_filtrados.append({k: v for k, v in row.items() if k in colunas_validas})
    
    return dados_filtrados

def sort_fsp_numerically(fsp):
    """Ordena F/S/P como números (ex: '0/0/11' → (0, 0, 11))"""
    try:
        f, s, p = map(int, fsp.split('/'))
        return (f, s, p)
    except:
        return (0, 0, 0)

def processar_arquivo(input_file):
    """Lê, filtra e ordena o arquivo CSV"""
    try:
        with open(input_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            rows = list(csv_reader)
            
            if not rows:
                print("\n⚠️ O arquivo está vazio!")
                return None
                
            # Remove colunas indesejadas
            rows = remover_colunas_indesejadas(rows)
            
            # Ordena por F/S/P
            return sorted(rows, key=lambda row: sort_fsp_numerically(row.get('F/S/P', '0/0/0')))
    except Exception as e:
        print(f"\n❌ Erro ao processar o arquivo: {str(e)}")
        return None

def adicionar_colunas(sorted_rows):
    """Adiciona colunas VLAN, GEMPORT e ONT-ID aos dados ordenados"""
    print("\nConfiguração de colunas adicionais:")
    
    # Configura VLAN
    vlan_value = input("Digite o valor para VLAN: ").strip()
    
    # Configura GEMPORT
    gemport_value = vlan_value
    if input("Deseja definir um GEMPORT diferente da VLAN? (s/n): ").strip().lower() == 's':
        gemport_value = input("Digite o valor para GEMPORT: ").strip()

    # Configura ONT-ID (iniciando em 0 por padrão)
    ont_id_start = 0
    ont_id_input = input("Digite o número inicial para ONT-ID (padrão=0): ").strip()
    if ont_id_input.isdigit():
        ont_id_start = int(ont_id_input)

    # Adiciona colunas
    current_ont_id = ont_id_start
    for row in sorted_rows:
        row['VLAN'] = vlan_value
        row['GEMPORT'] = gemport_value
        row['ONT-ID'] = str(current_ont_id)
        current_ont_id += 1

    return sorted_rows

def salvar_resultado(data, output_file):
    """Salva os dados processados em um novo arquivo"""
    if not data:
        return False

    try:
        script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'script')
        os.makedirs(script_dir, exist_ok=True)
        output_path = os.path.join(script_dir, output_file)
        
        with open(output_path, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        
        return True
    except Exception as e:
        print(f"\n❌ Erro ao salvar o arquivo: {str(e)}")
        return False

def main():
    input_csv = 'data.csv'
    script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'script')
    
    print("=== Organizador CSV ===")
    print(f"Diretório atual: {os.path.dirname(os.path.abspath(__file__))}")
    
    if not os.path.exists(input_csv):
        print(f"\n❌ Arquivo '{input_csv}' não encontrado.")
        print("Por favor, coloque o arquivo 'data.csv' no diretório deste script.")
        sys.exit(1)
    
    # Processa o arquivo (remove colunas e ordena)
    dados_processados = processar_arquivo(input_csv)
    if not dados_processados:
        sys.exit(1)
    
    # Adiciona colunas extras
    dados_finais = adicionar_colunas(dados_processados)
    
    # Salva o resultado
    while True:
        output_name = input("\nDigite o nome do arquivo de saída (sem extensão): ").strip()
        if output_name:
            output_csv = f"{output_name}.csv"
            break
        print("⚠️ Por favor, digite um nome válido.")
    
    if salvar_resultado(dados_finais, output_csv):
        print(f"\n✅ Processamento concluído com sucesso!")
        print(f"Arquivo de saída: {os.path.join(script_dir, output_csv)}")
        print(f"Colunas removidas: {', '.join(COLUNAS_REMOVER)}")
    else:
        print("\n❌ Falha ao salvar o arquivo.")

if __name__ == "__main__":
    main()