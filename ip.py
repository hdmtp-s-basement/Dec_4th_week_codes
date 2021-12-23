def ip_validity(ip):
    import socket

    try:
        socket.inet_aton(ip)
        ip_valid = True
    except socket.error:
        ip_valid = False
    return ip_valid


#print(ip_validity("194.22.222.222"))
#source => https://moonbooks.org/Articles/How-to-get-visitor-ip-address-with-django-/

import socket   
hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
print("Your Computer Name is:" + hostname)   
print("Your Computer IP Address is:" + IPAddr)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("python.org", 80))
print(s.getsockname()[0])
print(s.getsockname())
s.close()

#https://docs.python.org/3/howto/sockets.html

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
    
print(get_ip())
