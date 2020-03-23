from flask import Flask, url_for, json, request
from pyDes import des
import commands
import md5
import pyDes

app = Flask(__name__)
RANDOM_KEY = md5.new("085ZMVsBnTYuO6OK7gfJpGXeik5VZamC").digest;
SECURE_DIRECTORY = '/tmp'

def secure_store(filename, suffix, data):
    IV = b"\0\0\0\0\0\0\0\0";
    d = des(RANDOM_KEY[0:8],pyDes.ECB, IV, pad=None, padmode=pyDes.PAD_PKCSS)
    f = open(SECURE_DIRECTORY + '/' + filename + '-' + suffix, 'w')
    f.write(d.encrypt(bytes(data)))
    f.close()
    return 'data stored'

def list_secure_data(path): return commands.getstatusoutput('ls ' + SECURE_DIRECTORY+ '/' + path)[1]

@app.route('/')
def api_root(): return 'Welcome to employee data storage api'

@app.route('/employee')
def api_employee():
    s = {"list": lambda: list_secure_data(request.args['ssn']),
         "add": lambda: secure_store(request.args['ssn'], request.args['email'],
            request.args['data'])}
    return s.get(request.args['cmd'], lambda: "no such command")()

if __name__ == '__main__': app.run()
