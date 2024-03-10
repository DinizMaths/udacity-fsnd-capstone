"""
    The main application file
"""

from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth


def create_app():
    """
        Create and configure the app

        Args:
            None

        Returns:
            app: the created app
    """
    app = Flask(__name__)

    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        """
            Set Access-Control-Allow

            Args:
                response: the response object

            Returns:
                response: the modified response object
        """
        response.headers.add(
            "Access-Control-Allow-Headers",
            "Content-Type,Authorization, true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods",
            "GET, PUT, POST, DELETE, OPTIONS"
        )

        return response

    @app.route("/movies", methods=["GET"])
    @requires_auth("view:movies")
    def retrieve_movies():
        """
            Retrieve all movies

            Args:
                None

            Returns:
                jsonify: the response object
        """
        movies = Movie.query.all()
        movies = list(map(lambda movie: movie.format(), movies))

        return jsonify({
            "success": True,
            "movies": movies
        })

    @app.route("/actors", methods=["GET"])
    @requires_auth("view:actors")
    def retrieve_actors():
        """
            Retrieve all actors

            Args:
                None

            Returns:
                jsonify: the response object
        """
        actors = Actor.query.all()
        actors = list(map(lambda actor: actor.format(), actors))

        return jsonify({
            "success": True,
            "actors": actors
        })

    @app.route("/movies", methods=["POST"])
    @requires_auth("post:movies")
    def create_movie():
        """
            Create a new movie

            Args:
                None

            Returns:
                jsonify: the response object
        """
        body = request.get_json()

        if body is None:
            abort(400)

        title = body.get("title", None)
        release_date = body.get("release_date", None)

        if title is None or release_date is None:
            abort(400, "Missing field for Movie")

        movie = Movie(title=title, release_date=release_date)

        movie.insert()

        return jsonify({
            "success": True
        })

    @app.route("/actors", methods=["POST"])
    @requires_auth("post:actors")
    def create_actor():
        """
            Create a new actor

            Args:
                None

            Returns:
                jsonify: the response object
        """
        body = request.get_json()

        if body is None:
            abort(400)

        name = body.get("name", None)
        age = body.get("age", None)
        gender = body.get("gender", None)
        movie_id = body.get("movie_id", None)

        if name is None or age is None or gender is None or movie_id is None:
            abort(400, "Missing field for Actor")

        actor = Actor(name=name, age=age, gender=gender, movie_id=movie_id)

        actor.insert()

        return jsonify({
            "success": True
        })

    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    @requires_auth("delete:movies")
    def delete_movie(movie_id):
        """
            Delete a movie

            Args:
                movie_id: the id of the movie to be deleted

            Returns:
                jsonify: the response object
        """
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if movie is None:
            abort(404, "No movie with given id " + str(movie_id) + " is found")

        movie.delete()

        return jsonify({
            "success": True,
            "deleted": movie_id
        })

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    @requires_auth("delete:actors")
    def delete_actor(actor_id):
        """
            Delete an actor

            Args:
                actor_id: the id of the actor to be deleted

            Returns:
                jsonify: the response object
        """
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if actor is None:
            abort(404, "No actor with given id " + str(actor_id) + " is found")

        actor.delete()

        return jsonify({
            "success": True,
            "deleted": actor_id
        })

    @app.route("/movies/<int:movie_id>", methods=["PATCH"])
    @requires_auth("update:movies")
    def update_movie(movie_id):
        """
            Update a movie

            Args:
                movie_id: the id of the movie to be updated

            Returns:
                jsonify: the response object
        """

        updated_movie = Movie.query.get(movie_id)

        if not updated_movie:
            abort(
                404,
                "Movie with id: " +
                str(movie_id) +
                " could not be found.")

        body = request.get_json()

        title = body.get("title", None)
        release_date = body.get("release_date", None)

        if title:
            updated_movie.title = title
        if release_date:
            updated_movie.release_date = release_date

        updated_movie.update()

        return jsonify({
            "success": True,
            "updated": updated_movie.format()
        })

    @app.route("/actors/<int:actor_id>", methods=["PATCH"])
    @requires_auth("update:actors")
    def update_actor(actor_id):
        """
            Update an actor

            Args:
                actor_id: the id of the actor to be updated

            Returns:
                jsonify: the response object
        """

        updated_actor = Actor.query.get(actor_id)

        if not updated_actor:
            abort(404, "Actor with id: " + str(actor_id) + " could not be found.")

        body = request.get_json()
        name = body.get("name", None)
        age = body.get("age", None)
        gender = body.get("gender", None)
        movie_id = body.get("movie_id", None)

        if name:
            updated_actor.name = name
        if age:
            updated_actor.age = age
        if gender:
            updated_actor.gender = gender
        if movie_id:
            updated_actor.movie_id = movie_id

        try:
            updated_actor.update()
        except BaseException:
            abort(400, "Bad formatted request due to nonexistent movie id" + str(movie_id))

        return jsonify({
            "success": True,
            "updated": updated_actor.format()
        })

    def get_error_message(error, default_message):
        """
            Get the error message

            Args:
                error: the error object
                default_message: the default message

            Returns:
                str: the error message
        """
        try:
            return error.description
        except BaseException:
            return default_message

    @app.errorhandler(422)
    def unprocessable(error):
        """
            Handle unprocessable error

            Args:
                error: the error object

            Returns:
                jsonify: the response object
        """
        return jsonify({
            "success": False,
            "error": 422,
            "message": get_error_message(error, "unprocessable"),
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        """
            Handle not found error

            Args:
                error: the error object

            Returns:
                jsonify: the response object
        """
        return jsonify({
            "success": False,
            "error": 404,
            "message": get_error_message(error, "resource not found")
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        """
            Handle bad request error

            Args:
                error: the error object

            Returns:
                jsonify: the response object
        """
        return jsonify({
            "success": False,
            "error": 400,
            "message": get_error_message(error, "bad request")
        }), 400

    @app.errorhandler(AuthError)
    def auth_error(auth_error):
        """
            Handle auth error

            Args:
                auth_error: the error object

            Returns:
                jsonify: the response object
        """
        return jsonify({
            "success": False,
            "error": auth_error.status_code,
            "message": auth_error.error["description"]
        }), auth_error.status_code

    return app


APP = create_app()

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=8080, debug=True)
