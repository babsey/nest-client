### How to execute pytest?

Install local package with uv
```
uv pip install -e .
```

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
uv run pytest
```

Increase verbosity (to see individual test functions)

```
uv run pytest -v
```

Run pytest with coverage

```
uv run pytest --cov=src/nest_client
```

Run pytest with NEST Server MPI (deselect not_mpi markers)

```
uv run pytest -m 'not not_mpi'
```

### Debugging tests

Add debug logger.

```
import logging
logger = logging.getLogger()

...

logger.debug("Hello world")
```

Run pytest with debugs.

```
uv run pytest --log-level debug
```
