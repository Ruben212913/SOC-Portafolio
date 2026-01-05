import subprocess
from datetime import datetime

def run_command(command):
    try:
        # Ejecuta el comando y espera a que termine
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar: {command}")
        print(f"Detalle: {e.stderr}")

def auto_push():
    # 1. Obtener la fecha y hora actual para el mensaje
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensaje = f"Update automático: {fecha_actual}"
    
    print(f"🚀 Iniciando actualización del portafolio...")

    # 2. Secuencia lógica de Git
    run_command("git add .")
    run_command(f'git commit -m "{mensaje}"')
    
    # 3. Empuje inteligente (detecta si es main o master automáticamente)
    run_command("git push origin $(git branch --show-current)")

    print(f"✅ ¡Todo actualizado con éxito el {fecha_actual}!")

if __name__ == "__main__":
    auto_push()