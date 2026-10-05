# Background Remover — Eliminación de fondo con IA

Aplicación web que elimina automáticamente el fondo de una imagen usando segmentación con redes neuronales. Interfaz construida en **Streamlit**: el usuario sube una imagen, obtiene la versión recortada y la descarga en PNG con transparencia.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B)
![rembg](https://img.shields.io/badge/rembg-segmentación-green)

<!-- SUGERENCIA: agrega una captura mostrando el antes y después -->
<!-- ![Captura](docs/screenshot.png) -->

---

## Qué hace

La librería `rembg` aplica un modelo de segmentación semántica (U²-Net) que distingue el objeto principal del fondo a nivel de píxel, sin necesidad de selección manual ni máscaras.

**Flujo de la aplicación:**

1. El usuario carga una imagen en formato PNG, JPG o JPEG.
2. Al pulsar *Remove Background*, el modelo procesa la imagen.
3. Se muestran original y resultado lado a lado para comparar.
4. Botón de descarga del PNG con canal alfa transparente.

## Estructura

```
bck-remove/
├── app.py             # Aplicación Streamlit completa
└── requirements.txt
```

## Instalación y ejecución

```bash
git clone https://github.com/EiveenL/bck-remove.git
cd bck-remove
pip install -r requirements.txt
streamlit run app.py
```

La aplicación se abre en `http://localhost:8501`.

> La primera ejecución descarga el modelo de segmentación (~170 MB); las siguientes usan la caché local.

## Dependencias

```
streamlit
rembg
pillow
```

## Formatos soportados

| Entrada | Salida |
|---------|--------|
| `.png`, `.jpg`, `.jpeg` | `.png` con transparencia |

## Posibles mejoras

- [ ] Procesamiento por lotes de varias imágenes.
- [ ] Opción de reemplazar el fondo por un color sólido o una imagen.
- [ ] Indicador de progreso durante el procesamiento.
- [ ] Control del tamaño máximo de archivo para evitar tiempos de espera largos.

## Licencia

MIT
