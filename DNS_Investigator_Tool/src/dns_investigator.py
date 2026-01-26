import socket

def investigate_dns(target):
    print(f"\n[+] Investigando: {target}")
    try:
        # Intenta obtener la información del host
        data = socket.gethostbyaddr(target)
        print(f"    [*] Nombre de Host: {data[0]}")
        print(f"    [*] Alias: {data[1]}")
        print(f"    [*] Direcciones IP: {data[2]}")
    except socket.herror:
        print(f"    [!] No se encontró información inversa (Reverse DNS) para: {target}")
    except Exception as e:
        print(f"    [!] Error: {e}")

if __name__ == "__main__":
    print("--- DNS & OSINT Investigator Tool ---")
    
    # Aquí es donde ocurre la magia: te pide la IP por teclado
    user_input = input("\n[?] Introduce la IP o Dominio a investigar: ")
    
    investigate_dns(user_input)
    
    print("\n--- Análisis Finalizado ---")