from flask import Flask
import socket
import os

app=Flask(__name__)

@app.route('/hostname')
def host():
        return socket.gethostname()

@app.route('/author')
def author():
        temp=os.getenv('AUTHOR')
        if temp==None:
                return 'None'
        return os.getenv('AUTHOR')

@app.route('/id')
def id():
        temp=os.getenv('UUID')
        if temp==None:
                return 'None'
        return os.getenv('UUID')

if __name__=='__main__':
        app.run(debug=True,host='0.0.0.0',port=8000)