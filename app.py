from flask import Flask, render_template, request, redirect, url_for
from models.pila import PilaApoyos
from models.cola import ColaTarjetas

app = Flask(__name__)

# Instancias globales
pila = PilaApoyos()
cola = ColaTarjetas()

@app.route('/')
def index():
    return redirect(url_for('menu'))

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/cola', methods=['GET', 'POST'])
def vista_cola():
    mensaje = ''
    if request.method == 'POST':
        if 'agregar' in request.form:
            tarjeta = request.form.get('tarjeta')
            if tarjeta:
                cola.encolar(tarjeta)
                mensaje = 'Tarjeta agregada a la cola.'
        elif 'atender' in request.form:
            atendido = cola.desencolar()
            if atendido:
                mensaje = f'Se atendió a: {atendido}'
            else:
                mensaje = 'La cola está vacía.'
    return render_template('cola.html', cola=cola.mostrar(), mensaje=mensaje)

@app.route('/pila', methods=['GET', 'POST'])
def vista_pila():
    mensaje = ''
    if request.method == 'POST':
        if 'agregar' in request.form:
            apoyo = request.form.get('apoyo')
            if apoyo:
                pila.apilar(apoyo)
                mensaje = 'Apoyo agregado al historial.'
        elif 'deshacer' in request.form:
            deshecho = pila.desapilar()
            if deshecho:
                mensaje = f'Se deshizo el apoyo: {deshecho}'
            else:
                mensaje = 'El historial está vacío.'
    return render_template('pila.html', pila=pila.mostrar(), mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
