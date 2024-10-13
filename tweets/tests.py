from rest_framework.test import APITestCase
from .models import Tweet
from users.models import User


class TestTweets(APITestCase):
    PAYLOAD = "Test Tweet"
    URL = "/api/v1/tweets/"

    def setUp(self):
        user = User.objects.create(username="test")
        user.set_password("test")
        user.save()
        self.user = user

        Tweet.objects.create(
            user=user,
            payload=self.PAYLOAD,
        )

    def test_get(self):
        response = self.client.get(self.URL)
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )
        self.assertIsInstance(
            data,
            list,
            "data type isn't list",
        )
        self.assertEqual(
            len(data),
            1,
            "length of data isn't 1",
        )

        self.assertEqual(
            data[0]["payload"],
            self.PAYLOAD,
            "payload isn't 'Test Tweet",
        )

    def test_post(self):
        new_payload = "New Tweet"
        response = self.client.post(
            self.URL,
            data={
                "payload": new_payload,
            },
        )
        self.assertEqual(response.status_code, 403, "Test 403 status")
        self.client.force_login(self.user)
        response = self.client.post(
            self.URL,
            data={
                "payload": new_payload,
            },
        )
        self.assertEqual(
            response.status_code,
            200,
            "Test 200 status",
        )
        data = response.json()

        self.assertEqual(
            data["payload"],
            new_payload,
            "Test payload equal data",
        )
        self.assertIn(
            "payload",
            data,
            "Test payload in data",
        )


class TestTweet(APITestCase):
    PAYLOAD = "Test Tweet"

    def setUp(self):
        user = User.objects.create(username="test")
        user.set_password("test")
        user.save()
        self.user = user

        Tweet.objects.create(
            user=user,
            payload=self.PAYLOAD,
        )

    def test_tweet_not_found(self):
        response = self.client.get("/api/v1/tweets/2")
        self.assertEqual(response.status_code, 404)

    def test_get(self):
        response = self.client.get("/api/v1/tweets/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data["payload"],
            self.PAYLOAD,
        )

    def test_put(self):
        updated_tweet_payload = "Updated Tweet 1"
        response = self.client.put(
            "/api/v1/tweets/1",
            data={
                "payload": updated_tweet_payload,
            },
        )
        self.assertEqual(response.status_code, 403)

        self.client.force_login(self.user)
        response = self.client.put(
            "/api/v1/tweets/1",
            data={
                "payload": updated_tweet_payload,
            },
        )

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )

        data = response.json()
        self.assertEqual(
            data["payload"],
            updated_tweet_payload,
        )
        updated_tweet_payload = "Updated Tweet 2"
        response = self.client.put(
            "/api/v1/tweets/1",
            data={
                "payload": updated_tweet_payload,
            },
        )
        data = response.json()
        self.assertEqual(
            data["payload"],
            updated_tweet_payload,
        )

    def test_delete(self):

        response = self.client.delete("/api/v1/tweets/1")
        self.assertEqual(response.status_code, 403)
        self.client.force_login(self.user)
        response = self.client.delete("/api/v1/tweets/1")
        self.assertEqual(response.status_code, 204)
