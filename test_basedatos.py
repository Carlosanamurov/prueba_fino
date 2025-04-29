

import pyodbc

connection_string = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:carlos-server.database.windows.net,1433;"
    "Database=DMZ_ColegioUnion;"
    "Uid=admin-carlos;"
    "Pwd=@root.123;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

try:
    conn = pyodbc.connect(connection_string)
    print("Conexión exitosa")
except Exception as e:
    print(f"Error de conexión: {e}")
