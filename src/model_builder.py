"""
MindConnect - Módulo de Construcción de Modelos de Redes Neuronales (TensorFlow / Keras)
========================================================================================
Este módulo define dos arquitecturas de Redes Neuronales:
1. CNN Convolucional para imágenes de píxeles (48x48).
2. DNN (Deep Neural Network) de Puntos Facial Landmarks (MediaPipe 468 puntos 3D = 1404 coordenadas).

Autor: José Guillermo Paúl Díaz & Equipo AventoAI
"""

import tensorflow as tf
from tensorflow.keras import layers, models

# 7 Emociones Universales de Paul Ekman
EKMAN_EMOTIONS = [
    "Ira (Anger)",
    "Asco (Disgust)",
    "Miedo (Fear)",
    "Alegría (Happy)",
    "Tristeza (Sad)",
    "Sorpresa (Surprise)",
    "Neutral"
]

def build_microexpression_cnn(input_shape=(48, 48, 1), num_classes=7):
    """
    Construye y compila una Red Neuronal Convolucional (CNN).
    """
    model = models.Sequential(name="MindConnect_Microexpression_CNN")

    # --- Bloque 1 ---
    model.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=input_shape))
    model.add(layers.BatchNormalization())
    model.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dropout(0.25))

    # --- Bloque 2 ---
    model.add(layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dropout(0.25))

    # --- Bloque 3 ---
    model.add(layers.Conv2D(128, (3, 3), padding='same', activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dropout(0.25))

    # --- Clasificador ---
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(num_classes, activation='softmax', name="emotions_output"))

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

def build_landmark_microexpression_model(input_shape=(1404,), num_classes=7):
    """
    Construye una Red Neuronal Profunda (DNN) para procesar las 1404 coordenadas 3D
    extraídas por MediaPipe Face Mesh (468 puntos x 3D: X, Y, Z).
    """
    model = models.Sequential(name="MindConnect_MediaPipe_Landmark_DNN")

    model.add(layers.Dense(512, activation='relu', input_shape=input_shape))
    model.add(layers.BatchNormalization())
    model.add(layers.Dropout(0.3))

    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.Dropout(0.3))

    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.Dropout(0.2))

    model.add(layers.Dense(num_classes, activation='softmax', name="emotions_output"))

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

if __name__ == "__main__":
    cnn = build_microexpression_cnn()
    cnn.summary()
    print("\n" + "="*50 + "\n")
    dnn = build_landmark_microexpression_model()
    dnn.summary()
