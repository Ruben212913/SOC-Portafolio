## Resultados y Hallazgos

### Intentos de Inicio de Sesión Fallidos
Para identificar los intentos de inicio de sesión fallidos, se buscaron las frases "Failed password", "authentication failure" o "invalid user" en el archivo `auth_log_analysis.log` usando `grep -Ei`.

```bash
journalctl -b | grep -Ei "failed password|authentication failure|invalid user" > auth_log_analysis.log
grep -Ei "failed password|authentication failure|invalid user" auth_log_analysis.log | wc -l
```

Se encontró un total de **4** intentos de inicio de sesión fallidos.

### Usuarios Afectados
Se observaron múltiples intentos de inicio de sesión fallidos para el usuario `kali`, como se evidencia en las entradas del log que muestran `user=kali` y `authentication failure`. Esto indica un posible intento de fuerza bruta contra la cuenta de usuario principal del sistema.

## Conclusiones y Recomendaciones

(Aquí debes completar tus conclusiones y recomendaciones. Piensa en:
* **¿Qué significa encontrar 4 fallos de autenticación seguidos?**
* **¿Qué acciones de seguridad se podrían tomar?**
    * Implementar un bloqueo de cuentas (`account lockout`) después de X intentos fallidos.
    * Usar herramientas como `fail2ban` para bloquear IPs que intenten ataques de fuerza bruta.
    * Fortalecer las políticas de contraseñas.
    * Monitoreo constante de los logs para detectar patrones similares.)
