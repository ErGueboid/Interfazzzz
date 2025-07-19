# Sistema de Apoyos (Pilas y Colas)

**Nombre:** [Tu Nombre Aquí]
**Grupo y materia:** [Tu Grupo] - [Materia]

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
3. Abre tu navegador en [http://localhost:5000](http://localhost:5000)

## Ejemplo de uso
- Ve a "Entregar Tarjetas (Cola)" para agregar personas a la cola y atenderlas.
- Ve a "Historial de Apoyos (Pila)" para agregar apoyos y deshacer el último.

---
