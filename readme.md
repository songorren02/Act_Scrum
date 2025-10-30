# 🌸 VIZOR — Herramienta para Red Team

**VIZOR** es una utilidad simple en **Python 3** para ejecutar herramientas básicas de comprobación de red desde una interfaz interactiva en consola.  
El script `vizor.py` incluye tres opciones:

1. **Usar nmap** — Ejecuta `nmap -p <puertos> <target>` y muestra la salida.
2. **Usar pingsweep** — Versión mínima: hace 1 `ping` a una IP y muestra si responde.
3. **Calcular sha256 de un archivo** — Lee el archivo por bloques y muestra su hash SHA-256.

Soporta dos idiomas al iniciar: **ESP** (español) y **NO** (noruego).

---

## Requisitos

- **Python 3.6+** (se recomienda Python 3.8 o superior).
- Herramientas del sistema:
  - `ping` — normalmente incluido en Windows, Linux y macOS.
  - `nmap` — necesario solo si vas a usar la opción **Usar nmap**.

> La librería `hashlib` usada para SHA-256 forma parte de la librería estándar de Python, no requiere instalación adicional.

### Instalación (comandos)

#### Debian / Ubuntu
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip nmap
