if __name__ == '__main__':
    from wlstModule import *

print 'Starting the  create datasource script ....'
#connect to the Adminserver
connect('weblogic', 'weblogic1', 't3://myhost.mydomain.ie:7001')
#switch to the cluster
cd("/Clusters/my-cluster")
#record the cluster a variable for later use
target = cmo
#return to the root
cd("../..")

#method to create a datasource with generic settings
def create_datasource(username, password, jndiList):
    print 'Creating a data source with name ' + username
    #Create a datasource using the username as the name
    jdbcSystemResource = create(username, "JDBCSystemResource")
    jdbcResource = jdbcSystemResource.getJDBCResource()
    jdbcResource.setName(username)

    #set the connection properties
    connectionPoolParams = jdbcResource.getJDBCConnectionPoolParams()
    connectionPoolParams.setConnectionReserveTimeoutSeconds(25)
    connectionPoolParams.setInitialCapacity(1)
    connectionPoolParams.setMaxCapacity(5)
    connectionPoolParams.setTestConnectionsOnReserve(true)
    connectionPoolParams.setHighestNumWaiters(20)
    connectionPoolParams.setStatementTimeout(30)
    connectionPoolParams.setTestTableName("SQL SELECT 1 FROM DUAL")

    #add each element in the jndiList array as a jndi name
    dsParams = jdbcResource.getJDBCDataSourceParams()
    for jndi in jndiList:
      print 'Add jndi ' + jndi + ' to datasource ' + username
      dsParams.addJndiName(jndi)

    #Set the connection to the database
    driverParams = jdbcResource.getJDBCDriverParams()
    driverParams.setUrl("jdbc:oracle:thin:@your_db_hostname:1521:your_db_server_name")
    driverParams.setDriverName("oracle.jdbc.driver.OracleDriver")
    driverParams.setPassword(password)

    driverProperties = driverParams.getProperties()
    proper = driverProperties.createProperty("user")
    proper.setValue(username)

    #target the new datasource to your cluster
    jdbcSystemResource.addTarget(target)

edit()
startEdit()

#create an array for the datasource
jndiList='jdbc/whatever','jdbc/whomever','jdbc/etc'
create_datasource('who_ds', 'who_ds_pw', jndiList)

#create an array for the datasource
jndiList=['jdbc/curly','jdbc/larry','jdbc/moo']
create_datasource('stooges', 'stooges_pw', jndiList)

save()
activate(block="true")

print 'Finished configuring the data source'
