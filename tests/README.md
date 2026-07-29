### How to execute pytest?

Important: The nest server should be started with these settings:

- it is unauthorized
- the exec call is enabled
- the Python code is not restricted
- and loaded modules are nest and numpy.

First start NEST Server in other terminal:

```
nest-server start
```

Run pytest

```
pytest
```

Run pytest in virtual environment.

```
uv run --with pytest pytest
```

Increase verbosity (to see the test functions)

```
uv run --with pytest pytest -v
```

Run pytest with NEST Server MPI (deselect not_mpi markers)

```
uv run --with pytest pytest -m 'not not_mpi'
```

### Debugging tests

Add debug log.

```
from app_test_client import logger

...

logger.debug("Hello world")
```

Run with log level for debug.

```
uv run --with pytest pytest --log-level debug
```
