import telnetlib
from py4j.java_gateway import JavaGateway



class DubboService(object):
    host ='192.168.1.15:8807'
    port ='8807'
    cmd ='cn.magfin.publicapi.base.EncryptionService.decrypt(file)'
    dubbo = 'dubbo>'
def __init__(self,host,port):
        self.conn=telnetlib.Telnet()
        self.conn.open(host,port)

    # def DubboMethod(self,cmd):
    #     self.conn.write('invoke {}\n'.format(cmd).encode())
    #     data = self.conn.read_until(self.dubbo.encode()).decode().split('\r\n')[0]
    #     return data

if __name__ == '__main__':
    f = open("/Users/hanxiaodi/PycharmProjects/Appiumpro/testcase/hello.txt", "r", encoding="utf-8")
    print()
