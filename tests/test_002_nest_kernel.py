def test_reset_kernel(nest):  # noqa: F811
    nest.ResetKernel()


def test_get_kernel_status(nest):  # noqa: F811
    kernel_status = nest.GetKernelStatus()
    assert isinstance(kernel_status, dict)


def test_get_kernel_resolution(nest):  # noqa: F811
    resolution = nest.GetKernelStatus("resolution")
    assert isinstance(resolution, float)
    assert resolution == 0.1


def test_get_local_num_threads(nest):  # noqa: F811
    local_num_threads = nest.GetKernelStatus("local_num_threads")
    assert isinstance(local_num_threads, int)
    assert local_num_threads == 1


def test_get_rng_seed(nest):  # noqa: F811
    rng_seed = nest.GetKernelStatus("rng_seed")
    assert isinstance(rng_seed, int)
