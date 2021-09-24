import netmiko
dir(netmiko)
connection = netmiko.ConnectHandler(ip="192.168.4.2",device_type="cisco_ios" , username="admin", password="admin")
dir(connection)
while True :
    hostname = connection.find_prompt()
    command= input(hostname)
    print(connection.send_command(command))
connection.disconnect()
