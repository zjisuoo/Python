from collections import ChainMap
default_connection = {‘host’ : ‘localhost’, ‘port’ : 4567}
connection = {‘port’ : 5678}
conn = ChainMap(connection, default_connection) # map creation
conn[‘port’] # port is found in the first dictionary
conn[‘host’] # host is fetched from the second dictionary
conn.maps # we can see the mapping objects
conn[‘host’] = ‘packtpub.com’ # let’s add host
conn.maps
del conn[‘port’] # let’s remove the port information
conn.maps
conn[‘port’] # now port is fetched from the second dictionary
dict(conn) # easy to merge and convert to regular dictionary