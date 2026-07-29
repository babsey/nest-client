import pytest


def test_api_simulate_empty_spike_recorder(nest):  # noqa: F811
    sr_ids = nest.Create("spike_recorder")
    nest.Simulate(100)

    n_events = nest.GetStatus(sr_ids, "n_events")
    assert isinstance(n_events, int)
    assert n_events == 0


def test_api_simulate_empty_spike_recorders(nest):  # noqa: F811
    sr_ids = nest.Create("spike_recorder", 2)
    nest.Simulate(100)

    n_events = nest.GetStatus(sr_ids, "n_events")
    assert isinstance(n_events, list)
    assert all([n == 0 for n in n_events])


def test_api_simulate_spike_event(nest):  # noqa: F811
    """
    Getting n_events from NEST Server MPI throws error:
    ERROR: cannot combine response=[1, 0]
    """
    sg_ids = nest.Create("spike_generator", params={"spike_times": [10]})
    sr_ids = nest.Create("spike_recorder")

    nest.Connect(sg_ids, sr_ids)
    nest.Simulate(100)

    n_events = nest.GetStatus(sr_ids)["n_events"]
    assert isinstance(n_events, int)
    assert n_events > 0


def test_api_simulate_spike_events(nest):  # noqa: F811
    """
    Getting n_events from NEST Server MPI throws error:
    ERROR: cannot combine response=[1, 0]
    """
    sg_ids = nest.Create("spike_generator", params={"spike_times": list(range(10, 100, 10))})
    sr_ids = nest.Create("spike_recorder")

    nest.Connect(sg_ids, sr_ids)
    nest.Simulate(100)

    n_events = nest.GetStatus(sr_ids)["n_events"]
    assert isinstance(n_events, int)
    assert n_events > 0


def test_api_simulate_spike_event_multiple_recorders(nest):  # noqa: F811
    """
    Getting n_events from NEST Server MPI throws error:
    ERROR: cannot combine response=[1, 0]
    """
    sg_ids = nest.Create("spike_generator", 2, params={"spike_times": [10]})
    sr_ids = nest.Create("spike_recorder", 2)

    nest.Connect(sg_ids, sr_ids, "one_to_one")
    nest.Simulate(100)

    n_events = nest.GetStatus(sr_ids)["n_events"]
    assert isinstance(n_events, list)
    assert all([n > 0 for n in n_events])


def test_api_simulate_spike_events_multiple_recorders(nest):  # noqa: F811
    """
    Getting n_events from NEST Server MPI throws error:
    ERROR: cannot combine response=[1, 0]
    """
    sg_ids = nest.Create("spike_generator", 2, params={"spike_times": list(range(10, 100, 10))})
    sr_ids = nest.Create("spike_recorder", 2)

    nest.Connect(sg_ids, sr_ids, "one_to_one")
    nest.Simulate(100)

    n_events = nest.GetStatus(sr_ids)["n_events"]
    assert isinstance(n_events, list)
    assert all([n > 0 for n in n_events])
