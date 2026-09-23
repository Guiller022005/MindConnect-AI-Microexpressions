# 🧠 MindConnect AI - Servicio de Reconocimiento de Microexpresiones Faciales

![Python 3.9](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.11+-FF6F00?style=flat&logo=tensorflow&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-FaceMesh--468-00979D?style=flat)
![Licencia](https://img.shields.io/badge/Licencia-Propiedad--Intelectual--MindConnect-blue)

Módulo de Inteligencia Artificial para el ecosistema **MindConnect** (AventoAI x Breaklinestudio). Este servicio realiza el análisis fisiológico 3D post-sesión de videoconsultas WebRTC para detectar microexpresiones faciales basadas en el sistema **FACS (Facial Action Coding System) de Paul Ekman** y generar analítica clínica para especialistas de la salud mental (Caso de Uso **CU-03**).

---

## 📐 Arquitectura del Sistema

```
  ┌───────────────────────┐
  │  Imagen / Video Frame │
  └───────────┬───────────┘
              │
              ▼
  ┌─────────────────────────────────────────┐
  │ MediaPipe Face Mesh 3D                  │
  │ (Extracción de 468 Landmarks = 1404 3D) │
  └───────────┬─────────────────────────────┘
              │
      ┌───────┴───────────────────────┐
      ▼                               ▼
┌───────────────────────────┐   ┌───────────────────────────┐
│ Motor Fisiológico FACS    │   │ Red Neuronal Profunda     │
│ (Action Units de Ekman)   │   │ (Keras Landmark DNN)      │
│ Ponderación: 80%          │   │ Ponderación: 20%          │
└─────────────┬─────────────┘   └─────────────┬─────────────┘
              │                               │
              └───────────────┬───────────────┘
                              ▼
                ┌───────────────────────────┐
                │ Clasificador Ensamble IA  │
                │ (7 Microexpresiones)      │
                └───────────────────────────┘
```

El motor combina:
1. **Extracción 3D de MediaPipe Face Mesh**: Normaliza 468 coordenadas tridimensionales centradas en el puente nasal y escaladas por la distancia interocular.
2. **Motor Fisiológico Ekman FACS (80%)**: Evalúa matemáticamente desplazamientos anatómicos de Action Units (AU):
   - **Alegría (AU 12 + AU 6)**: Elevación de comisuras labiales ($\text{corner\_elev} > 0.038$).
   - **Miedo (AU 1+2+4+5)**: Elevación drástica de cejas interiores hacia la frente ($\text{inner\_brow\_lift} > 0.25$).
   - **Asco (AU 9/10)**: Elección y arrugamiento del labio superior hacia la nariz ($\text{corner\_elev} < -0.08$).
   - **Ira (AU 4)**: Inclinación descendente del ceño fruncido ($\text{brow\_slant} < -0.015$).
   - **Sorpresa (AU 26)**: Apertura de mandíbula en vertical ($\text{mouth\_h} > 0.04$).
   - **Tristeza (AU 15)**: Caída de comisuras labiales ($\text{corner\_elev} < -0.025$).
   - **Neutral**: Estado de reposo facial baseline.
3. **Red Neuronal Keras DNN (20%)**: Red neuronal multicapa (`input_shape=(1404,)`) entrenada sobre deformaciones musculares tridimensionales.

---

## 🚀 Guía de Inicio Rápido

### 1. Clonar e Instalar Dependencias

```bash
git clone https://github.com/guiller022005/MindConnect-AI-Microexpressions.git
cd MindConnect-AI-Microexpressions

# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias requeridas
pip install -r requirements.txt
```

### 2. Configurar Variables de Entorno (`.env`)

Copia el archivo de ejemplo o edita directamente tu `.env`:

```bash
cp .env.example .env
```

Contenido de `.env`:
```env
# URL o ruta local de la imagen a probar
TEST_IMAGE_URL=https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg

# Parámetros de entrenamiento de la Red Neuronal
TRAIN_EPOCHS=15
TRAIN_SAMPLES=700
SAVE_MODEL=true
MODEL_PATH=models/mindconnect_landmark_dnn.keras
```

---

## 📸 Catálogo de Imágenes de Prueba (7 Emociones)

Para probar cualquier emoción (Alegría, Miedo, Asco, Ira, Sorpresa, Tristeza, Neutral), dispones del catálogo interactivo en **[`TEST_IMAGES.md`](TEST_IMAGES.md)**.

Basta con copiar el enlace deseado de `TEST_IMAGES.md` en tu `.env` y ejecutar la demostración.

### 3. Ejecutar la Demostración

```bash
python3 src/demo_microexpressions.py
```

### Opciones por Línea de Comandos:

```bash
# Probar una URL específica directamente
python3 src/demo_microexpressions.py --image "https://st4.depositphotos.com/13318524/22528/i/1600/depositphotos_225287314-stock-photo-close-portrait-scared-frightened-old.jpg"

# Forzar re-entrenamiento del modelo DNN
python3 src/demo_microexpressions.py --retrain --epochs 20 --samples 1400
```

---

## 📹 Analítica Clínica Post-Sesión WebRTC (Caso de Uso CU-03)

El script incluye la simulación del módulo de analítica asíncrona post-sesión WebRTC. Procesa fotogramas de grabación (30 FPS) y genera un informe minuto a minuto identificando **Picos Emocionales** (Ira, Asco, Miedo o Tristeza) para la toma de decisiones del especialista.

```text
======================================================================
📹 REPORTE CLÍNICO DE MICROEXPRESIONES POST-SESIÓN (CASO DE USO CU-03)
======================================================================
Sesión: Videoconsulta Psicología (Duración simulada: 10 min)
----------------------------------------------------------------------
Minuto   | Emoción Predominante   | Confianza IA   | Alerta Clínica
----------------------------------------------------------------------
Min 01    | Ira (Anger)            |   89.6%       | ⚠️ Pico Emocional Detectado
Min 02    | Neutral                |   74.8%       | ---
Min 05    | Miedo (Fear)           |   88.4%       | ⚠️ Pico Emocional Detectado
...
```

---

## 📜 Licencia y Derechos de Propiedad Intelectual

Este módulo forma parte del ecosistema protegido de **MindConnect** (AventoAI x Breaklinestudio). Todos los derechos reservados.
