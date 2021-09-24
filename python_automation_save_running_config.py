import netmiko
dir(netmiko)
connection = netmiko.ConnectHandler(ip="192.168.4.2",device_type="cisco_ios" , username="admin", password="admin", secret="hello")
dir(connection)
#enable the configuration
connection.enable()
print("device connected ")
result = connection.send_command("show running-config")
file_name = input("name of file :")
save_file = open(file_name+".txt","w")
save_file.write(result)
save_file.close()
connection.disconnect()
