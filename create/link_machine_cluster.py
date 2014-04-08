if __name__ == '__main__':
    from wlstModule import *

connect('weblogic', 'weblogic1', 't3://myhost.mydomain.ie:7001')
edit()

startEdit()

cd('/ServerTemplates/my-server-template')
cmo.setMachine(getMBean('/Machines/my-machine'))
cmo.setCluster(getMBean('/Clusters/my-cluster'))

cd('/ServerTemplates/my-server-template/SSL/my-server-template')
cmo.setEnabled(false)

activate()

exit()