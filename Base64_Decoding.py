import base64

base64_string = str(input("Data : "))
base64_bytes = base64_string.encode('ascii')

data_bytes = base64.b64decode(base64_bytes)
data = data_bytes.decode('ascii')

print("Decoded Data:" + data)