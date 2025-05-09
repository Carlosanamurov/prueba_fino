from urllib.parse import quote_plus
import mysql.connector

# Codifica la contraseña (para caracteres especiales como +, @, etc.)
password_encoded = quote_plus("Deviozapp10+")  # Resultado: "Deviozapp10%2B"

try:
    conn = mysql.connector.connect(
        host="auth-db465.hstgr.io",
        user="u777467137_deviozapp",
        password="Deviozapp10+",  # Usa la contraseña ORIGINAL aquí
        database="u777467137_deviozapp",
        port=3306,
        ssl_disabled=True,  # Importante para Hostinger
        connect_timeout=5
    )
    print("✅ ¡Conexión exitosa!")
    conn.close()
except mysql.connector.Error as err:
    print(f"❌ Error de MySQL: {err}")