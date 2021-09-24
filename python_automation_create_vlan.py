import netmiko
import time
dir(netmiko)
cisco_switch = {
'ip' : "192.168.4.2",
'device_type' : "cisco_ios" ,
'username': "admin" ,
'password':"admin",
'secret':"hello",
}
connection = netmiko.ConnectHandler(**cisco_switch)
dir(connection)
hostname = connection.find_prompt()
print("connected to hostname : " + hostname+"\n");
#create a vlan : 
connection.enable()
vlan_id = input("which vlan id you want to create : ")
#
# check if a vlan exists or not 

if not vlan_id.isnumeric() :
    print("you did not enter a valid vlan id quiting !!!\n")
    connection.disconnect()
    quit()
result = connection.send_command("show vlan-switch id "+vlan_id)
if len(result)<100 :
    vlan_name = input("name for the vlan "+vlan_id+" : ")
    print("please wait we are creating your vlan \n")
    connection.send_command("vlan database", expect_string=r"#")
    time.sleep(1)
    result = connection.send_command("vlan "+vlan_id+" name "+ vlan_name)
    time.sleep(1)
    print("vlan id : "+ vlan_id+" is created \n")
    connection.send_command("exit", expect_string=r"#")
else :
    print("vlan id already exists \n")

#adding interfaces
user_answer = input("do you want to add some interfaces to vlan id "+vlan_id+" [yes/no] : ")
if user_answer == "yes" : #if yes he want to add interfaces to the vlan id 
    #connection.disconnect()
    time.sleep(1)
    #connection = netmiko.ConnectHandler(**cisco_switch)
    time.sleep(1)
    interfaces = []
    while True :
        interfs = input("please enter a valid interface (to skip tap (no) ) : ")
        interfs = interfs.replace(" ",'')
        if interfs != "no" : # the user give a valid interface name
            interfaces.append(interfs) if interfs not in interfaces else interfaces
            continue
        else :
            print("is this all the interfaces you want to add : \n" )
            print(interfaces)
            answer = input(" [yes / other ] : " )
            if answer != "yes":
                break;
            while len(interfaces)>0 :
                interf = interfaces.pop(0)
                print("adding the interface : "+interf+"\n")
                config_commands = ["int "+interf,"switchport mode access" ,
                        "switchport access vlan "+vlan_id]
                connection.send_config_set(config_commands,exit_config_mode =False)
                connection.send_command("do wr")
                print("interface "+interf +" is added to vlan "+vlan_id+"\n")
            break;
else : # user does not want to add interfaces to the vlan id 
    print("no interface is added ")
answer = input("do you want to add an address ip to the vlan ? [yes/no] : ")
if answer == "yes" :
    add_ip = input("address id you want to add : ")
    mask_ip = input("mask : ")
    command_format = "ip add "+add_ip+" "+mask_ip;
    result = connection.send_config_set(["int vlan "+vlan_id , command_format],exit_config_mode =False)
  # connection.send_command("no shutdown")
    connection.send_command("do wr")
    print("the ip address is added to the vlan " + vlan_id +"\n")
print("\nenjoy !!!!!!")
connection.disconnect()
