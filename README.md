# redis-sacsc

[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services)
[![Build Status](https://travis-ci.com/wemake.services/redis-sacsc.svg?branch=master)](https://travis-ci.com/wemake.services/redis-sacsc)
[![Coverage](https://coveralls.io/repos/github/wemake.services/redis-sacsc/badge.svg?branch=master)](https://coveralls.io/github/wemake.services/redis-sacsc?branch=master)
[![Python Version](https://img.shields.io/pypi/pyversions/redis-sacsc.svg)](https://pypi.org/project/redis-sacsc/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Redis Server-Assisted Client-Side Caching in Python


## Features

- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)
- Redis Server-Assisted Client-Side Caching


## Installation

```bash
pip install redis-sacsc
```


## Example

Showcase how your project can be used:

```python
import redis
from redis_sacsc import Manager
pool = redis.ConnectionPool.from_url("redis://127.0.0.1:6379")
manager = Manager(pool, capacity=512)
redis_conn = manager.get_connection()
redis_conn.set('foo', 'bar')
redis_conn.get('foo')
# => 'bar'

```

## License

[MIT](https://github.com/iamajay/redis-sacsc/blob/master/LICENSE)
