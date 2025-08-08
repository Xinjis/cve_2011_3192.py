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
```
Antes de ejecutar el script, edita el archivo y cambia la variable host con la IP o dominio del servidor que quieres probar:
host = '192.168.31.1'

## 🧪 Ejemplo de cabecera enviada

Range: bytes=0-,5-1,5-2,5-3,5-4,5-5,5-6,5-7,5-8,5-9.

## ✅ Resultado esperado

- Si el servidor no es vulnerable, responderá con un código 200 OK y servirá contenido normalmente.
- Si el servidor es vulnerable, podrías observar lentitud, error 500, o incluso la caída del servidor.

## 🔐 Mitigación

Los servidores Apache deben actualizarse a la versión 2.2.20 o superior. Alternativamente, se puede desactivar el uso de rangos o aplicar un parche manual.

## 📚 Referencias

- CVE-2011-3192.
- Seclists Full Disclosure.
- Nmap NSE Script.

## 👨‍💻 Autor

Este script fue adaptado con fines educativos y de evaluación en entornos controlados. Úsalo con responsabilidad.
