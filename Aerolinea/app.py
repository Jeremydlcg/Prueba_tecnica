from flask import Flask, request, jsonify, render_template, url_for
from flask_migrate import Migrate
from models import Aviones
from database import db
from forms import AvionForm
from werkzeug.utils import redirect

"""Configuracion del proyecto"""
app = Flask(__name__)

#Configuración de la bd
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'aerolinea_nelmix'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

# database_config = Developmentconfig()

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

app.config['SECRET_KEY']='password'

# @app.route('/aviones')

        

    

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    #aviones = Aviones.query.all() #para traer la lista de los aviones
    aviones = Aviones.query.order_by('id')
    total_aviones = Aviones.query.count() #para contar los aviones
    app.logger.debug(f'Listado Aviones: {aviones}')
    app.logger.debug(f'Total Aviones: {total_aviones}')
    return render_template('index.html', aviones = aviones, total_aviones = total_aviones)

@app.route('/ver/<int:id>')
def ver_detalle(id):
    avion = Aviones.query.get_or_404(id)
    app.logger.debug(f'Ver Avion: {avion}')
    return render_template('detail.html', avion = avion)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    avion = Aviones()
    avionForm = AvionForm(obj=avion)
    if request.method == 'POST':
        if avionForm.validate_on_submit():
            avionForm.populate_obj(avion)
            app.logger.debug(f'Avion a insertar: {avion}')
            
            db.session.add(avion) 
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregar.html', forma = avionForm)

@app.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    avion = Aviones.query.get_or_404(id)
    avionForma = AvionForm(obj=avion)
    if request.method == 'POST':
        if avionForma.validate_on_submit():
            avionForma.populate_obj(avion)
            app.logger.debug(f'Avion a Actualizar: {avion}')
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html',forma = avionForma)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    avion = Aviones.query.get_or_404(id)
    app.logger.debug(f'Avion a Eliminar: {avion}')
    db.session.delete(avion)
    db.session.commit()
    return redirect(url_for('inicio'))

    
    
    # try:
    #     cursor = conexion.cursor()
    #     sql = 'SELECT * FROM usuario'
    #     cursor.execute(sql)
    #     datos = cursor.fetchall()
    #     print(datos)
    #     return "Aviones Listados!"
    
    # except Exception as e:
    #     print("Error:", e)
    #     return "Error al obtener los aviones",e


# def paginaNoEncontrada(error):
#     return "<h1>Pagina no encontrada</h1>"


# if __name__=="__main__":
#     app.config.from_object(config['development'])
#     app.register_error_handler(404,paginaNoEncontrada)
#     app.run()
