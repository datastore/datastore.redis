
__version__ = '0.1.3'
__author__ = 'Juan Batiz-Benet'
__email__ = 'juan@benet.ai'
__doc__ = '''
redis datastore implementation.

Tested with:
  * datastore 0.3.0
  * Redis 2.4.15
  * redis 2.7.2

'''

#TODO: Implement queries using a key index.
#TODO: Implement TTL (and key configurations)


import datastore.core


class RedisDatastore(datastore.ShimDatastore):
  '''Simple redis datastore. Does not support queries.

  The redis interface is very similar to datastore's. The only differences are:
  - values must be strings (SerializerShimDatastore)
  - keys should be converted into strings (InterfaceMappingDatastore)
  - `put` calls should be mapped to `set` (InterfaceMappingDatastore)
  '''

  def __init__(self, redis, serializer=None):
    '''Initialize the datastore with given redis client `redis`.

    Args:
      redis: A redis client to use. Must implement the basic redis
          interface: set, get, delete. This datastore keeps the interface so
          basic in order to work with any redis client (or pool of clients).

      serializer: An optional value serializer to use instead of the default.
        Serializer must respond to `loads` and `dumps`.
    '''
    self._redis = redis

    # use an InterfaceMappingDatastore to access the native redis interface
    mapper = datastore.InterfaceMappingDatastore(redis, put='set', key=str)

    # use a SerializerShimDatastore to ensure values are stringified
    serial = datastore.SerializerShimDatastore(mapper, serializer=serializer)

    # initialize ShimDatastore with serial as our child_datastore
    super(RedisDatastore, self).__init__(serial)

  def query(self, query):
    '''Returns an iterable of objects matching criteria expressed in `query`

    Args:
      query: Query object describing the objects to return.

    Raturns:
      Cursor with all objects matching criteria
    '''
    #TODO
    raise NotImplementedError


'''
Hello World:

    >>> import redis
    >>> import datastore.redis
    >>>
    >>> r = redis.Redis()
    >>> ds = datastore.redisRedisDatastore(r)
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

'''
