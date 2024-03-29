"""
    The main application file
"""

import os

from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Movie, Actor, db
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
            "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Methods",
            "GET, POST, PATCH, DELETE, OPTIONS"
        )

        return response

    @app.route("/movies", methods=["GET"])
    @requires_auth("get:movie")
    def get_movies(payload):
        """
            Get all movies

            Args:
                None

            Returns:
                jsonify: the response object
        """
        movies = Movie.query.all()

        if movies is None:
            abort(404, "No movies found.")

        movies = list(map(lambda movie: movie.format(), movies))

        return jsonify({
            "success": True,
            "movies": movies
        })

    @app.route("/movies", methods=["POST"])
    @requires_auth("post:movie")
    def post_movie(payload):
        """
            Post a movie

            Args:
                None

            Returns:
                jsonify: the response object
        """
        request_body = request.get_json()

        if request_body is None:
            abort(400, "Invalid request.")

        title = request_body.get("title", None)
        release_date = request_body.get("release_date", None)

        if title is None or release_date is None:
            abort(400, "Missing information.")

        movie = Movie(title=title, release_date=release_date)

        movie.insert()

        return jsonify({
            "success": True
        })

    @app.route("/movies/<int:movie_id>", methods=["PATCH"])
    @requires_auth("patch:movie")
    def update_movie(payload, movie_id):
        """
            Update a movie

            Args:
                movie_id: the id of the movie to be updated

            Returns:
                jsonify: the response object
        """

        movie_query = Movie.query.get(movie_id)

        if not movie_query:
            abort(404, "Movie not found.")

        request_body = request.get_json()

        title = request_body.get("title", None)
        release_date = request_body.get("release_date", None)

        if title:
            movie_query.title = title
        if release_date:
            movie_query.release_date = release_date

        movie_query.update()

        return jsonify({
            "success": True,
            "updated": movie_query.format()
        })

    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    @requires_auth("delete:movie")
    def delete_movie(payload, movie_id):
        """
            Delete a movie

            Args:
                movie_id: the id of the movie to be deleted

            Returns:
                jsonify: the response object
        """
        movie_query = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if movie_query is None:
            abort(404, f"Movie not found.")

        movie_query.delete()

        return jsonify({
            "success": True,
            "deleted": movie_id
        })

    @app.route("/actors", methods=["GET"])
    @requires_auth("get:actor")
    def get_actors(payload):
        """
            Get all actors

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

    @app.route("/actors", methods=["POST"])
    @requires_auth("post:actor")
    def post_actor(payload):
        """
            Post a actor

            Args:
                None

            Returns:
                jsonify: the response object
        """
        request_body = request.get_json()

        if request_body is None:
            abort(400)

        name = request_body.get("name", None)
        age = request_body.get("age", None)
        gender = request_body.get("gender", None)
        movie_id = request_body.get("movie_id", None)

        if name is None or age is None or gender is None or movie_id is None:
            abort(400, "Missing information.")

        actor = Actor(name=name, age=age, gender=gender, movie_id=movie_id)

        actor.insert()

        return jsonify({
            "success": True
        })

    @app.route("/actors/<int:actor_id>", methods=["PATCH"])
    @requires_auth("patch:actor")
    def update_actor(payload, actor_id):
        """
            Update an actor

            Args:
                actor_id: the id of the actor to be updated

            Returns:
                jsonify: the response object
        """

        actor_query = Actor.query.get(actor_id)

        if not actor_query:
            abort(404, "Actor not found.")

        body = request.get_json()
        name = body.get("name", None)
        age = body.get("age", None)
        gender = body.get("gender", None)
        movie_id = body.get("movie_id", None)

        if name:
            actor_query.name = name
        if age:
            actor_query.age = age
        if gender:
            actor_query.gender = gender
        if movie_id:
            actor_query.movie_id = movie_id

        try:
            actor_query.update()
        except BaseException:
            abort(400, "Invalid request.")

        return jsonify({
            "success": True,
            "updated": actor_query.format()
        })

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    @requires_auth("delete:actor")
    def delete_actor(payload, actor_id):
        """
            Delete an actor

            Args:
                actor_id: the id of the actor to be deleted

            Returns:
                jsonify: the response object
        """
        actor_query = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if actor_query is None:
            abort(404, "Actor not found.")

        actor_query.delete()

        return jsonify({
            "success": True,
            "deleted": actor_id
        })

    # @app.route("/authentification/url", methods=["GET"])
    # def get_authentification_url():
    #     """
    #         Get the authentification url

    #         Args:
    #             None

    #         Returns:
    #             jsonify: the response object
    #     """
    #     AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]
    #     API_AUDIENCE = os.environ["API_AUDIENCE"]
    #     AUTH0_CLIENT_ID = os.environ["AUTH0_CLIENT_ID"]
    #     AUTH0_CALLBACK_URL = os.environ["AUTH0_CALLBACK_URL"]

    #     url = f"https://{AUTH0_DOMAIN}/authorize?audience={API_AUDIENCE}&response_type=token&client_id={AUTH0_CLIENT_ID}&redirect_uri={AUTH0_CALLBACK_URL}"

    #     return jsonify({
    #         "auth_url": url
    #     })

    def set_error_message(error, default_message):
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
    def unprocessable_entity(error):
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
            "message": set_error_message(error, "Unprocessable entity."),
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
            "message": set_error_message(error, "Not found.")
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
            "message": set_error_message(error, "Bad request.")
        }), 400

    @app.errorhandler(AuthError)
    def auth_error(err):
        """
            Handle auth error

            Args:
                auth_error: the error object

            Returns:
                jsonify: the response object
        """
        return jsonify({
            "success": False,
            "error": err.status_code,
            "message": err.error["description"]
        }), err.status_code

    return app


APP = create_app()

with APP.app_context():
    db.create_all()

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=8080, debug=True)
