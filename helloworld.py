from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hola')
def hola():
    return 'Hola!'

if __name__ == '__main__':
    #http
    #app.run('0.0.0.0', port=80)

    #https flask certificate
    #app.run('0.0.0.0', port=443, ssl_context='adhoc')

    #https self-signed certificate
    app.run('0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))
