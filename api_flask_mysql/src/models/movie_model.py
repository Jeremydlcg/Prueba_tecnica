from database.db import get_connection
from .entities.movie import Movie

class MovieModel():
    @classmethod
    def get_movie(self):
        try:
            connection=get_connection()
            movies=[]
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, title, duration, relased FROM movie ORDER title ASC")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    movie=Movie(row[0],row[1],row[2],row[3])
                    movies.append(movie)
            connection.close()
            return movies
        except Exception as ex:
            raise Exception(ex)