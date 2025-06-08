# Documentação do sistema para tratamento de relatórios `autofind` de OLTs Huawei
## Visão Geral do Sistema
Este conjunto de scripts foi desenvolvido especificamente para processar relatórios autofind gerados por OLTs (Optical Line Terminals) da Huawei, automatizando a criação de scripts de configuração para administração de redes GPON.
Funcionalidades Principais

### Processamento do Relatório Autofind:
- Filtra colunas desnecessárias do relatório bruto
- Ordena ONTs por posição (F/S/P)
- Adiciona metadados de configuração (VLAN, GEMPORT, ONT-ID)

### Geração de Scripts de Configuração:
- Adoção de ONTs (add.py)
- Configuração de VLAN nativa (native.py)
- Criação de service ports (service.py)

### Fluxo de Trabalho Típico
- Extrair relatório autofind da OLT Huawei (normalmente via U2000 ou CLI)
- Salvar como CSV com o nome data.csv na pasta dos scripts
- Processar o arquivo com organizador-csv.py
- Gerar scripts através do menu principal (main.py)

## Estrutura do Relatório Autofind
O sistema espera um CSV com a estrutura típica de relatórios autofind da Huawei, contendo:

### Campos obrigatórios:
- F/S/P (Formato Frame/Slot/Port)
- Ont SN (Número de série da ONT)
- Password (Senha da ONT)
- Ont Version (Modelo do equipamento)
      
### Campos adicionais tratados:
- Number (Número sequencial)
- Loid, Checkcode
- VendorID, Ont EquipmentID
      
## Processamento pelo Organizador CSV
O organizador-csv.py realiza:
- Filtragem de colunas: Remove dados sensíveis/desnecessários como senhas
- Ordenação lógica: Organiza ONTs por F/S/P (numérica, não alfabética)
- Padronização:
- Adiciona VLAN de serviço
- Define GEMPORT (padrão ou customizado)
- Sequência de ONT-ID

### Scripts Gerados

1. Adoção de ONTs (add.py)

```bash
ont add 1/1/1 sn-auth ALCL98765432 omci ont-lineprofile-id 1000 ont-srvprofile-id 1000 desc cliente01
```

Parâmetros configuráveis:

- Número inicial da sequência de clientes
- Perfis de linha/serviço (usam o valor da VLAN)

2. Native VLAN (native.py)
```bash
ont port native-vlan 1 0 eth 1 vlan 1000 priority 0
quit
```

- Parâmetros configuráveis:
- ONT-ID inicial
- Prioridade VLAN (fixa em 0)

3. Service Port (service.py)
```bash
service-port vlan 1000 gpon 1/1/1 ont 0 gemport 1000 multi-service user-vlan 1000 tag-transform translate
```

## Melhores Práticas
### Antes de processar:
- Verifique se o relatório contém todas ONTs desejadas
- Confira a consistência dos dados (F/S/P válidos, SNs únicos)

### Durante o processamento:
- Anote os valores de VLAN/GEMPORT utilizados
- Guarde uma cópia do CSV original

### Após geração:
- Revise os scripts antes de aplicar na OLT
- Para grandes quantidades, considere dividir em lotes

### Casos Especiais
- ONT com senha conhecida:
- O campo Password é removido por segurança
- Se necessário, adicione manualmente ao comando de adoção

### Múltiplas VLANs:
- O sistema atual suporta uma VLAN por ONT
- Para cenários mais complexos, edite manualmente os scripts gerados

### Modelos específicos de ONT:
- O campo Ont Version é preservado para referência
- Pode ser usado para filtrar ONTs compatíveis

## Segurança
- Dados sensíveis (senhas, LOIDs) são automaticamente removidos
- Arquivos gerados são salvos em subpasta script/
- Recomenda-se apagar os arquivos após uso em produção

### Limitações Conhecidas
1. Suporta apenas uma VLAN por ONT nos scripts gerados
2. Assume configuração ETH1 para VLAN nativa
3. GEMPORT padrão igual à VLAN (customizável durante o processamento)
       
Este sistema otimiza significativamente o processo de configuração massiva de ONTs em redes GPON baseadas em equipamentos Huawei, reduzindo erros manuais e tempo de implantação.
