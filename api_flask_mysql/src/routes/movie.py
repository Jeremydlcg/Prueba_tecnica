from flask import Blueprint, jsonify

from models.movie_model import MovieModel

main=Blueprint('movie_blueprint',__name__)

@main.route('/')
def get_movies():
    try:
        movies=MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500