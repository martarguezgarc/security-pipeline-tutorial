"""Tutorial de Seguridad en Pipelines — Aplicación de ejemplo

ADVERTENCIA: Este archivo contiene vulnerabilidades INTENCIONALES para el tutorial.
NO uses este código en producción.
"""

import os
import sqlite3
import subprocess

# Vulnerabilidad 1: credenciales hardcodeadas
SECRET_KEY = os.environ.get("SECRET_KEY", "")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "")


def search_user(username):
    """Busca un usuario por nombre."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Vulnerabilidad 2: SQL Injection — string concatenado directamente en execute
    cursor.execute("SELECT * FROM users WHERE name = ?", (username,))

    return cursor.fetchall()


def ping_host(host):
    """Comprueba si un host es accesible."""
    # Vulnerabilidad 3: Command Injection — os.system con input del usuario
    subprocess.run(["ping", "-c", "1", host], check=True)


def main():
    print("App started")
    result = search_user("admin")
    print(f"Found: {result}")
    ping_host("localhost")


if __name__ == "__main__":
    main()
