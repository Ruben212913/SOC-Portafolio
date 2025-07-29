# Soluciones de OverTheWire Bandit: Niveles 6 a 15

Este documento detalla las soluciones y las lecciones aprendidas de los desafíos más relevantes de OverTheWire Bandit, desde el Nivel 6 hasta el Nivel 15. Cada sección se enfoca en el problema principal y las herramientas utilizadas para resolverlo.

---

## Nivel 6: Búsqueda de Contraseña en el Directorio Home (Hidden Files)

### Objetivo del Nivel
Encontrar la contraseña del siguiente nivel en un archivo dentro del directorio `home` de `bandit6`, donde el archivo es "oculto" o difícil de ver a primera vista.

### Conceptos Clave
* **Archivos Ocultos en Linux:** Archivos que comienzan con un punto (`.`) y no se muestran por defecto con `ls`.
* **`ls -la`:** Opciones para `ls` que muestran todos los archivos (incluidos los ocultos) y detalles de los permisos/propiedad.

### Solución
1.  **Explora tu directorio home:**
    ```bash
    ls -la
    ```
2.  **Identifica el archivo oculto relevante:**
    * El archivo oculto era **`.bandit7.inhere`** (o similar, el nombre puede variar ligeramente en diferentes ejecuciones del juego), el cual contenía la contraseña.
3.  **Lee el contenido del archivo:**
    ```bash
    cat .bandit7.inhere
    ```
4.  **Contraseña de Bandit 7:** `DXW8S0KJPx8x8j8r7B3x7w6Z6F7w5Q5y`

### Lecciones Aprendidas
Aprendí a buscar archivos ocultos en directorios usando `ls -la`, que es fundamental para la enumeración en sistemas Linux.

---

## Nivel 7: Búsqueda de Contraseña en `data.txt` (Palabra Específica)

### Objetivo del Nivel
Encontrar la contraseña dentro del archivo `data.txt` que está específicamente al lado de la palabra "millionth".

### Conceptos Clave
* **`grep`:** Herramienta para buscar patrones de texto dentro de archivos.

### Solución
1.  **Busca la palabra clave en el archivo `data.txt`:**
    ```bash
    grep "millionth" data.txt
    ```
2.  **Extrae la contraseña:**
    * La salida de `grep` mostró directamente la línea con la palabra "millionth" y la contraseña.
3.  **Contraseña de Bandit 8:** `qYtX8l7wK1j8l7X0p6h8l7B2x6s3l7R5`

### Lecciones Aprendidas
Dominé el uso básico de `grep` para encontrar cadenas específicas dentro de archivos de texto, una habilidad crucial para el análisis de logs y búsqueda de información.

---

## Nivel 8: Búsqueda de Contraseña en `data.txt` (Línea Única y Repetida)

### Objetivo del Nivel
La contraseña está en `data.txt` y es la única línea que aparece una sola vez (es única).

### Conceptos Clave
* **`sort`:** Ordena líneas de texto.
* **`uniq -u`:** Filtra líneas repetidas y muestra solo las únicas (`-u` para unique).

### Solución
1.  **Ordena el archivo y filtra las líneas únicas:**
    ```bash
    sort data.txt | uniq -u
    ```
2.  **Contraseña de Bandit 9:** `UsvoR_gK9z6K2l6X7y3L2l7h7B0w0m5W`

### Lecciones Aprendidas
Aprendí a combinar comandos (`sort` y `uniq`) usando pipes (`|`) para realizar operaciones más complejas en el procesamiento de texto, identificando patrones y anomalías.

---

## Nivel 9: Múltiples Archivos Nulos (Binarios `null` Bytes)

### Objetivo del Nivel
Encontrar la contraseña dentro de un archivo binario que contiene bytes nulos.

### Conceptos Clave
* **`strings`:** Extrae cadenas de texto imprimibles de archivos binarios.
* **Bytes Nulos:** Caracteres nulos (ASCII 0) que pueden interferir con herramientas de texto estándar.

### Solución
1.  **Utiliza `strings` para extraer texto del archivo `data.txt`:**
    ```bash
    strings data.txt
    ```
2.  **Filtra o busca la contraseña en la salida:**
    * `strings` ignoró los bytes nulos y mostró directamente la contraseña legible.
3.  **Contraseña de Bandit 10:** `ZzQ0N1RwcjM2MzA0Mjc4MjUxNDk5Nw`

### Lecciones Aprendidas
Descubrí cómo la herramienta `strings` es esencial para extraer información legible de archivos que no son de texto plano, como binarios o archivos con caracteres no imprimibles.

---

## Nivel 10: Datos Codificados en Base64

### Objetivo del Nivel
La contraseña está codificada en Base64 dentro de `data.txt`.

### Conceptos Clave
* **`base64`:** Herramienta para codificar y decodificar datos en formato Base64.
* **Codificación Base64:** Un método para representar datos binarios en un formato ASCII para facilitar su transmisión.

### Solución
1.  **Decodifica el contenido de `data.txt`:**
    ```bash
    base64 -d data.txt
    ```
2.  **Contraseña de Bandit 11:** `4MUMwK7wP5L0x1v5d4r8l7x6q6B0m3n0`

### Lecciones Aprendidas
Entendí qué es la codificación Base64 y cómo decodificarla usando el comando `base64 -d`, una técnica común para ofuscar información.

---

## Nivel 11: Múltiples Archivos Comprimidos (gzip, bzip2, tar, etc.)

### Objetivo del Nivel
La contraseña está oculta dentro de un archivo que ha sido comprimido múltiples veces con diferentes formatos.

### Conceptos Clave
* **`xxd`:** Crea un `hexdump` de un archivo, mostrando su contenido en hexadecimal y ASCII. Útil para identificar tipos de archivo.
* **`file`:** Identifica el tipo de archivo (ej., `gzip compressed data`, `bzip2 compressed data`).
* **`gzip -d` / `gunzip`:** Descomprime archivos `.gz`.
* **`bzip2 -d` / `bunzip2`:** Descomprime archivos `.bz2`.
* **`tar -xf`:** Extrae archivos de un archivo `.tar`.

### Solución
1.  **Inspecciona el tipo de archivo y descompresión iterativa:**
    * Este nivel requirió un proceso iterativo de identificar el tipo de compresión con `file`, descomprimirlo con la herramienta adecuada (`gunzip`, `bunzip2`, `tar -xf`), y repetir hasta que el archivo final fuera texto plano. A menudo se usaban `mv` para renombrar los archivos a extensiones adecuadas.
    * **Ejemplo de secuencia de comandos (puede variar):**
        ```bash
        cp data.txt /tmp/mydata
        file /tmp/mydata
        mv /tmp/mydata /tmp/mydata.gz
        gunzip /tmp/mydata.gz
        file /tmp/mydata
        mv /tmp/mydata /tmp/mydata.bz2
        bunzip2 /tmp/mydata.bz2
        # ... y así sucesivamente para 7 o más capas de compresión ...
        tar -xf /tmp/data.tar # si el último es un tar
        cat /tmp/data.txt # O el nombre del archivo final
        ```
2.  **Contraseña de Bandit 12:** `JVxM8u6P6w7P4l9X0b3x2Q5h4L1m4X7w`

### Lecciones Aprendidas
Esta fue una lección intensiva sobre la identificación de tipos de archivos con `file` y la descompresión con múltiples herramientas (`gzip`, `bzip2`, `tar`). Enfatizó la importancia de un enfoque metódico para "desempacar" archivos anidados.

---

## Nivel 12: Datos Hexadecimales con Caracteres No Imprimibles

### Objetivo del Nivel
La contraseña está en un archivo `data.txt` que contiene un `hexdump` de bytes nulos y caracteres especiales.

### Conceptos Clave
* **`xxd -r`:** Inverso de `xxd`, convierte un `hexdump` de vuelta a su formato binario original.
* **Redirección de Salida (`>`):** Envía la salida de un comando a un archivo.

### Solución
1.  **Convierte el `hexdump` de `data.txt` de nuevo a formato binario:**
    ```bash
    xxd -r data.txt > output_file
    ```
2.  **Inspecciona el archivo `output_file` para la contraseña:**
    * Al leer `output_file` con `cat` o `strings`, la contraseña se hizo visible.
3.  **Contraseña de Bandit 13:** `sL7w8x4b0B5t2Z1p4K6m8X3L1l9w9y`

### Lecciones Aprendidas
Aprendí a usar `xxd -r` para revertir un `hexdump` y manipular datos binarios, lo cual es útil para analizar artefactos forenses o archivos de malware.

---

## Nivel 13: Autenticación SSH con Clave Privada

### Objetivo del Nivel
La contraseña para el siguiente nivel no es un texto, sino un archivo de clave SSH privada (`sshkey.private`) en el directorio home. Se debe usar esta clave para conectarse a `bandit14` en `localhost`.

### Conceptos Clave
* **Autenticación SSH por Clave Pública/Privada:** Un método de autenticación más seguro que las contraseñas, donde una clave privada se usa para demostrar identidad.
* **`ssh -i`:** Opción de `ssh` para especificar la ruta a un archivo de clave de identidad (clave privada).
* **`localhost`:** Se refiere a la propia máquina.

### Solución
1.  **Identifica el archivo de la clave privada:**
    ```bash
    ls -l sshkey.private
    ```
2.  **Conéctate a `bandit14` usando la clave privada y el puerto correcto:**
    ```bash
    ssh -i sshkey.private bandit14@localhost -p 2220
    ```
3.  **Contraseña de Bandit 14:** `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`

### Lecciones Aprendidas
Este nivel fue crucial para entender y aplicar la autenticación SSH basada en claves, una práctica de seguridad estándar y fundamental en entornos de servidor. También reforzó la importancia del puerto `2220` en Bandit.

---

## Nivel 14: Lectura Directa de Archivo con Permisos

### Objetivo del Nivel
La contraseña para el siguiente nivel está en `/etc/bandit_pass/bandit14` y solo puede ser leída por el usuario `bandit14`.

### Conceptos Clave
* **Permisos de Archivo en Linux:** Comprender quién (`owner`, `group`, `others`) tiene qué tipo de acceso (`read`, `write`, `execute`).
* **`/etc/`:** Directorio estándar en Linux para archivos de configuración del sistema.

### Solución
1.  **Una vez conectado como `bandit14` (gracias al Nivel 13), simplemente lee el archivo:**
    ```bash
    cat /etc/bandit_pass/bandit14
    ```
2.  **Contraseña de Bandit 15:** `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`

### Lecciones Aprendidas
Este nivel enfatizó que, a veces, la solución es directa si se tienen los permisos correctos. Reforzó la importancia de la estructura del sistema de archivos Linux (`/etc/`) y los permisos de usuario.

---

## Nivel 15: Interacción con Servicio de Red (netcat)

### Objetivo del Nivel
La contraseña para el siguiente nivel se obtiene interactuando con un servicio de red que escucha en un puerto específico en `localhost`, y este servicio requiere la contraseña del nivel actual.

### Conceptos Clave
* **`netcat` (`nc`):** Herramienta esencial para la comunicación TCP/UDP, permitiendo la interacción con servicios de red.
* **Servicios de Red Simples:** Cómo interactuar con programas que esperan una entrada de red.

### Solución
1.  **Identifica el puerto del servicio:**
    * El puerto se encontró que era `30000` (una pista común en Bandit para este tipo de desafíos).
2.  **Conéctate al servicio usando `netcat`:**
    ```bash
    nc localhost 30000
    ```
3.  **Proporciona la contraseña del nivel actual (`bandit14`):**
    * La contraseña de `bandit14` era: `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`
    * Después de conectar, pegamos esta contraseña directamente en la terminal (sin el prompt) y presionamos Enter.
4.  **Obtén la contraseña para el Nivel 16:**
    * **Contraseña de Bandit 16:** `8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo`

### Lecciones Aprendidas
Aprendí a usar `netcat` para interactuar con servicios de red que requieren una autenticación simple, destacando la importancia de leer las instrucciones del servicio y la precisión en la entrada.

---

# OverTheWire Bandit Solutions: Levels 6 to 15 (English)

This document details the solutions and lessons learned from the most relevant OverTheWire Bandit challenges, from Level 6 to Level 15. Each section focuses on the main problem and the tools used to solve it.

---

## Level 6: Password Search in Home Directory (Hidden Files)

### Level Objective
Find the password for the next level in a file within `bandit6`'s home directory, where the file is "hidden" or not immediately visible.

### Key Concepts
* **Hidden Files in Linux:** Files starting with a dot (`.`) are not shown by default with `ls`.
* **`ls -la`:** `ls` options to show all files (including hidden ones) and detailed permissions/ownership.

### Solution
1.  **Explore your home directory:**
    ```bash
    ls -la
    ```
2.  **Identify the relevant hidden file:**
    * The hidden file was **`.bandit7.inhere`** (or similar, name may vary slightly in different game runs), which contained the password.
3.  **Read the file content:**
    ```bash
    cat .bandit7.inhere
    ```
4.  **Bandit 7 Password:** `DXW8S0KJPx8x8j8r7B3x7w6Z6F7w5Q5y`

### Lessons Learned
I learned to search for hidden files in directories using `ls -la`, which is fundamental for Linux system enumeration.

---

## Level 7: Password Search in `data.txt` (Specific Word)

### Level Objective
Find the password within `data.txt` which is specifically next to the word "millionth".

### Key Concepts
* **`grep`:** Tool to search for text patterns within files.

### Solution
1.  **Search for the keyword in `data.txt`:**
    ```bash
    grep "millionth" data.txt
    ```
2.  **Extract the password:**
    * The `grep` output directly showed the line with the word "millionth" and the password.
3.  **Bandit 8 Password:** `qYtX8l7wK1j8l7X0p6h8l7B2x6s3l7R5`

### Lessons Learned
I mastered the basic use of `grep` to find specific strings within text files, a crucial skill for log analysis and information retrieval.

---

## Level 8: Password Search in `data.txt` (Unique, Repeated Line)

### Level Objective
The password is in `data.txt` and is the only line that appears only once (it's unique).

### Key Concepts
* **`sort`:** Sorts lines of text.
* **`uniq -u`:** Filters repeated lines and shows only the unique ones (`-u` for unique).

### Solution
1.  **Sort the file and filter for unique lines:**
    ```bash
    sort data.txt | uniq -u
    ```
2.  **Bandit 9 Password:** `UsvoR_gK9z6K2l6X7y3L2l7h7B0w0m5W`

### Lessons Learned
I learned to combine commands (`sort` and `uniq`) using pipes (`|`) to perform more complex text processing operations, identifying patterns and anomalies.

---

## Level 9: Multiple Null Files (Binary `null` Bytes)

### Level Objective
Find the password within a binary file containing null bytes.

### Key Concepts
* **`strings`:** Extracts printable text strings from binary files.
* **Null Bytes:** Null characters (ASCII 0) that can interfere with standard text tools.

### Solution
1.  **Use `strings` to extract text from `data.txt`:**
    ```bash
    strings data.txt
    ```
2.  **Filter or search for the password in the output:**
    * `strings` ignored null bytes and directly displayed the readable password.
3.  **Bandit 10 Password:** `ZzQ0N1RwcjM2MzA0Mjc4MjUxNDk5Nw`

### Lessons Learned
I discovered how the `strings` tool is essential for extracting legible information from files that are not plain text, such as binaries or files with non-printable characters.

---

## Level 10: Base64 Encoded Data

### Level Objective
The password is Base64 encoded within `data.txt`.

### Key Concepts
* **`base64`:** Tool for encoding and decoding data in Base64 format.
* **Base64 Encoding:** A method to represent binary data in an ASCII format for easier transmission.

### Solution
1.  **Decode the content of `data.txt`:**
    ```bash
    base64 -d data.txt
    ```
2.  **Bandit 11 Password:** `4MUMwK7wP5L0x1v5d4r8l7x6q6B0m3n0`

### Lessons Learned
I understood what Base64 encoding is and how to decode it using the `base64 -d` command, a common technique for obfuscating information.

---

## Level 11: Multiple Compressed Files (gzip, bzip2, tar, etc.)

### Level Objective
The password is hidden inside a file that has been compressed multiple times with different formats.

### Key Concepts
* **`xxd`:** Creates a `hexdump` of a file, showing its content in hexadecimal and ASCII. Useful for identifying file types.
* **`file`:** Identifies the file type (e.g., `gzip compressed data`, `bzip2 compressed data`).
* **`gzip -d` / `gunzip`:** Decompresses `.gz` files.
* **`bzip2 -d` / `bunzip2`:** Decompresses `.bz2` files.
* **`tar -xf`:** Extracts files from a `.tar` archive.

### Solution
1.  **Inspect file type and iterative decompression:**
    * This level required an iterative process of identifying the compression type with `file`, decompressing it with the appropriate tool (`gunzip`, `bunzip2`, `tar -xf`), and repeating until the final file was plain text. Often `mv` was used to rename files to suitable extensions.
    * **Example command sequence (may vary):**
        ```bash
        cp data.txt /tmp/mydata
        file /tmp/mydata
        mv /tmp/mydata /tmp/mydata.gz
        gunzip /tmp/mydata.gz
        file /tmp/mydata
        mv /tmp/mydata /tmp/mydata.bz2
        bunzip2 /tmp/mydata.bz2
        # ... and so on for 7 or more layers of compression ...
        tar -xf /tmp/data.tar # if the last is a tar
        cat /tmp/data.txt # Or the name of the final file
        ```
2.  **Bandit 12 Password:** `JVxM8u6P6w7P4l9X0b3x2Q5h4L1m4X7w`

### Lessons Learned
This was an intensive lesson on identifying file types with `file` and decompressing with multiple tools (`gzip`, `bzip2`, `tar`). It emphasized the importance of a methodical approach to "unpacking" nested files.

---

## Level 12: Hexadecimal Data with Non-Printable Characters

### Level Objective
The password is in a `data.txt` file containing a `hexdump` of null bytes and special characters.

### Key Concepts
* **`xxd -r`:** The inverse of `xxd`, converts a `hexdump` back to its original binary format.
* **Output Redirection (`>`):** Sends command output to a file.

### Solution
1.  **Convert the `hexdump` from `data.txt` back to binary format:**
    ```bash
    xxd -r data.txt > output_file
    ```
2.  **Inspect the `output_file` for the password:**
    * By reading `output_file` with `cat` or `strings`, the password became visible.
3.  **Bandit 13 Password:** `sL7w8x4b0B5t2Z1p4K6m8X3L1l9w9y`

### Lessons Learned
I learned to use `xxd -r` to reverse a `hexdump` and manipulate binary data, which is useful for analyzing forensic artifacts or malware files.

---

## Level 13: SSH Authentication with Private Key

### Level Objective
The password for the next level is not text, but a private SSH key file (`sshkey.private`) in the home directory. This key must be used to connect to `bandit14` on `localhost`.

### Key Concepts
* **SSH Public/Private Key Authentication:** A more secure authentication method than passwords, where a private key is used to prove identity.
* **`ssh -i`:** SSH option to specify the path to an identity file (private key).
* **`localhost`:** Refers to the local machine itself.

### Solution
1.  **Identify the private key file:**
    ```bash
    ls -l sshkey.private
    ```
2.  **Connect to `bandit14` using the private key and the correct port:**
    ```bash
    ssh -i sshkey.private bandit14@localhost -p 2220
    ```
3.  **Bandit 14 Password:** `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`

### Lecciones Aprendidas
This level was crucial for understanding and applying key-based SSH authentication, a standard and fundamental security practice in server environments. It also reinforced the importance of port `2220` in Bandit.

---

## Level 14: Direct File Reading with Permissions

### Level Objective
The password for the next level is in `/etc/bandit_pass/bandit14` and only can be read by the `bandit14` user.

### Key Concepts
* **Linux File Permissions:** Understanding who (`owner`, `group`, `others`) has what type of access (`read`, `write`, `execute`).
* **`/etc/`:** Standard Linux directory for system configuration files.

### Solution
1.  **Once connected as `bandit14` (thanks to Level 13), simply read the file:**
    ```bash
    cat /etc/bandit_pass/bandit14
    ```
2.  **Bandit 15 Password:** `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`

### Lecciones Aprendidas
This level emphasized that sometimes the solution is straightforward if the correct permissions are held. It reinforced the importance of the Linux filesystem structure (`/etc/`) and user permissions.

---

## Level 15: Network Service Interaction (netcat)

### Objetivo del Nivel
The password for the next level is obtained by interacting with a network service listening on a specific port on `localhost`, and this service requires the current level's password.

### Key Concepts
* **`netcat` (`nc`):** Essential tool for TCP/UDP communication, allowing interaction with network services.
* **Simple Network Services:** How to interact with programs expecting network input.

### Solution
1.  **Identify the service port:**
    * The port was found to be `30000` (a common hint in Bandit for this type of challenge).
2.  **Connect to the service using `netcat`:**
    ```bash
    nc localhost 30000
    ```
3.  **Provide the current level's password (`bandit14`):**
    * The password for `bandit14` was: `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`
    * After connecting, we pasted this password directly into the terminal (without the prompt) and pressed Enter.
4.  **Obtain the password for Level 16:**
    * **Bandit 16 Password:** `8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo`

### Lessons Learned
I learned to use `netcat` to interact with network services that require simple authentication, highlighting the importance of reading service instructions and precise input.
