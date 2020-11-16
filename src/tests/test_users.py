import unittest
from main import create_app, db
from models.Users import Users

class TestUsers(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()
        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()




    def test_users_index(self):
        response= self.client.get("/users/")

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_book_create(self):
        response = self.client.post("/users/", json=  {
            "account_active": "False",
            "fname": "Test Fname",
            "lname": "Test Lname",
            "username": "Test_username"
            })

        data = response.get_json()

        #self.assertEqual(response.status_code, 200)
        self.assertTrue(bool(response.status_code >= 200 and response.status_code < 300))
        self.assertIsInstance(data, dict)
        self.assertTrue(bool("userid" in data.keys()))

        user = Users.query.get(data["userid"])
        self.assertIsNotNone(user)

    # def test_user_update(self):
    #     response = self.client.post("/users/", json=  {
    #         "account_active": "False",
    #         "email": "Test Email2",
    #         "fname": "Test Fname2",
    #         "lname": "Test Lname2",
    #         "profile_pic": "Test Pic2",
    #         "username": "Test_username2",
    #         "userpass": "Test_Pass2",
    #         })

        

    #     responseput = self.client.put("/users/Test_username2", json=  {
    #         "account_active": "False",
    #         "email": "Updated",
    #         "fname": "Updated",
    #         "lname": "Updated",
    #         "profile_pic": "Test Pic2",
    #         "username": "Updated",
    #         "userpass": "Test_Pass2",
    #         }) 

    #     data = responseput.get_json()

    #     #self.assertEqual(response.status_code, 200)
    #     self.assertTrue(bool(response.status_code >= 200 and response.status_code < 300))
    #     self.assertIsInstance(data, dict)
    #     self.assertTrue(bool("userid" in data.keys()))
    #     self.assertEqual(data["username"] == username)

    #     user = Users.query.get(data["userid"])
    #     self.assertIsNotNone(user)

    def test_book_delete(self):
        user = Users.query.first()

        response = self.client.delete(f"/users/{user.userid}")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        user = Users.query.get(user.userid)
        self.assertIsNone(user)