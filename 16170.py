import time

t = time.localtime(time.time())
print(time.strftime('%Y', t))
print(time.strftime('%m', t))
print(time.strftime('%d', t))
