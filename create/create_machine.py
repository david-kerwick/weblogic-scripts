if __name__ == '__main__':
    from wlstModule import *

print 'Starting createMachine script ....'
#connect to the adminserver this time, using the username, password 
#and hostname set you in the create domain script
connect('weblogic', 'weblogic1', 't3://myhost.mydomain.ie:7001')

#start up an edit session
edit()
startEdit()
#change to the root
cd('/')

#create a unix machine with what ever name suits
myMachine = cmo.createUnixMachine("my-machine")

print 'Create machine result: ' + str(myMachine)

#set the nodemanager settings, again that match the settings set up in 
#the create domain script
myMachine.getNodeManager().setNMType('plain')
myMachine.getNodeManager().setListenAddress('myhost.mydomain.ie')

#save and activate the changes
save()
activate(block="true")

print 'Done'

exit()