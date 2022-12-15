from flask import Flask, render_template

app = Flask(__name__) #inicializar flask en app

@app.route('/hola') # definimos la ruta donde vamos a ejecutar la funcion
def hola_mundo():
    return 'hola mundo flask'

# inicializar el servidor de flask
    # en mac: export FLASK_APP=hello.py

# ejecutar el servidor:
    # flask --app hello run
# comando para actualizar el servidor por cambio de codigo en tiempo real
    # flask --app hello --debug run
# comando especial para lanzar el servidor en un puerto diferente
    # flask --app hello run -p 5001
#



@app.route('/adios')
def despedida():
    return 'Hasta pronto pepe!!!'

# ejemplo para enviar parametros en las rutas

@app.route('/nombre/<nombre>')
def name(nombre):
    return f'tu nombre es {nombre}'

@app.route('/numero/<n>')
def cuadrado(n):
    num = int(n)*int(n)
    return f'el cuadrado del numero {n} es {num}'

#ejercicio realizaruna ruta que dinamicamente pueda solicitar realizar
#operaciones de suma , resta , multiplicacion y division

@app.route('/operaciones/<float:n1>/<float:n2>/<ope>')
def calculadora(n1,n2,ope):
    if ope == 'suma':
        return render_template ('hola.html', resultado = f'La suma es {n1+n2}')

    elif ope == 'resta':
        return render_template ('hola.html', resultado = f'La resta es {n1-n2}')
    
    elif ope == 'multiplicacion':
        return render_template ('hola.html', resultado = f'La multiplicacion es {n1*n2}')
    
    elif ope == 'division':
        return render_template ('hola.html', resultado = f'La division es {n1/n2}')
    
# ejemplo de devolver un Html por flask

@app.route('/primerhtml/<nombre>')
def callhtml(nombre):
    return render_template('hola.html')
    
