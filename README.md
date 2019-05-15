# database-server
Runs a server that is accessible on http://localhost:4000/. When the server receives a request on http://localhost:4000/set?somekey=somevalue stores the passed key and value in memory. When it receives a request on http://localhost:4000/get?key=somekey returns the value stored at somekey.


## Installation:

* Create a Python3 Virtualenv and activate it:

```
virtualenv -p `which python3.6` venv
```

* Install requirements:

`pip install -r requirements.txt`
