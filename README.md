# Multi-View Latent Diffusion App

## Descripción

Esta aplicación permite la carga de vistas observadas y la generación de vistas objetivo utilizando un modelo de difusión latente multi-vista. Utiliza Flask para la interfaz web y modelos de aprendizaje profundo en TensorFlow y PyTorch para el procesamiento y generación de imágenes.

## Estructura del Proyecto

```plaintext
project/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Punto de entrada de la aplicación
│   ├── views/                  # Plantillas y rutas de la interfaz de usuario
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates/
│   │       └── index.html
│   ├── static/                 # Archivos estáticos como CSS, JS y imágenes
│   │   └── styles.css
│   └── models/                 # Implementaciones de modelos y procesamiento
│       ├── __init__.py
│       ├── encoder.py
│       ├── decoder.py
│       ├── diffusion.py
│       └── nerf.py
├── data/                       # Almacenamiento de datos (imágenes, modelos, etc.)
│   ├── observed/
│   ├── target/
│   └── generated/
├── scripts/                    # Scripts para preprocesamiento de datos y entrenamiento
│   ├── preprocess.py
│   └── train.py
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Documentación del proyecto
```
