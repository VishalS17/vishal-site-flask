def test_home_page(client):
    r = client.get("/")
    assert r.status_code == 200

def test_projects_page(client):
    r = client.get("/projects")
    assert r.status_code in [200, 302]
