from flask import Flask
from config import config
from flask_mysqldb import MySQL
from routes import movie

app=Flask(__name__)

conexion=MySQL(app)

# @app.route('/cursos')
# def listar_cursos():
#     try:
#         cursor=conexion.connection.cursor()
#         sql="SELECT codigo, nombre, credito FROM curso"
#         cursor.execute(sql)
#         datos=cursor.fetchall()
#         print(datos)
#         return "Cursos Listados!"
#     except Exception as ex:
#         return "ERROR"
    
def page_not_found(error):
    return "<h1>La pagina no pudo ser encontrada...</h1>"


if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    #Blrptiny
    app.register_blueprint(movie.main, urlprefix='/api/movies')
    
    app.register_error_handler(404, page_not_found)
    app.run()