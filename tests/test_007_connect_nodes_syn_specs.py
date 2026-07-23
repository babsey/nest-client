from random import randint


def test_selfconnect_static_synapse(nest):  # noqa: F811
    node_ids = nest.Create("iaf_psc_alpha")

    syn_dict = nest.Connect(node_ids, node_ids, syn_spec="static_synapse", return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert isinstance(syn_dict["source"], int)
    assert syn_dict["source"] == syn_dict["target"] == node_ids[0]


def test_selfconnect_synapse_weight(nest):  # noqa: F811
    weight = randint(-10, 10)
    node_ids = nest.Create("iaf_psc_alpha")

    syn_dict = nest.Connect(node_ids, node_ids, syn_spec={"weight": weight}, return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert syn_dict["weight"] == weight


def test_selfconnect_synapse_delay(nest):  # noqa: F811
    delay = randint(1, 10)
    node_ids = nest.Create("iaf_psc_alpha")

    syn_dict = nest.Connect(node_ids, node_ids, syn_spec={"delay": delay}, return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert syn_dict["delay"] == delay
