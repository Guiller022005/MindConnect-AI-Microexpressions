# Historias de Usuario y Casos de Uso - Ecosistema MindConnect

## 1. Historias de Usuario (Backlog)

### Módulo de Autenticación y Menores
* **HU-01: Registro Diferenciado por Edad**:
  * Dado un usuario entre 12 y 17 años, el sistema solicita el correo del acudiente y marca la cuenta como `PENDIENTE_AUTORIZACION`.
* **HU-02: Autorización de Acudiente**:
  * El acudiente firma el consentimiento informado vía correo/SMS para activar la cuenta del menor.

### Módulo de Citas y Pagos
* **HU-03: Agendamiento y Pago en Línea**:
  * El sistema calcula `Monto Total = Tarifa Especialista + 20% Comisión`. Cambia estado a `CONFIRMADA_PAGADA`.
* **HU-04: Chat Restringido con Filtro Anti-Bypass**:
  * El chat solo opera durante la ventana de tiempo de la cita. Enmascara datos sensibles de contacto en tiempo real.
* **HU-05: Videoconsulta WebRTC**:
  * Habilita la sala de videollamada cifrada 5 min antes de la consulta.

---

## 2. Casos de Uso Formale

### **CU-01: Flujo Completo de Reserva, Pago y Cancelación de Cita**
* **Actor Principal**: Usuario Final.
* **Precondiciones**: Cuenta activa y consentimientos aceptados.
* **Flujo**: Selección de horario -> Pago en Pasarela -> Cambio a `CONFIRMADA_PAGADA` -> Desglose 80%/20% -> Habilitación de chat.
* **Cancelación**:
  * >24h antes: Devuelta del 100% (`CANCELADA_REEMBOLSADA`).
  * <2h antes / No-show: Penalización 100% (`NO_ASISTIO_USUARIO`), saldo pagado al especialista.

### **CU-02: Envío de Mensajes por Chat con Filtro Anti-Bypass**
* **Servicio Backend**: `AntiBypassFilterService`.
* **Regex aplicados**: Números telefónicos (10+ dígitos), emails (`@domain.com`), enlaces externos (`wa.me`, `instagram.com`), cuentas/ALIAS bancarios.
* **Resultado**: Reemplazo por `*** [INFORMACION DE CONTACTO BLOQUEADA POR POLITICA DE SEGURIDAD] ***`.

### **CU-03: Análisis Post-Sesión de Microexpresiones por IA**
* **Infraestructura**: WebRTC Client -> Grabación local cifrada -> Carga a S3 -> Microservicio Python (`AnalisisMicroexpresion`).
* **Algoritmo**: CNN en TensorFlow procesando 30 FPS. Clasificación Ekman (7 emociones).
* **Entregable**: Dashboard privado con la línea de tiempo emocional y mapa de alertas de estrés para el especialista.
