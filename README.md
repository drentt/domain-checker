# Monitor de Vencimiento de Dominios

Esta es una herramienta de línea de comandos en Python que verifica diariamente el estado de vencimiento de una lista de dominios.

El script lee los dominios desde un archivo `domains.txt`, realiza una consulta WHOIS para cada uno y muestra su fecha de vencimiento y los días restantes.

---
### ## Características

-   **Verificación en Lote:** Revisa múltiples dominios a la vez.
-   **Entrada Sencilla:** Gestiona la lista de dominios desde un simple archivo de texto.
-   **Estados Claros:** Indica si un dominio está **Activo**, **Expira pronto** (menos de 30 días) o ya ha **Expirado**.
-   **Manejo de Errores:** Informa si un dominio no es válido o no se puede encontrar.

---
### ## Instalación

1.  **Requisitos:**
    -   Python 3.6 o superior.

2.  **Clona o descarga este repositorio.**

3.  **Instala las dependencias:**
    Abre una terminal en la carpeta del proyecto y ejecuta:
    ```bash
    pip install -r requirements.txt
    ```

---
### ## Modo de Empleo

1.  **Añade tus dominios:**
    Abre el archivo `domains.txt` y añade los dominios que deseas monitorear, **uno por línea**.
    ```
    google.com
    github.com
    wikipedia.org
    ```
    Si el archivo no existe, el script creará uno de ejemplo la primera vez que se ejecute.

2.  **Ejecuta el script:**
    Desde tu terminal, simplemente ejecuta el siguiente comando:
    ```bash
    python domain_checker.py
    ```

3.  **Revisa la salida:**
    El script imprimirá una tabla con el estado de cada dominio.

    **Ejemplo de salida:**
    ```
    --------------------------------------------------------------------------------
    Dominio                        | Estado             | Detalles
    --------------------------------------------------------------------------------
    google.com                     | ✅ Activo            | Vence el 2028-09-14 (faltan 1088 días)
    expired-domain-example.com     | EXPIRADO           | Venció el 2024-04-29
    unregistered-domain-blah.com   | ❌ Error: Dominio no encontrado o no válido.
    --------------------------------------------------------------------------------
    Verificación completada.
    ```

---
### ## Automatización

Para que este script se ejecute "cada día" automáticamente, puedes usar:
-   **Cron jobs** en macOS o Linux.
-   El **Programador de Tareas (Task Scheduler)** en Windows.