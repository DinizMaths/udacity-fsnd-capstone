"""
  File for database models
"""

import os

from sqlalchemy import ForeignKey, Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


DATABASE_PATH = os.environ["DATABASE_URL"]
db = SQLAlchemy()


def setup_db(app):
    """
        Setup the database

        Args:
            app: The app

        Returns:
            None
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


class Movie(db.Model):
    """
        Table for movies

        Attributes:
            id: The id of the movie
            title: The title of the movie
            release_date: The release date of the movie
            actors: The actors in the movie
    """
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(DateTime)
    actors = relationship("Actor", backref="movie", lazy=True)

    def __init__(self, title, release_date):
        """
            Constructor for Movie

            Args:
                title: The title of the movie
                release_date: The release date of the movie

            Returns:
                None
        """
        self.title = title
        self.release_date = release_date

    def insert(self):
        """
            Insert the movie into the database

            Args:
                None

            Returns:
                None
        """
        db.session.add(self)
        db.session.commit()

    def update(self):
        """
            Update the movie in the database

            Args:
                None

            Returns:
                None
        """
        db.session.commit()

    def delete(self):
        """
            Delete the movie from the database

            Args:
                None

            Returns:
                None
        """
        db.session.delete(self)
        db.session.commit()

    def format(self):
        """
            Format the movie

            Args:
                None

            Returns:
                dict: The formatted movie
        """
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
            "actors": list(map(lambda actor: actor.format(), self.actors))
        }

class Actor(db.Model):
    """
        Table for actors

        Attributes:
            id: The id of the actor
            name: The name of the actor
            age: The age of the
    """
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=True)

    def __init__(self, name, age, gender, movie_id):
        """
            Constructor for Actor

            Args:
                name: The name of the actor
                age: The age of the actor
                gender: The gender of the actor
                movie_id: The id of the movie
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.movie_id = movie_id

    def insert(self):
        """
            Insert the actor into the database

            Args:
                None

            Returns:
                None
        """
        db.session.add(self)
        db.session.commit()

    def update(self):
        """
            Update the actor in the database

            Args:
                None

            Returns:
                None
        """
        db.session.commit()

    def delete(self):
        """
            Delete the actor from the database

            Args:
                None

            Returns:
                None
        """
        db.session.delete(self)
        db.session.commit()

    def format(self):
        """
            Format the actor

            Args:
                None

            Returns:
                dict: The formatted actor
        """
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "movie_id": self.movie_id
        }
