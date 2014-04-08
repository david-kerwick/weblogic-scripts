if __name__ == '__main__':
    from wlstModule import *

readTemplate("/home/weblogic/Oracle/Middleware/Oracle_Home/wlserver/common/templates/wls/wls.jar")

print 'Create AdminServer: '
cd('Servers/AdminServer')
set('ListenAddress', 'myhost.mydomain.ie')
set('ListenPort', 7001)

create('AdminServer', 'SSL')
cd('SSL/AdminServer')
set('Enabled', 'false')
set('ListenPort', 7002)

print 'Set the password: '
cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('weblogic1')

cd('/')
cd('NMProperties')
set('SecureListener', 'false')
set('ListenAddress', 'myhost.mydomain.ie')
set('CrashRecoveryEnabled', 'true')

print 'Write the domain: '
setOption('OverwriteDomain', 'true')
setOption('ServerStartMode', 'prod')
writeDomain('/home/weblogic/user_projects/domains/my_domain')
closeTemplate()

exit()