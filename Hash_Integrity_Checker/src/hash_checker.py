import hashlib
import os

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        return f"Error: {e}"

def verify_integrity():
    print("\n" + "="*40)
    print("🛡️  SOC FILE INTEGRITY VERIFIER  🛡️")
    print("="*40)
    
    ruta = input("\n[?] Introduce la ruta del archivo: ").strip().replace("'", "").replace('"', "")
    
    if os.path.isfile(ruta):
        current_hash = calculate_sha256(ruta)
        print(f"\n[+] Hash SHA-256 actual: \n👉 {current_hash}")
        
        # Nueva funcionalidad de comparación
        check = input("\n[?] ¿Tienes un hash de referencia para comparar? (s/n): ").lower()
        
        if check == 's':
            original_hash = input("[?] Pega el hash original: ").strip()
            
            if current_hash == original_hash:
                print("\n✅ [INTEGRIDAD CONFIRMADA]: El archivo no ha sido modificado.")
            else:
                print("\n❌ [ALERTA DE SEGURIDAD]: Los hashes no coinciden. El archivo podría estar corrupto o manipulado.")
        else:
            print("\n[*] Guarda este hash para futuras verificaciones.")
            
    else:
        print("\n[!] Error: No se pudo encontrar el archivo.")

if __name__ == "__main__":
    verify_integrity()