def test_get_request(nest):  # noqa: F811

    response = nest.get("/")
    assert response.status_code == 200
    assert response.json() == {"mpi": False, "nest": "3.10.0"}
