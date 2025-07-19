# Sistema de Apoyos (Pilas y Colas)

**Nombre:** Victor Daniel Gonzalez Flores   
**Grupo y materia:** 1 - Estructura de Datos

## Descripción
Sistema web sencillo en Python usando Flask para gestionar:
- **Cola:** Entrega de tarjetas de apoyo (personas esperando su tarjeta).
- **Pila:** Historial de apoyos recibidos (simula deshacer apoyos).

## Estructura del proyecto
```
menuflask/
├── app.py
├── README.md
├── models/
│   ├── pila.py
│   └── cola.py
├── templates/
│   ├── menu.html
│   ├── cola.html
│   └── pila.html
```

## Instrucciones para instalar dependencias y ejecutar
1. Instala Flask:
   ```bash
   pip install flask
   ```
2. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

## Ejemplo de uso
- Ve a "Entregar Tarjetas (Cola)" para agregar personas a la cola y atenderlas.
- Ve a "Historial de Apoyos (Pila)" para agregar apoyos y deshacer el último.

