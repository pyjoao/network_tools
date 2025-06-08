# Documentação do Script de Verificação de IP Público e ASN
## Descrição
Este script Python verifica os endereços IP públicos (IPv4 e IPv6) do host onde é executado e consulta informações de ASN (Autonomous System Number) relacionadas a esses IPs no site BGP.he.net.

## Funcionalidades
- Obtém o endereço IPv4 público

- Obtém o endereço IPv6 público (se disponível)

- Consulta o ASN associado a cada IP no BGP.he.net

- Exibe os resultados de forma clara e organizada

## Requisitos
- Python 3.x

- Bibliotecas externas:

    **`requests`**

    **`beautifulsoup4`**

## Instalação
Instale as dependências necessárias:

    pip install requests beautifulsoup4

Salve o script como `**ip_publico_asn.py**`

## Uso
Execute o script com:

```bash
python ip_publico_asn.py
```

Saída Esperada
Exemplo de saída:

```bash
Verificando IPs públicos e informações de rede...

🔷 IPv4: 123.45.67.89
   → ASN: AS12345

🔷 IPv6: 2001:db8:85a3::8a2e:370:7334
   → ASN: AS12345
```
   
## Estrutura do Código
### Funções Principais

**`get_public_ipv4()`**

Tenta obter o IPv4 público usando dois serviços diferentes

Retorna o IPv4 como string ou None se falhar

**`get_public_ipv6()`**

Tenta obter o IPv6 público usando dois serviços diferentes

Retorna o IPv6 como string ou None se falhar

**`get_ip_info(ip)`**

Consulta informações do IP no [bgp.he.net](https://bgp.he.net)

Extrai apenas o ASN associado ao IP

Retorna um dicionário com o ASN ou mensagem de erro

**`main()`**

Função principal que orquestra todo o processo

Exibe os resultados formatados


## Serviços Utilizados
### Para IPv4:

https://ipv4.whatismyip.akamai.com/

https://ipv4.icanhazip.com/

### Para IPv6:

https://ipv6.whatismyip.akamai.com/

https://ipv6.icanhazip.com/

### Para consulta ASN:

https://bgp.he.net/

## Personalização
O script pode ser facilmente modificado para:

- Adicionar mais serviços de verificação de IP

- Incluir timeout diferente

- Extrair mais informações do BGP.he.net

## Tratamento de Erros
O script inclui tratamento básico de erros para:

- Falhas de conexão

- Timeouts