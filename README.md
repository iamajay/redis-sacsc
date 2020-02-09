[![Build Status](https://travis-ci.com/iamajay/redis-sacsc.svg?branch=master)](https://travis-ci.com/iamajay/redis-sacsc)
[![Coverage](https://coveralls.io/repos/github/iamajay/redis-sacsc/badge.svg?branch=master)](https://coveralls.io/github/iamajay/redis-sacsc?branch=master)

# redis-sacsc

Redis Server-Assisted Client-Side Caching in Python

#### WARNING!
This feature is still in redis beta release, scheduled to be released in version 6


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
