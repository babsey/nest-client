from random import randint

size = randint(2, 10)


def test_selfconnect_single_node_all_to_all(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha")

    syn_dict = nest.Connect(node_ids, node_ids, "all_to_all", return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert isinstance(syn_dict["source"], int)
    assert syn_dict["source"] == syn_dict["target"] == node_ids[0]


def test_selfconnect_single_node_one_to_one(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha")

    syn_dict = nest.Connect(node_ids, node_ids, "one_to_one", return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert isinstance(syn_dict["source"], int)
    assert syn_dict["source"] == syn_dict["target"]


def test_selfconnect_all_to_all(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha", size)

    syn_dict = nest.Connect(node_ids, node_ids, "all_to_all", return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert isinstance(syn_dict["source"], list)
    assert syn_dict["source"] == [node_id for node_id in node_ids for _ in range(size)]  # [1,1,2,2]
    # assert syn_dict["target"] == size * node_ids
    # BUG: Why are target ids not ordered as expected, e.g. [1,2,1,2]?


def test_selfconnect_one_to_one(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha", size)

    syn_dict = nest.Connect(node_ids, node_ids, "one_to_one", return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert isinstance(syn_dict["source"], list)
    assert syn_dict["source"] == syn_dict["target"] == node_ids


def test_selfconnect_fixed_outdegree(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha", size)

    syn_dict = nest.Connect(
        node_ids, node_ids, {"rule": "fixed_outdegree", "outdegree": 1}, return_synapsecollection=True
    )
    assert isinstance(syn_dict, dict)
    assert isinstance(syn_dict["source"], list)
    assert syn_dict["source"] == node_ids


def test_selfconnect_fixed_indegree(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha", size)

    syn_dict = nest.Connect(
        node_ids, node_ids, {"rule": "fixed_indegree", "indegree": 1}, return_synapsecollection=True
    )
    assert isinstance(syn_dict, dict)
    assert isinstance(syn_dict["target"], list)
    assert all([(target_id in node_ids) for target_id in syn_dict["target"]])


def test_selfconnect_fixed_total_number(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha", size)

    syn_dict = nest.Connect(node_ids, node_ids, {"rule": "fixed_total_number", "N": 1}, return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert isinstance(syn_dict["source"], int)
    assert syn_dict["source"] in node_ids


def test_selfconnect_fixed_total_numbers(nest):  # noqa: F811
    N = randint(2, size)

    node_ids = nest.Create("iaf_psc_alpha", size)

    syn_dict = nest.Connect(node_ids, node_ids, {"rule": "fixed_total_number", "N": N}, return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert isinstance(syn_dict["source"], list)
    assert len(syn_dict["source"]) == N


def test_selfconnect_pairwise_bernoulli(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha", size)

    syn_dict = nest.Connect(node_ids, node_ids, {"rule": "pairwise_bernoulli", "p": 0.5}, return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    if "source" in syn_dict:
        assert isinstance(syn_dict["source"], list)


def test_selfconnect_pairwise_bernoulli_no_autoapses_no_multapses(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha", size)

    syn_dict = nest.Connect(
        node_ids,
        node_ids,
        {"rule": "pairwise_bernoulli", "p": 0.5, "allow_autapses": False, "allow_multapses": False},
        return_synapsecollection=True,
    )
    assert isinstance(syn_dict, dict)
    if "source" in syn_dict:
        assert isinstance(syn_dict["source"], list)


def test_selfconnect_symmetric_pairwise_bernoulli(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha", size)

    syn_dict = nest.Connect(
        node_ids,
        node_ids,
        {"rule": "symmetric_pairwise_bernoulli", "p": 0.5, "allow_autapses": False, "make_symmetric": True},
        return_synapsecollection=True,
    )
    assert isinstance(syn_dict, dict)
    if "source" in syn_dict:
        assert isinstance(syn_dict["source"], list)


def test_selfconnect_pairwise_poisson(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha", size)

    syn_dict = nest.Connect(
        node_ids,
        node_ids,
        {"rule": "pairwise_poisson", "pairwise_avg_num_conns": 0.5},
        return_synapsecollection=True,
    )
    assert isinstance(syn_dict, dict)
    if "source" in syn_dict:
        assert isinstance(syn_dict["source"], list)
