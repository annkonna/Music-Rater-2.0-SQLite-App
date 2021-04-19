import json

import bottle
import eventlet
import eventlet.wsgi

import ratings


@bottle.route('/')
def index():
    return bottle.static_file("index.html", root="")


@bottle.route('/myCode.js')
def static():
    return bottle.static_file("myCode.js", root="")


@bottle.route('/songs')
def get_chat():
    return json.dumps(ratings.get_songs())


@bottle.post('/add_song')
def add_song():
    content = bottle.request.body.read().decode()
    content = json.loads(content)
    ratings.add_song(content)
    return json.dumps(ratings.get_songs())


@bottle.post('/rate_song')
def rate_song():
    content = bottle.request.body.read().decode()
    content = json.loads(content)
    ratings.rate_song(content)
    return json.dumps(ratings.get_songs())


eventlet.wsgi.server(eventlet.listen(('localhost', 8080)), bottle.default_app())
