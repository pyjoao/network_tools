import requests
from bs4 import BeautifulSoup

def get_public_ipv4():
    urls = [
        'https://ipv4.whatismyip.akamai.com/',
        'https://ipv4.icanhazip.com/'
    ]
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            continue
    return None

def get_public_ipv6():
    urls = [
        'https://ipv6.whatismyip.akamai.com/',
        'https://ipv6.icanhazip.com/'
    ]
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            continue
    return None

def get_ip_info(ip):
    try:
        url = f"https://bgp.he.net/ip/{ip}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extrai apenas o ASN (as outras informações foram removidas)
            asn_tag = soup.find("a", href=lambda x: x and x.startswith("/AS"))
            asn = asn_tag.text.strip() if asn_tag else "Não encontrado"
            
            return {
                "ASN": asn
            }
        else:
            return {"Erro": "Falha ao consultar BGP.he.net"}
    except Exception as e:
        return {"Erro": f"Erro na consulta: {str(e)}"}

def main():
    print("Verificando IPs públicos e informações de rede...\n")
    
    ipv4 = get_public_ipv4()
    if ipv4:
        print(f"🔷 IPv4: {ipv4}")
        ipv4_info = get_ip_info(ipv4)
        print(f"   → ASN: {ipv4_info.get('ASN', 'N/A')}\n")
    else:
        print("❌ Não foi possível obter o IPv4 público\n")
    
    ipv6 = get_public_ipv6()
    if ipv6:
        print(f"🔷 IPv6: {ipv6}")
        ipv6_info = get_ip_info(ipv6)
        print(f"   → ASN: {ipv6_info.get('ASN', 'N/A')}\n")
    else:
        print("❌ Não foi possível obter o IPv6 público\n")

if __name__ == "__main__":
    main()