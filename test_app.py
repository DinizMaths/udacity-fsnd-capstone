"""
    File for testing the app
"""

import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor


class CapstoneTestCase(unittest.TestCase):
    """
        This class represents the capstone test case
    """
    def setUp(self):
        """
            Define test variables and initialize app
        """
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres:///{}".format(self.database_name)

        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()

            self.db.init_app(self.app)
            self.db.create_all()

        self.movie = {
            "title": "ABC",
            "release_date": "2020-11-02"
        }

        self.actor = {
            "name": "Roger",
            "age": 30,
            "gender": 'M',
            "movie_id": 1
        }

        with open("auth_config.json", "r") as f:
            self.auth = json.loads(f.read())

        assistant_jwt = self.auth["roles"]["Casting Assistant"]["jwt_token"]
        director_jwt = self.auth["roles"]["Casting Director"]["jwt_token"]
        producer_jwt = self.auth["roles"]["Executive Producer"]["jwt_token"]

        self.auth_headers = {
            "Casting Assistant": f"Bearer {assistant_jwt}",
            "Casting Director": f"Bearer {director_jwt}",
            "Executive Producer": f"Bearer {producer_jwt}"
        }

    def tearDown(self):
        """
            Executed after reach test
        """
        pass

    def test_get_movies(self):
        """
            Test getting movies
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get('/movies', headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(type(data["movies"]), type([]))

    def test_get_actors(self):
        """
            Test getting actors
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get("/actors", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(type(data["actors"]), type([]))

    def test_get_actors_by_director(self):
        """
            Test getting actors by director
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client().get("/actors", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(type(data["actors"]), type([]))

    def test_get_actor_fail_401(self):
        """
            Test getting actors fail 401
        """
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])
        self.assertEqual(type(data["message"]), type(""))

    def test_create_movies(self):
        """
            Test creating movies
        """
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().post(f"/movies", json=self.movie, headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_create_movies_fail_400(self):
        """
            Test creating movies fail 400
        """
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        movie_fail = {"title": "Movie"}
        res = self.client().post(f"/movies", json=movie_fail, headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Missing field for Movie")

    def test_create_movies_fail_403(self):
        """
            Test creating movies fail 403
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        movie_fail = {"title": "Movie"}
        res = self.client().post(f"/movies", json=movie_fail, headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])

    def test_create_actors(self):
        """
            Test creating actors
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client().post(f"/actors", json=self.actor, headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_create_actors_fail_400(self):
        """
            Test creating actors fail 400
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        actor_fail = {"name": "Actor"}
        res = self.client().post(f"/actors", json=actor_fail, headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Missing field for Actor")

    def test_create_actors_fail_403(self):
        """
            Test creating actors fail 403
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        actor_fail = {"name": "Actor"}
        res = self.client().post(f"/actors", json=actor_fail, headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])

    def test_delete_movie(self):
        """
            Test deleting movies
        """
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        delete_id_movie = 1
        res = self.client().delete(f"/movies/{delete_id_movie}", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["deleted"], delete_id_movie)

        res = self.client().get("/movies", headers=header_obj)
        movie_data = json.loads(res.data)

        found_deleted = False

        for movie in movie_data["movies"]:
            if movie["id"] == delete_id_movie:
                found_deleted = True

                break

        self.assertFalse(found_deleted)

    def test_delete_movie_fail_404(self):
        """
            Test deleting movies fail 404
        """
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        m_id = 100
        res = self.client().delete(f"/movies/{m_id}", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])

    def test_delete_movie_fail_403(self):
        """
            Test deleting movies fail 403
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        m_id = 3
        res = self.client().delete(f"/movies/{m_id}", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])

    def test_delete_actor(self):
        """
            Test deleting actors
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        delete_id_actor = 1
        res = self.client().delete(f"/actors/{delete_id_actor}", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["deleted"], delete_id_actor)

        res = self.client().get("/actors", headers=header_obj)
        actors_data = json.loads(res.data)

        found_deleted = False

        for actor in actors_data["actors"]:
            if actor["id"] == delete_id_actor:
                found_deleted = True
                break

        self.assertFalse(found_deleted)

    def test_delete_actor_fail_404(self):
        """
            Test deleting actors fail 404
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        actor_id = -100
        res = self.client().delete(f"/actors/{actor_id}", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])

    def test_delete_actor_fail_403(self):
        """
            Test deleting actors fail 403
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        actor_id = 100
        res = self.client().delete(f"/actors/{actor_id}", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])

    def test_update_movie_casting_director(self):
        """
            Test updating movies
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        update_id_movie = 2
        new_title = "Avatar"
        res = self.client().patch(f"/movies/{update_id_movie}", json={
                "title": new_title
            }, headers=header_obj
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["updated"]["id"], update_id_movie)
        self.assertEqual(data["updated"]["title"], new_title)

    def test_update_movie_executive_producer(self):
        """
            Test updating movies
        """
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        update_id_movie = 2
        new_title = "Avatar"
        res = self.client().patch(
            f"/movies/{update_id_movie}",
            json={
                "title": new_title
            },headers=header_obj
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["updated"]["id"], update_id_movie)
        self.assertEqual(data["updated"]["title"], new_title)

    def test_update_movie_fail_404(self):
        """
            Test updating movies fail 404
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        update_id_movie = -100
        res = self.client().patch(
            f"/movies/{update_id_movie}",
            headers=header_obj
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])

    def test_update_actor_casting_director(self):
        """
            Test updating actors
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        update_id_actor = 2
        new_name = "Tom Hanks"
        new_age = 54
        res = self.client().patch(
            f"/actors/{update_id_actor}",
            json={
                "name": new_name,
                "age": new_age
            },
            headers=header_obj
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["updated"]["id"], update_id_actor)
        self.assertEqual(data["updated"]["name"], new_name)
        self.assertEqual(data["updated"]["age"], new_age)

    def test_update_actor_fail_404(self):
        """
            Test updating actors fail 404
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        update_id_actor = 100
        res = self.client().patch(
            f"/actors/{update_id_actor}",
            headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])

    def test_update_actor_fail_403(self):
        """
            Test updating actors fail 403
        """
        header_obj = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        update_id_actor = 100
        res = self.client().patch(
            f"/actors/{update_id_actor}",
            headers=header_obj
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])


if __name__ == "__main__":
    unittest.main()