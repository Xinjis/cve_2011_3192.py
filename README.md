# Apache ByteRange DoS (CVE-2011-3192) PoC

Este es un script en Python para probar la vulnerabilidad conocida como **CVE-2011-3192**, que afecta a versiones antiguas del servidor web Apache (2.0 hasta 2.2.19). Esta vulnerabilidad permite realizar un ataque de **Denegación de Servicio (DoS)** utilizando cabeceras `Range` con rangos de bytes superpuestos.

## ⚠️ Advertencia

> Este script debe usarse **solo en entornos controlados y autorizados**. Ejecutar este tipo de prueba en sistemas que no te pertenecen o sin consentimiento **es ilegal y antiético**.

## 📌 Descripción

La vulnerabilidad se basa en el mal manejo de múltiples rangos de bytes en la cabecera `Range`, lo que puede consumir excesivos recursos del servidor (CPU y RAM), provocando lentitud o caída del servicio.

Este script:

- Se conecta vía socket TCP al puerto 80 de un servidor web.
- Envía una solicitud HTTP con una cabecera `Range` malformada.
- Recibe y muestra la respuesta.

## 📂 Archivos

- `cve_2011_3192.py` – Script principal de PoC.

## 🛠️ Requisitos

- Python 3.x

## 🚀 Uso

```bash
python3 cve_2011_3192.py
