import whois
import datetime
import os

def check_domain_status(domain_name):
    """
    Consulta la información WHOIS de un dominio y devuelve su estado de vencimiento.

    Args:
        domain_name (str): El nombre del dominio a verificar.

    Returns:
        str: Un mensaje formateado con el estado del dominio.
    """
    try:
        # Realiza la consulta WHOIS
        w = whois.whois(domain_name)

        # La respuesta puede no tener una fecha de expiración si el dominio no está registrado
        if not w.expiration_date:
            return f"{domain_name:<30} |  स्टेटस: Disponible o sin datos"

        # La librería puede devolver una lista de fechas o una sola fecha
        exp_date = w.expiration_date
        if isinstance(exp_date, list):
            exp_date = exp_date[0] # Tomamos la primera fecha si hay varias

        # Calculamos los días restantes
        now = datetime.datetime.now()
        days_left = (exp_date - now).days

        # Formateamos la fecha para una mejor lectura
        formatted_date = exp_date.strftime('%Y-%m-%d')

        # Determinamos el estado
        if days_left < 0:
            status = "EXPIRADO"
            message = f"Venció el {formatted_date}"
        elif days_left < 30:
            status = "⚠️ Expira pronto"
            message = f"Vence el {formatted_date} (en {days_left} días)"
        else:
            status = "✅ Activo"
            message = f"Vence el {formatted_date} (faltan {days_left} días)"

        return f"{domain_name:<30} | {status:<18} | {message}"

    except whois.parser.PywhoisError:
        return f"{domain_name:<30} | ❌ Error: Dominio no encontrado o no válido."
    except Exception as e:
        return f"{domain_name:<30} | ❌ Error: No se pudo procesar ({e})"

def main():
    """
    Función principal que lee los dominios de un archivo y verifica su estado.
    """
    domains_file = "domains.txt"

    # Verificar si el archivo de dominios existe
    if not os.path.exists(domains_file):
        print(f"Error: No se encontró el archivo '{domains_file}'.")
        print("Por favor, crea este archivo y añade un dominio por línea.")
        # Creamos un archivo de ejemplo para el usuario
        with open(domains_file, "w") as f:
            f.write("google.com\n")
            f.write("expired-domain-example.com\n")
        print(f"Se ha creado un archivo '{domains_file}' de ejemplo.")
        return

    # Leer los dominios del archivo
    with open(domains_file, "r") as f:
        # Ignoramos líneas vacías y eliminamos espacios en blanco
        domains = [line.strip() for line in f if line.strip()]

    if not domains:
        print(f"El archivo '{domains_file}' está vacío. Por favor, añade dominios para verificar.")
        return

    # Imprimir encabezado
    print("-" * 80)
    print(f"{'Dominio':<30} | {'Estado':<18} | {'Detalles'}")
    print("-" * 80)

    # Procesar cada dominio
    for domain in domains:
        result = check_domain_status(domain)
        print(result)

    print("-" * 80)
    print("Verificación completada.")

if __name__ == "__main__":
    main()