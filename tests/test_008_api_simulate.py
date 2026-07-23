def test_simulate(nest):  # noqa: F811
    biological_time = nest.GetKernelStatus("biological_time")
    assert isinstance(biological_time, float)
    assert biological_time == 0

    nest.Simulate(100)

    biological_time = nest.GetKernelStatus("biological_time")
    assert isinstance(biological_time, float)
    assert biological_time == 100


def test_api_simulate_empty_spike_recorder(nest):  # noqa: F811
    sr_ids = nest.Create("spike_recorder")
    nest.Simulate(100)

    n_events = nest.GetStatus(sr_ids, "n_events")
    assert isinstance(n_events, list)
    assert n_events[0] == 0


def test_api_simulate_spike_events(nest):  # noqa: F811
    sg_ids = nest.Create("spike_generator", params={"spike_times": [10]})
    sr_ids = nest.Create("spike_recorder")

    nest.Connect(sg_ids, sr_ids)
    nest.Simulate(100)

    n_events = nest.GetStatus(sr_ids, "n_events")
    assert isinstance(n_events, list)
    assert n_events[0] > 0
