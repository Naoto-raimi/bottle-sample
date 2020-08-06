from bottle import route, run, template, request, get, post


@get('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


@post('/login')
def do_login():
    username = request.forms.username
    password = request.forms.password
    if username == "username" and password == "password":
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


run(host='localhost', port=8080, debug=True, reloader=True)
