"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""

import pytest
from src import app
from src import status

@pytest.fixture()
def client():
    """Fixture for Flask test client"""
    return app.test_client()

@pytest.mark.usefixtures("client")
class TestCounterEndpoints:
    """Test cases for Counter API"""

    def test_create_counter(self, client):
        """It should create a counter"""
        result = client.post('/counters/foo')
        assert result.status_code == status.HTTP_201_CREATED
   
    def test_delete_counter(self, client):
        client.post('/counters/deltest')
        assert 'deltest' in client.get('/counters').get_json()

        result = client.delete('/counters/deltest')
        assert result.status_code == status.HTTP_204_NO_CONTENT
        assert 'deltest' not in client.get('/counters').get_json()

    def test_list_counters(self, client):
        """It should list all counters and their values"""
        client.post('/counters/test1')
        client.post('/counters/test2')

        result = client.get('/counters')
        assert result.status_code == status.HTTP_200_OK

        # Other tests share the COUNTERS dict, so assert on the counters
        # this test created rather than on the whole response.
        data = result.get_json()
        assert data['test1'] == 0
        assert data['test2'] == 0

    def test_retrieve_existing_counter(self, client):
        """It should retrieve an existing counter by name"""
        counter_name = "retrievable"
        create_result = client.post(f'/counters/{counter_name}')
        assert create_result.status_code == status.HTTP_201_CREATED

        result = client.get(f'/counters/{counter_name}')

        assert result.status_code == status.HTTP_200_OK
        assert result.get_json() == {counter_name: 0}
