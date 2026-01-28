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

if __name__ == "__main__":
    print("--- 🔐 SOC Hash Integrity Tool ---")
    
    # ESTE ES EL INPUT QUE MENCIONAS:
    ruta_archivo = input("\n[?] Arrastra el archivo aquí o escribe su ruta: ")
    
    # Limpiamos las comillas por si el usuario arrastró el archivo a la terminal
    ruta_archivo = ruta_archivo.replace("'", "").replace('"', "").strip()

    if os.path.isfile(ruta_archivo):
        hash_result = calculate_sha256(ruta_archivo)
        print(f"\n[+] SHA-256: {hash_result}")
    else:
        print("[!] Error: No se encontró el archivo. Revisa la ruta.")