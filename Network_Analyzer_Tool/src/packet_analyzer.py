from scapy.all import sniff, IP, TCP, Ether

# ============================================================
# 🧠 LÓGICA DE TRADUCCIÓN DE BANDERAS (TCP FLAGS)
# 
# Significado de las Siglas:
# - SYN (Synchronize): "Hola, ¿podemos hablar?" (Inicio)
# - ACK (Acknowledgment): "Entendido, te escucho" (Confirmación)
# - RST (Reset): "Error / Conexión cortada" (Reinicio)
# - FIN (Finish): "Ya terminé, adiós" (Finalización)
# ============================================================
def traducir_flags(pkt):
    """
    Traduce el valor hexadecimal de las banderas TCP a texto legible.
    Usa una operación lógica (&) para verificar qué bandera está activa.
    """
    flags = pkt[TCP].flags
    description = []
    
    if flags & 0x02: description.append("SYN")
    if flags & 0x10: description.append("ACK")
    if flags & 0x04: description.append("RST")
    if flags & 0x01: description.append("FIN")
    
    return " | ".join(description) if description else "N/A"

# ============================================================
# 🔍 PASO 1: FUNCIÓN DE ANÁLISIS TÉCNICO
# 
# Lógica: Esta función actúa como un microscopio. Descompone
# el paquete en capas (Layers) para extraer las direcciones.
# 
# Conceptos:
# - IP (Internet Protocol): Dirección lógica del equipo.
# - TCP (Transmission Control Protocol): Protocolo de transporte confiable.
# ============================================================
def analizar_paquete(packet):
    # Verificamos si el paquete tiene la capa IP (Direcciones de red)
    if packet.haslayer(IP):
        ip_src = packet[IP].src  # IP de Origen
        ip_dst = packet[IP].dst  # IP de Destino
        
        # Verificamos si el paquete es TCP (Protocolo de Conexión)
        if packet.haslayer(TCP):
            port_src = packet[TCP].sport # Puerto de Origen
            port_dst = packet[TCP].dport # Puerto de Destino
            info_flags = traducir_flags(packet)
            
            print(f"\n[+] PAQUETE CAPTURADO")
            print(f"    RUTA: {ip_src}:{port_src} ---> {ip_dst}:{port_dst}")
            print(f"    ESTADO (FLAGS): {info_flags}")

# ============================================================
# 🚀 PASO 2: PUNTO DE ENTRADA (MAIN)
# 
# Lógica: Pone la tarjeta de red en "Modo Promiscuo" para
# escuchar todo el tráfico que pase, no solo el dirigido a ti.
# ============================================================
def main():
    print("="*60)
    print("🛡️  SOC ANALYZER - Herramienta de Monitoreo de Red")
    print("Estado: Escuchando tráfico en tiempo real...")
    print("="*60)
    
    try:
        # sniff() es la función de Scapy que captura paquetes
        # prn: llama a la función de análisis por cada paquete recibido
        # count: se detiene tras capturar 15 paquetes para revisión
        # store: 0 significa que no guarda todo en RAM para evitar lentitud
        sniff(prn=analizar_paquete, count=15, store=0)
        print("\n\n" + "="*60)
        print("✅ Captura finalizada con éxito.")
        print("="*60)
    except PermissionError:
        print("\n❌ ERROR: Debes ejecutar este script con privilegios de ROOT (sudo).")
    except KeyboardInterrupt:
        print("\n\n🛑 Monitoreo detenido por el usuario.")

if __name__ == "__main__":
    main()