# Exercice 1

## Variables declaration (line 7-9)

- RANDOM_KEY = md5.new("085ZMVsBnTYuO6OK7gfJpGXeik5VZamC").digest;
* MD5
* Same key for every one
* Key stored in plain text in the code

- SECURE_DIRECTORY = '/tmp'
* /tmp is not meant to be a secure storage. it is a directory accessible for read and write by all users.

## Secure store (line11-17)
- IV 
* IV = b"\0\0\0\0\0\0\0\0"; IV should not be only zeros.

- d = des(RANDOM_KEY[0:8],pyDes.ECB, IV, pad=None, padmode=pyDes.PAD_PKCSS) 
* pad=None ? 
* ECB ?

- f = open(SECURE_DIRECTORY + '/' + filename + '-' + suffix, 'w')

- f.write(d.encrypt(bytes(data)))

* filename, suffix, data sanitised ?

## List secure data (line 19)
- def list_secure_data(path): return commands.getstatusoutput('ls ' + SECURE_DIRECTORY+ '/' + path)[1]
* Command injection ? with a specific path

## Api employee (line 24-29)
- @app.route('/employee')
employee name in plain text. Everyone can access it.

- "list": lambda: list_secure_data(request.args['ssn'])
* request.args['ssn'] is not sanitised, could perform command injection.

- "add": lambda: secure_store(request.args['ssn'], request.args['email'],request.args['data'])
* request.args are not sanitised. 

- s.get(request.args['cmd'], lambda: "no such command")
* command injection ? not secure

