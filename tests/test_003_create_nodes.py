from random import randint

size = randint(2, 10)


def test_create_single_node(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha")
    assert isinstance(node_ids, list)
    assert len(node_ids) == 1
    assert node_ids == [1]


def test_create_multiple_nodes(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha", size)
    assert isinstance(node_ids, list)
    assert len(node_ids) == size
    assert node_ids == list(range(1, size + 1))


def test_create_node_with_params(nest):  # noqa: F811
    I_e = 376

    node_ids = nest.Create("iaf_psc_alpha", params={"I_e": I_e})
    node_I_e = nest.GetStatus(node_ids, "I_e")
    assert isinstance(node_I_e, list)
    assert node_I_e == [I_e]


def test_create_multiple_nodes_with_params(nest):  # noqa: F811
    I_e = 376

    node_ids = nest.Create("iaf_psc_alpha", n=size, params={"I_e": I_e})
    node_I_e = nest.GetStatus(node_ids, "I_e")
    assert isinstance(node_I_e, list)
    assert len(node_I_e) == size
    assert node_I_e == size * [I_e]


def test_create_multiple_nodes_with_various_params(nest):  # noqa: F811
    I_e = [375, 376]

    node_ids = nest.Create("iaf_psc_alpha", n=2, params={"I_e": I_e})
    node_I_e = nest.GetStatus(node_ids, "I_e")
    assert isinstance(node_I_e, list)
    assert len(node_I_e) == 2
    assert node_I_e == I_e
