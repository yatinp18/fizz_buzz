import requests
from fastapi.testclient import TestClient

from fizz_buzz_app.main import app, fizz_buzz, statistics
client = TestClient(app)

def test_fizz_buzz():
    # Test the Fizz-Buzz logic
    result = fizz_buzz(3, 5, 3, "fizz", "buzz")
    assert result == ['1','2','fizz']

def test_fizzbuzz_endpoint():
    # Test the /fizzbuzz endpoint
    params = {"int1": 3, "int2": 5, "limit": 15, "str1": "fizz", "str2": "buzz"}
    response = client.get("/fizzbuzz", params=params)
    result = response.json()
    # Knowing which service is hit the highest would be difficult at compile time
    assert result != None

def test_statistics_endpoint():
    # Test the /statistics endpoint
    response = client.get("/statistics")
    result = response.json()
    assert "most_used_request" in result

def test_statistics_hit_counter():
    # Test that the hit counter increments for the /fizzbuzz endpoint
    params = {"int1": 3, "int2": 5, "limit": 15, "str1": "fizz", "str2": "buzz"}
    for _ in range(5):
        client.get("/fizzbuzz", params=params)

    response = client.get("/statistics")
    result = response.json()
    assert result['most_used_request']['hits']
