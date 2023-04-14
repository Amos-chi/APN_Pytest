# Time : 2023/4/14 10:25
import os

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
import pymongo
import paramiko

# # SSH连接MongoDB服务器
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='10.0.0.70', username='amos.chi', key_filename=r'C:\Users\Administrator\Desktop\jobdiva_amos.chi.pem')
#
# # 通过SSH隧道连接MongoDB
# local_port = 27017
# remote_port = 27017
# ssh_transport = ssh.get_transport()
# ssh_channel = ssh_transport.open_channel('direct-tcpip', ('localhost', remote_port), ('localhost', local_port))


#d = os.popen(r'ssh -i C:\Users\Administrator\Desktop\jobdiva_amos.chi.pem  -L 33033:10.0.0.70:27017 amos.chi@13.251.44.53')
client = pymongo.MongoClient("mongodb://localhost:33033/")
#client.admin.authenticate("jobdiva", "!pgJ0dI1@3!2#")
db = client["admin"]
db.authenticate("jobdiva","!pgJ0dI1@3!2#")


