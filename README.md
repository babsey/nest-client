# NEST Client -- A client for the NEST Server

The easiest way to interact with the NEST Server is the NEST Client. It can be
used either by directly starting a Python session in a clone of that repository,
or by installing it by `pip` install therein. NEST Simulator itself does not
have to be installed in order to use the NEST Client.

Using a dynamic function mapping mechanism, the NEST Client supports the same
functions as PyNEST does. However, instead of directly executing calls in NEST,
it forwards them together with their arguments to the NEST Server, which in turn
executes them. To you as a user, everything looks much like a typical simulation
code for NEST Simulator.

### Basic usage

To give you an idea of the usage, the following table shows a comparison of a
typical simulation once for PyNEST and once using the NEST Client.

The client can be installed with this command:

```
pip install nest-client
```

The directory `examples` holds some examples that demonstrate the usage of the
client.

- For API calls:

  ```
  python ./examples/api_example.py
  ```

- For exec call:

  ```
  python ./examples/exec_example.py
  ```

### Development mode

We recommend to use virtual environment, e.g. with `uv`:

Install `nest-client` as an editable package

```
uv pip install -e .
```

#### Test against multiple Python versions using uv

```
make test-all
```

### References

- [Documentation](https://nest-simulator.readthedocs.io/en/latest/interface_nest/nest_server.html#the-nest-client)
- [NEST Simulator](http://nest-simulator.org) via its REST-based interface
- [NEST Server](https://nest-simulator.readthedocs.io/en/latest/interface_nest/nest_server.html)
