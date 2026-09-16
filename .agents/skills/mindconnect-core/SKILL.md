---
name: mindconnect-core
description: >-
  Habilidad principal del proyecto MindConnect (AventoAI x Breaklinestudio).
  Contiene los estatutos del acuerdo 50/50, derechos de autoría de IP (10% Guillermo Paúl),
  bolsa de participación operativa (40%), arquitectura del servicio de IA de microexpresiones post-sesión WebRTC,
  reglas del chat restringido con filtro anti-bypass, Historias de Usuario (HU-01 a HU-05) y Casos de Uso (CU-01 a CU-03).
  Usar al desarrollar módulos, APIs o consultar reglas de negocio del ecosistema MindConnect.
---

# MindConnect Core - Guía de Proyecto & Reglas de Negocio

Esta habilidad define los estándares técnicos, legales, operativos y arquitectónicos del ecosistema **MindConnect**, desarrollado en alianza entre **AventoAI** y **Breaklinestudio**.

---

## 1. Estatutos de Alianza y Modelo Económico (Acuerdos Internos)

* **Alianza Externa (50/50)**:
  * **50% AventoAI (Liderado por José Guillermo Paúl Díaz)**: Frontend (React Native, React/Next.js), Servicio de IA en Python (FastAPI, RAG, triaje, microexpresiones), UI/UX, animaciones 2D/3D.
  * **50% Breaklinestudio (Liderado por Johlver José Pardo)**: Backend principal (Java Spring Boot, arquitectura DDD, PostgreSQL, autenticación OTP, Docker/Sandbox).
* **Distribución Interna AventoAI (sobre su 50%)**:
  * **10% Reconocimiento de Autoría (Fijo e intocable)**: Perteneciente a José Guillermo Paúl Díaz a título personal como ideador original del proyecto.
  * **40% Bolsa Operativa de AventoAI (80% del 50%)**: Distribuido proporcionalmente entre los integrantes activos según horas registradas en Plane/Jira y aportes técnicos.

---

## 2. Arquitectura del Módulo de Microexpresiones con IA (CU-03)

1. **Captura y Grabación**:
   * Las videoconsultas se realizan mediante **WebRTC nativo / SFU**.
   * El video de la sesión de 50 min se graba localmente de forma cifrada y se sube a almacenamiento seguro **Amazon S3**.
2. **Procesamiento Asíncrono Post-Sesión**:
   * Al finalizar la cita (`COMPLETADA`), Spring Boot notifica al Microservicio de IA en Python.
   * La red neuronal convolucional (CNN) procesa el video **fotograma a fotograma (30 FPS)** analizando cambios sutiles (40ms-200ms) basándose en las **7 emociones universales de Ekman**.
3. **Entregable para el Especialista**:
   * Generación automática de la entidad `AnalisisMicroexpresion` con la línea de tiempo emocional y alertas clínicas de picos de ansiedad o estrés.

---

## 3. Reglas del Chat Restringido y Filtro Anti-Bypass (CU-02)

* El chat entre paciente y especialista solo se activa cuando la cita está en estado `CONFIRMADA_PAGADA`.
* **Filtro Anti-Bypass (`AntiBypassFilterService`)**:
  * El backend escanea el texto con expresiones regulares (Regex).
  * Si detecta números telefónicos (10+ dígitos), correos electrónicos (`@domain.com`), enlaces externos (`wa.me`, `instagram.com`) o cuentas bancarias, el texto es enmascarado automáticamente:
    ```
    *** [INFORMACIÓN DE CONTACTO BLOQUEADA POR POLÍTICA DE SEGURIDAD] ***
    ```

---

## 4. Referencias Técnicas Detalladas

Para consultar los documentos completos, accede a las referencias adjuntas:

* 📄 **[Acuerdos Internos y Propiedad Intelectual (IP)](./references/internal_agreements_and_ip.md)**
* 📄 **[Historias de Usuario (HUs) y Casos de Uso (CUs)](./references/user_stories_and_use_cases.md)**

---

## 5. Verificación de Entregables

Al desarrollar componentes de MindConnect:
1. Verificar que todo endpoint de chat pase por el filtro anti-bypass.
2. Confirmar que la comisión del 20% de la plataforma sea calculada en Spring Boot.
3. Asegurar que el informe de microexpresiones sea estrictamente accesible por el especialista asignado.
