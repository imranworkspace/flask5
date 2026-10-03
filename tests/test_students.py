import pytest
from app import create_app

@pytest.fixture
def client():
    app=create_app()
    app.config['TESTING']=True
    return app.test_client()
id=4
def test_get_student_success_byid(client):
    resp = client.get(f'api/students/{id}')
    assert resp.status_code == 200
    data= resp.get_json()
    assert data['name']=='vicky'

def test_get_student_404_byid(client):
    resp = client.get(f'api/students/{id}')
    assert resp.status_code != 404

@pytest.mark.parametrize('student_id,expected',[(4,200),(24,200),(99,404)])

def test_get_student_success_by_manyids(client,student_id,expected):
    resp = client.get(f'/api/students/{student_id}')
    print(resp.status_code)
    assert resp.status_code==expected

def test_post_new_record(client):
    data = {"name":"suri2","age":23}
    resp = client.post('api/students',json=data)
    assert resp.status_code==201

def test_update_by_id(client):
    data = {"name":"suri22","age":23}
    resp = client.put('api/students/22',json=data)
    assert resp.status_code==200

def test_update_by_id_404(client):
    data = {"name":"IMRAN","age":22}
    resp = client.put('api/students/22',json=data)
    assert resp.status_code!=404

# id=23
# def test_delete_student_by_id(client):
#     resp = client.delete(f'api/students/{id}')
#     assert resp.status_code == 200

# def test_delete_student_by_id_404(client):
#     resp = client.delete(f'api/students/{id}')
#     assert resp.status_code == 404