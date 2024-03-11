"""
    File for testing the app
"""


import os
import unittest
import json
from app import APP
from models import setup_db, Movie, Actor

class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_movie = {
            "title": "Test Movie",
            "release_date": "2023-01-01"
        }

        self.new_actor = {
            "name": "Test Actor",
            "age": 30,
            "gender": "Male",
            "movie_id": 1
        }

        self.casting_assistant_token = os.environ.get("CASTING_ASSISTANT_TOKEN")
        self.casting_director_token = os.environ.get("CASTING_DIRECTOR_TOKEN")
        self.executive_producer_token = os.environ.get("EXECUTIVE_PRODUCER_TOKEN")

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_movies(self):
        """Test get movies endpoint"""
        response = self.client().get('/movies', headers={"Authorization": "Bearer " + self.casting_assistant_token})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movies']))

    def test_create_movie(self):
        """Test create movie endpoint"""
        response = self.client().post('/movies', headers={"Authorization": "Bearer " + self.executive_producer_token}, json=self.new_movie)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_update_movie(self):
        """Test update movie endpoint"""
        response = self.client().patch('/movies/1', headers={"Authorization": "Bearer " + self.executive_producer_token}, json={"title": "Updated Title"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_delete_movie(self):
        """Test delete movie endpoint"""
        response = self.client().delete('/movies/1', headers={"Authorization": "Bearer " + self.executive_producer_token})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_actors(self):
        """Test get actors endpoint"""
        response = self.client().get('/actors', headers={"Authorization": "Bearer " + self.casting_assistant_token})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']))

    def test_create_actor(self):
        """Test create actor endpoint"""
        response = self.client().post('/actors', headers={"Authorization": "Bearer " + self.casting_director_token}, json=self.new_actor)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_update_actor(self):
        """Test update actor endpoint"""
        response = self.client().patch('/actors/1', headers={"Authorization": "Bearer " + self.casting_director_token}, json={"name": "Updated Name"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_delete_actor(self):
        """Test delete actor endpoint"""
        response = self.client().delete('/actors/1', headers={"Authorization": "Bearer " + self.casting_director_token})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

if __name__ == "__main__":
    unittest.main()
