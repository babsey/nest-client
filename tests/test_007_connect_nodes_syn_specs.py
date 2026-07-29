from random import randint

import pytest


def test_selfconnect_static_synapse(nest):  # noqa: F811
    synapse_model = "static_synapse"
    node_ids = nest.Create("iaf_psc_alpha")

    syn_dict = nest.Connect(node_ids, node_ids, syn_spec=synapse_model, return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert syn_dict["synapse_model"] == synapse_model


def test_selfconnect_synapse_weight(nest):  # noqa: F811
    weight = randint(-10, 10)
    node_ids = nest.Create("iaf_psc_alpha")

    syn_dict = nest.Connect(node_ids, node_ids, syn_spec={"weight": weight}, return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert isinstance(syn_dict["weight"], float)
    assert syn_dict["weight"] == weight


def test_selfconnect_synapse_delay(nest):  # noqa: F811
    delay = randint(1, 10)
    node_ids = nest.Create("iaf_psc_alpha")

    syn_dict = nest.Connect(node_ids, node_ids, syn_spec={"delay": delay}, return_synapsecollection=True)
    assert isinstance(syn_dict, dict)
    assert isinstance(syn_dict["delay"], float)
    assert syn_dict["delay"] == delay
