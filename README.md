wsgi Delegator
==============

Delegate your request to multiple `wsgi` instances.

Usage
=====

just wrap your instances in a `dict`

```
from bottle import Bottle
from wsgidelegator import Delegator
from wsgiref.simple_server import make_server


app1 = Bottle()
app2 = Bottle()


@app1.route('/')
def f():
    return 'test 1'

@app2.route('/')
def f():
    return 'test 2'

app = Delegator({ 'api': app1 }, default = app2)

httpd = make_server('localhost', 8089, app)
httpd.serve_forever()
```

reslut 

```
$ curl localhost:8089/api
test 1

$ curl localhost:8089/other
test 2

```

