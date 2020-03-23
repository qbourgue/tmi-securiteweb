# Exercice 1

## Variables declaration (line 7-9)

- RANDOM_KEY = md5.new("085ZMVsBnTYuO6OK7gfJpGXeik5VZamC").digest;
* MD5
* Same key for every user
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
* Directory traversal (filemane= '../../etc/passwd')

- f.write(d.encrypt(bytes(data)))

* filename, suffix, data sanitised ?

## List secure data (line 19)
- def list_secure_data(path): return commands.getstatusoutput('ls ' + SECURE_DIRECTORY+ '/' + path)[1]
* Command injection, path = ' ; rm /tmp'
* Directory traversal, path = '../../homes') 

## Api employee (line 24-30)
- Line 27: "list": lambda: list_secure_data(request.args['ssn'])
* request.args['ssn'] is not sanitised, could perform command injection.
* Expose all files, begining with request.args['ssn'], to the api user

- Line 28: "add": lambda: secure_store(request.args['ssn'], request.args['email'],request.args['data'])
* request.args are not sanitised. 
* suffix = email in plain text 

- Line 30:  s.get(request.args['cmd'], lambda: "no such command")
* command injection ? not secure
* User can perform any command he wants.

# WHODUNNIT

## Tim created random key
## John choose the Secure_directory

## Jo implemented api_employee
* He did not sanitised the request arguments
* He add line 30, allowing user to perform any command he wants
* He introduces a way to list every file in the secure_directory
