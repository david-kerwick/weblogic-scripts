if __name__ == '__main__': 
    from wlstModule import *  
  
try:  
    connect(userConfigFile='/home/weblogic/user_projects/domains/my_domain/adminServerConfig.secure', userKeyFile='/home/weblogic/user_projects/domains/my_domain/adminServerKey.secure', url='t3://myhost.mydomain.ie:7001')
    shutdown()
    disconnect()
except WLSTException,e:
    print 'Could not shutdown admin server, attempting to kill it'
    nmConnect(userConfigFile='/home/weblogic/user_projects/domains/my_domain/nodemanagerConfig.secure', userKeyFile='/home/weblogic/user_projects/domains/my_domain/nodemanagerKey.secure', host='myhost.mydomain.ie', port='5556', domainName='my_domain', domainDir='/home/weblogic/user_projects/domains/my_domain/', nmType='plain')
    nmKill('AdminServer')
    disconnect()

exit()
