def test_selfconnect_node(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha")

    syn_dict = nest.Connect(node_ids, node_ids, return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert syn_dict["source"] == syn_dict["target"] == node_ids[0]


def test_selfconnect_nodes(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha", n=2)

    syn_dict = nest.Connect(node_ids, node_ids, return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert syn_dict["source"] == [node_id for node_id in node_ids for _ in range(2)]  # [1,1,2,2]
    assert syn_dict["target"] == 2 * node_ids  # [1,2,1,2]


def test_connect_multiple_nodes(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha", n=2)

    syn_dict = nest.Connect([node_ids[0]], [node_ids[1]], return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert syn_dict["source"] == node_ids[0] and syn_dict["target"] == node_ids[1]


def test_connect_various_nodes(nest):  # noqa: F811
    source_ids = nest.Create("iaf_psc_alpha")
    target_ids = nest.Create("iaf_psc_alpha")

    syn_dict = nest.Connect(source_ids, target_ids, return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert syn_dict["source"] == source_ids[0] and syn_dict["target"] == target_ids[0]


def test_connect_various_nodes(nest):  # noqa: F811
    source_ids = nest.Create("iaf_psc_alpha", 2)
    target_ids = nest.Create("iaf_psc_alpha", 2)

    syn_dict = nest.Connect(source_ids, target_ids, return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert syn_dict["source"] == [source_id for source_id in source_ids for _ in range(2)]  # [1,1,2,2]
    assert syn_dict["target"] == 2 * target_ids  # [1,2,1,2]
