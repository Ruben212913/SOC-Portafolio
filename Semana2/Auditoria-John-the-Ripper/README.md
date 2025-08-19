# 💻 Auditoría de Contraseñas con John the Ripper

## Objetivo del Proyecto
El objetivo de este proyecto es demostrar la vulnerabilidad de las contraseñas débiles y comunes. Para ello, utilizamos la herramienta de hacking ético **John the Ripper** para descifrar hashes de contraseñas y auditar la seguridad de las credenciales.

## Herramientas Utilizadas
* **John the Ripper:** Herramienta de código abierto para descifrar contraseñas.
* **Kali Linux:** Sistema operativo especializado en ciberseguridad que incluye John the Ripper.
* **Editor de texto (`nano`):** Para crear y editar el archivo de hashes.

## Pasos del Análisis

### 1. Creación del Archivo de Hashes (`hashes.txt`)
* Creamos un archivo llamado `hashes.txt` con los hashes MD5 de contraseñas de texto plano.
* **Contenido del archivo:**

* ruben:25d55ad283aa400af464c76d7132072f
* test:098f6bcd4621d373cade4e832627b4f6
* admin:21232f297a57a5a743894a0e4a801fc3
* user:ee11cbb19052e40b07aac0ca060c23ee
* guest:a762956c3a07ed5e45a273295b93d258

### 2. Ejecución del Ataque de Diccionario
* Se ejecutó el siguiente comando en la terminal de Kali Linux para auditar el archivo:
* `john --format=Raw-MD5 hashes.txt`
* El programa inició su proceso y, al encontrar una coincidencia en su diccionario, la mostró en pantalla.

### 3. Análisis de la Salida
* La salida fue la siguiente:

* user             (user)
* admin            (admin)
* test             (test)

* El programa identificó que las contraseñas para los usuarios `user`, `admin` y `test` eran las mismas que su nombre de usuario. Esto demuestra su extrema debilidad.

## Conclusiones y Lecciones Aprendidas
* **Vulnerabilidad de Contraseñas Débiles:** Se demostró que las contraseñas de uso común son extremadamente vulnerables a un ataque de diccionario. John the Ripper las descifró en segundos, lo que resalta la importancia de educar a los usuarios para que creen contraseñas fuertes.
* **Importancia de los Hashes y los Salts:** El ejercicio nos enseñó que un hash es una "huella digital" única de una contraseña. También entendimos el concepto de "salt" y por qué su uso es crucial para prevenir ataques de diccionario.
* **Habilidad Práctica:** Este proyecto sirvió para dominar una herramienta de auditoría de contraseñas en un entorno controlado, una habilidad fundamental para cualquier analista de ciberseguridad.
