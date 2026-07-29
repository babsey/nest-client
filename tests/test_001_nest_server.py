has_mpi = False


def test_get_request(nest):  # noqa: F811

    response = nest.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "mpi" in data and "nest" in data
