if __name__ == '__main__': 
    from wlstModule import *
    
nmConnect(userConfigFile='/home/weblogic/user_projects/domains/my_domain/nodemanagerConfig.secure', userKeyFile='/home/weblogic/user_projects/domains/my_domain/nodemanagerKey.secure', host='myhost.mydomain.ie', port='5556', domainName='my_domain', domainDir='/home/weblogic/user_projects/domains/my_domain/', nmType='plain')

nmKill('AdminServer') 

exit()
