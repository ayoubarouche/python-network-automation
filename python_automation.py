import netmiko
dir(netmiko)
connection = netmiko.ConnectHandler(ip="192.168.4.2",device_type="cisco_ios" , username="admin", password="admin", secret="hello")
dir(connection)
#enable the configuration
connection.enable()
hostname = connection.find_prompt()
print(hostname+"\n")
interfaces = connection.send_command("show vlan-switch brief")
#result = interfaces.split(' ')
#the_new_result = [ item for item in result if item.startswith('Fa')]
the_new_result = interfaces.split("\n")
the_new_result.pop(0)
the_new_result.pop(0)
the_new_result.pop(0)
vlan_ids = []
vlan_names = []
i=0
for item in the_new_result :
    vlan_id = ""
    vlan_name= ""
    vlan_interfaces = ""
    item_length = len(item)
    i = 0
    for it in range (item_length) :
        if item[it] == ' ' :
            break
        vlan_id += item[it]
    item.removesuffix(vlan_id)
    vlan_ids.insert(0, vlan_id)
    print(vlan_id+"\n")
    item.strip()
    item_length = len(item)
    
    print("the new length is : "+item_length+"\n")
    for it in range (item_length) :
        if item[it] == ' ' :
            break
        vlan_name += item[it]
    vlan_names.insert(0,vlan_name)
    item.replace(vlan_name , '')
    item.strip()
    
print("vlan ids are \n ========================\n")
print(vlan_ids)
print(vlan_names)
quit()
the_new_result = interfaces.split("active")
the_new_result = [ item.strip() for item in the_new_result]
k = 0
first_vlan = the_new_result.pop(0)
get_first_vlan = first_vlan.split("\n")
first_vlan = get_first_vlan.pop(2)
for i in the_new_result :
    item = i.split("\n")
   
    print ("    " + "and length is : " +str(len(item)))
    if len(item) < 2 :
        print("true")
        the_new_result.remove(i)
    else :
        print("false")
    print("---------------------------\n")
    print('\n')
print("\n ======== the new result is ======================")
the_new_result.insert(0, first_vlan)

print(the_new_result)
#print(the_new_result)
#connection.send_command("vlan database", expect_string=r"#")
#connection.send_command("vlan 3")
#while True :
#    command= input(hostname)
#    print(connection.send_command(command))
connection.disconnect()
