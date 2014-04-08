if __name__ == '__main__':
    from wlstModule import *

connect('weblogic', 'weblogic1', 't3://myhost.mydomain.ie:7001')
edit()
startEdit()

dynamicServerTemplate = cmo.createServerTemplate('my-server-template')
dynamicServerTemplate.setAcceptBacklog(2000)
dynamicServerTemplate.setAutoRestart(true)
dynamicServerTemplate.setRestartMax(1)
dynamicServerTemplate.setStartupTimeout(600)
dynamicServerTemplate.setAutoKillIfFailed(true)
dynamicServerTemplate.getOverloadProtection().setFailureAction('force-shutdown')
dynamicServerTemplate.getOverloadProtection().setPanicAction('system-exit')
# Set whatever settings best suit the memory on the system and what you what to do with this server
#I believe MaxPermSize should be half the max heap
#The urandom is covered in another post
dynamicServerTemplate.getServerStart().setArguments(
    '-Xmx2048m -Xms2048m -XX:+UseG1GC -XX:MaxPermSize=1024m -Djava.security.egd=file:///dev/./urandom')
dynamicServerTemplate.getLog().setFileName('${serverName}_%yyyy%_%MM%_%dd%_%hhmm%.log')
dynamicServerTemplate.getLog().setRotationType('byTime')
dynamicServerTemplate.getLog().setRedirectStderrToServerLogEnabled(true)
dynamicServerTemplate.getLog().setRedirectStdoutToServerLogEnabled(true)
dynamicServerTemplate.getWebServer().getWebServerLog().setFileName('${serverName}_access_%yyyy%_%MM%_%dd%_%hhmm%.log')
dynamicServerTemplate.getWebServer().getWebServerLog().setRotationType('byTime')

dynCluster = cmo.createCluster('my-cluster')
dynCluster.getOverloadProtection().setFailureAction('force-shutdown')
dynCluster.getOverloadProtection().setPanicAction('system-exit')
dynServers = dynCluster.getDynamicServers()
dynServers.setMaximumDynamicServerCount(1)
dynServers.setServerTemplate(dynamicServerTemplate)

dynServers.setServerNamePrefix('my-server-')

dynServers.setCalculatedMachineNames(true)
dynServers.setCalculatedListenPorts(true)

activate(block="true")

exit()
