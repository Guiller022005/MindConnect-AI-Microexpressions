# 📸 Catálogo de Imágenes de Prueba - Microexpresiones FACS (Paul Ekman)

Este documento contiene una colección curada de URLs de imágenes públicas para validar el reconocimiento de las **7 Microexpresiones Básicas del Modelo de Ekman** en MindConnect.

Para probar cualquiera de estas imágenes, copia el enlace deseado y reemplázalo en el archivo `.env`:

```env
TEST_IMAGE_URL=<URL_DE_LA_IMAGEN>
```

Y luego ejecuta en tu terminal:
```bash
python3 src/demo_microexpressions.py
```

---

## 1. 😃 Alegría (Happy - AU 12 + AU 6)
* **Fisiología FACS**: Elevación de comisuras labiales hacia arriba y hacia afuera (AU12) y contracción de mejillas/patas de gallo (AU6).
* **URL 1 (Joven Caucásica Sonriente - iStock)**:
  ```env
  TEST_IMAGE_URL=https://media.istockphoto.com/id/1143502198/es/foto/close-up-retrato-de-joven-mujer-muy-cauc%C3%A1sica-con-cara-feliz-y-hermosa-sonrisa-mirando.jpg?s=2048x2048&w=is&k=20&c=xlyMwftlnQdquzYJuzfR8Jb-AwEjRRo6zMGc6itW23k=
  ```
* **URL 2 (Hombre Sonriente - Dreamstime)**:
  ```env
  TEST_IMAGE_URL=https://thumbs.dreamstime.com/b/cara-sonriente-del-hombre-30386566.jpg
  ```

---

## 2. 😨 Miedo (Fear - AU 1 + AU 2 + AU 4 + AU 5 + AU 20)
* **Fisiología FACS**: Elevación drástica de cejas interiores hacia la frente ($\text{inner\_brow\_lift} > 0.25$, AU1+2+4), mirada fija desorbitada (AU5) y tensión labial lateral hacia las orejas (AU20).
* **URL 1 (Retrato Anciano Asustado - Depositphotos)**:
  ```env
  TEST_IMAGE_URL=https://st4.depositphotos.com/13318524/22528/i/1600/depositphotos_225287314-stock-photo-close-portrait-scared-frightened-old.jpg
  ```
* **URL 2 (Expresión de Pánico / Susto - Dreamstime)**:
  ```env
  TEST_IMAGE_URL=https://thumbs.dreamstime.com/b/cara-de-hombre-asustado-85834898.jpg
  ```

---

## 3. 😐 Neutral (Baseline / Reposo)
* **Fisiología FACS**: Músculos faciales relajados sin contracción de Action Units (cejas horizontales, comisuras en posición de reposo).
* **URL 1 (Rostro de Lena - OpenCV Standard Data)**:
  ```env
  TEST_IMAGE_URL=https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg
  ```

---

## 4. 😡 Ira (Anger - AU 4)
* **Fisiología FACS**: Fruncimiento y descenso de las cejas hacia los ojos en diagonal ($\text{brow\_slant} < -0.015$, AU4) con labios apretados o grito sin sonrisa.
* **URL 1 (Expresión de Enojo - Quo El Diario)**:
  ```env
  TEST_IMAGE_URL=https://quo.eldiario.es/wp-content/uploads/2019/10/quieres-parecer-mas-fuerte-pon-cara-de-enfadado.jpg.webp
  ```
* **URL 2 (Cara de Enfado Clásica - LMNeuquén)**:
  ```env
  TEST_IMAGE_URL=https://media.lmneuquen.com/p/410d97b89a573e44db378f26bd2ee1b7/adjuntos/195/imagenes/000/283/0000283880/las-cejas-la-nariz-y-la-boca-son-piezas-clave-la-cara-enojado.jpg
  ```

---

## 5. 🤢 Asco (Disgust - AU 9 + AU 10)
* **Fisiología FACS**: Arrugamiento del puente nasal y elevación marcada del labio superior hacia la nariz ($\text{corner\_elev} < -0.08$, AU9/10).
* **URL 1 (Gesto de Asco / Repulsión - BBC)**:
  ```env
  TEST_IMAGE_URL=https://ichef.bbci.co.uk/ace/ws/800/cpsprodpb/4361/production/_101894271_p066st0k.jpg.webp
  ```
* **URL 2 (Expresión de Repulsión - PyM)**:
  ```env
  TEST_IMAGE_URL=https://pymstatic.com/64783/conversions/frases-asco-wide_webp.webp
  ```

---

## 6. 😲 Sorpresa (Surprise - AU 1 + AU 2 + AU 26)
* **Fisiología FACS**: Apertura vertical de boca por caída relajada de la mandíbula ($\text{mouth\_h} > 0.04$, AU26) y cejas alzadas en arco alto sin arrugar el ceño.
* **URL 1 (Choque y Sorpresa Masculina - Dreamstime)**:
  ```env
  TEST_IMAGE_URL=https://thumbs.dreamstime.com/b/expresi%C3%B3n-de-la-sorpresa-y-del-choque-en-la-cara-masculina-18568388.jpg?w=576
  ```

---

## 7. 😢 Tristeza (Sadness - AU 15 + AU 1)
* **Fisiología FACS**: Caída de las comisuras labiales hacia abajo ($\text{corner\_elev} < -0.025$, AU15) y cejas interiores inclinadas hacia arriba en el centro (AU1).
* **URL 1 (Cara Triste / Decepción - iStock)**:
  ```env
  TEST_IMAGE_URL=https://media.istockphoto.com/id/1318482009/photo/sad-disappointed-young-man.jpg
  ```
* **URL 2 (Hombre Melancólico - Dreamstime)**:
  ```env
  TEST_IMAGE_URL=https://thumbs.dreamstime.com/b/hombre-triste-15203949.jpg
  ```
