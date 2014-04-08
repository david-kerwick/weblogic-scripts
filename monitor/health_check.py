#redirect wlst's own output to null, print lines in the script itself
redirect('/dev/null', 'false')

connect(userConfigFile='/home/weblogic/user_projects/domains/my_domain/adminServerConfig.secure',
        userKeyFile='/home/weblogic/user_projects/domains/my_domain/adminServerKey.secure',
        url='t3://myhost.mydomain.ie:7001')

servers = cmo.getServers()

domainRuntime()
stoppedServers = []

for server in servers:
    try:
        cd('/ServerRuntimes/' + server.getName())
        currentState = get('HealthState').getState()
        if currentState == 0:
            print server.getName() + ': ' + get('State') + ': HEALTH_OK'
        elif currentState == 1:
            print server.getName() + ': ' + get('State') + ': HEALTH_WARN'
        elif currentState == 2:
            print server.getName() + ': ' + get('State') + ': HEALTH_CRITICAL'
            stoppedServers.append(server.getName())
        elif currentState == 3:
            print server.getName() + ': ' + get('State') + ': HEALTH_FAILED'
            stoppedServers.append(server.getName())
        elif currentState == 4:
            print server.getName() + ': ' + get('State') + ': HEALTH_OVERLOADED'
        else:
            print server.getName() + ': ' + get('State') + ': UNKNOWN HEALTH STATE (' + currentState + ')'

    except WLSTException, e:
        print server.getName() + " is not running."
        stoppedServers.append(server.getName())

disconnect()

if stoppedServers:
    print "Found stopped servers first one is " + stoppedServers[0]
    #If you want to email info on the failed server (probably a good idea) and are on Linux you can do something like this
    #os.system('echo "Auto restarting failed server: %s" | /bin/mailx -s  "WARNING: Auto restart failed server" system@mydomain.ie' % stoppedServers[0])
    nmConnect(userConfigFile='/home/weblogic/user_projects/domains/my_domain/nodemanagerConfig.secure',
              userKeyFile='/home/weblogic/user_projects/domains/my_domain/nodemanagerKey.secure',
              host='myhost.mydomain.ie', port='5556', domainName='my_domain',
              domainDir='/home/weblogic/user_projects/domains/my_domain/', nmType='plain')

    runningStatus = nmServerStatus(stoppedServers[0])
    print 'Server ' + stoppedServers[0] + ' current running state is ' + runningStatus

    #turn redirect off, we want to see how the server kill and start goes
    redirect('/dev/null', 'true')
    #kill the server and start it again
    try:
        nmKill(stoppedServers[0])
    except WLSTException, e:
        print 'Could not kill server, it may not have been running '

    print 'Starting server \'' + stoppedServers[0] + '\' using nodemanager '
    nmStart(stoppedServers[0])



exit()
