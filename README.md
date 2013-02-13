# datastore-redis

## datastore implementation for redis

See [datastore](https://github.com/datastore/datastore).


### Install

From pypi (using pip):

    sudo pip install datastore.redis

From pypi (using setuptools):

    sudo easy_install datastore.redis

From source:

    git clone https://github.com/datastore/datastore.redis/
    cd datastore.redis
    sudo python setup.py install


### License

datastore.redis is under the MIT License.

### Contact

datastore.redis is written by [Juan Batiz-Benet](https://github.com/jbenet).
It was extracted from [datastore](https://github.com/datastore/datastore)
in Feb 2013.

Project Homepage:
[https://github.com/datastore/datastore.redis](https://github.com/datastore/datastore.redis)

Feel free to contact me. But please file issues in github first. Cheers!


### Hello World

    >>> import redis
    >>> import datastore.redis
    >>>
    >>> r = redis.Redis()
    >>> ds = datastore.redis.RedisDatastore(r)
    >>>
    >>> hello = datastore.Key('hello')
    >>> ds.put(hello, 'world')
    >>> ds.contains(hello)
    True
    >>> ds.get(hello)
    'world'
    >>> ds.delete(hello)
    >>> ds.get(hello)
    None
