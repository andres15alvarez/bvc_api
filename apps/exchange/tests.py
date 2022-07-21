import pytest


@pytest.mark.django_db
def test_list_ibc(client):
    response = client.get('/exchange', data={'date_from': '2021-01-01', 'date_to': '2021-01-05'})
    assert response.status_code == 200
