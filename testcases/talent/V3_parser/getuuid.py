import hashlib

def get_uuid(file):
    with open(file, 'rb') as f:
        rb = f.read()

    md = hashlib.md5()
    md.update(rb)
    md5 = md.hexdigest()
    return md5