if __name__ == '__main__': 
    from wlstModule import *
    
connect(userConfigFile='/home/weblogic/user_projects/domains/my_domain/adminServerConfig.secure', userKeyFile='/home/weblogic/user_projects/domains/my_domain/adminServerKey.secure', url='t3://myhost.mydomain.ie:7001')

start('my-cluster', 'Cluster')

exit()