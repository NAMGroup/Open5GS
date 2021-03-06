import yaml
import socket
import sys
import netifaces
import os


def find_IP():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        print("IP fetch error")
    

def parseAUSF():
    documents = None
    try:
        # with open(r'ausfOld.yaml') as file:
        with open(r'/etc/open5gs/ausf.yaml') as file:

            documents = yaml.safe_load(file)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    # print(documents["ausf"]["sbi"][0]["addr"])
    # print("--------------------------------->")
    try:
        documents["ausf"]["sbi"][0]["addr"] = own_ip
        documents["ausf"]['sbi'][0]['port'] = 7781
    except:
        print("Paths have been changed")
    # print("--------------------------------->")
    # print(documents)

    try:
        # with open('ausf.yaml', 'w') as outfile:
        with open('/etc/open5gs/ausf.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()
    
    os.system('sudo systemctl restart open5gs-ausfd')


def parseUDM():
    documents = None
    try:
        with open(r'/etc/open5gs/udm.yaml') as file:
        # with open(r'udmOld.yaml') as file:
            documents = yaml.safe_load(file)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    print(documents["udm"]["sbi"][0]["addr"])
    # print("--------------------------------->")
    try:
        documents["udm"]["sbi"][0]["addr"] = own_ip
        documents["udm"]['sbi'][0]['port'] = 7779
    except:
        print("Paths have been changed")
    # print("--------------------------------->")
    # print(documents)

    try:
        with open('/etc/open5gs/udm.yaml', 'w') as outfile:
        # with open('udm.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()
    
    os.system('sudo systemctl restart open5gs-udmd')


def parseNRF():
    documents = None
    try:
        # with open(r'nrfOld.yaml') as file:
        with open(r'/etc/open5gs/old/nrf.yaml') as file:
            documents = yaml.safe_load(file)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    # print(documents["nrf"]["sbi"]["addr"][0])
    try:
        documents["nrf"]["sbi"]["addr"][0] = own_ip
        documents["nrf"]['sbi'][0]['port'] = 7778
        if documents["nrf"]["sbi"]["addr"][1] == "::1":
            del documents["nrf"]["sbi"]["addr"][1]

    except:
        print("Paths have been changed")

    try:
        # with open('nrf.yaml', 'w') as outfile:
        with open('/etc/open5gs/nrf.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()

    os.system('sudo systemctl restart open5gs-nrfd')


def parseAMF():
    documents = None
    try:
        # with open(r'amfOld.yaml') as file:
        with open(r'/etc/open5gs/amf.yaml') as file:
            documents = yaml.safe_load(file)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    # print(documents["amf"]["ngap"][0]["addr"])
    try:
        #documents["amf"]["ngap"][0]["addr"] = netifaces.ifaddresses('ens4')[2][0]['addr']
        documents["amf"]["ngap"][0]["addr"] = own_ip
        documents["amf"]["sbi"][0]['addr'] = own_ip
        documents["amf"]["plmn_support"][0]["s_nssai"][0]["sd"] = 1
    except:
        print("Paths have been changed")

    try:
        # with open('amf.yaml', 'w') as outfile:
        with open('/etc/open5gs/amf.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()
    
    os.system('sudo systemctl restart open5gs-amfd')


def parseSMF():
    documents = None
    doc2 = None
    try:
        with open(r'/etc/open5gs/smf.yaml') as file:
        # with open(r'smfOld.yaml') as file:
            documents = yaml.safe_load(file)
        with open(r'/home/ubuntu/Open5GS/smf_open5gs_input.yaml') as file2:
        # with open(r'smf_open5gs_input.yaml') as file2:
            doc2 = yaml.safe_load(file2)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    # print(documents["smf"]["pfcp"][0]['addr'])
    try:
        #documents["smf"]["pfcp"][0]['addr'] = netifaces.ifaddresses('ens5')[2][0]['addr']
        documents["smf"]["pfcp"][0]['addr'] = own_ip
        documents["smf"]["sbi"][0]['addr'] = own_ip
        if documents["smf"]["pfcp"][1]['addr'] == "::1":
            del documents["smf"]["pfcp"][1]
        documents["smf"]["subnet"] = doc2["smf"]["subnet"]
        documents["upf"]["pfcp"] = doc2["upf"]["pfcp"]
    except Exception as e:
        print(e)
        exit()

    try:
        # with open('smf.yaml', 'w') as outfile:
        with open('/etc/open5gs/smf.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()
    
    os.system('sudo systemctl restart open5gs-smfd')


def parseUPF():
    documents = None
    doc2 = None
    try:
        with open(r'/etc/open5gs/upf.yaml') as file:
        # with open(r'upfOld.yaml') as file:
            documents = yaml.safe_load(file)
    except Exception as e:
        print(e)
        exit()

    try:
        with open(r'/home/ubuntu/Open5GS/upf_open5gs_input.yaml') as file2:
        # with open(r'upf_open5gs_input.yaml') as file2:
            doc2 = yaml.safe_load(file2)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    # print(documents["upf"])
    try:
        #documents["upf"]["pfcp"][0]['addr'] = netifaces.ifaddresses('ens5')[2][0]['addr']
        #documents["upf"]["gtpu"][0]['addr'] = netifaces.ifaddresses('ens4')[2][0]['addr']
        documents["upf"]["pfcp"][0]['addr'] = own_ip
        documents["upf"]["pfcp"][0]['addr'] = own_ip
        documents["upf"]["subnet"] = doc2["upf"]["subnet"]
    except:
        print("Paths have been changed")

    try:
        with open('/etc/open5gs/upf.yaml', 'w') as outfile:
        # with open('upf.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()
        
    os.system(sudo sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/' /etc/sysctl.conf)
    os.system(sudo sysctl -p)
    os.system(sudo ip tuntap add name ogstun mode tun)
    os.system(sudo ip addr add 10.45.0.1/16 dev ogstun)
    os.system(sudo ip addr add "cafe::1/64" dev ogstun)
    os.system(sudo ip link set ogstun up)
    os.system(sudo iptables -t nat -A POSTROUTING -s 10.45.0.0/16 ! -o ogstun -j MASQUERADE)
    os.system('sudo systemctl restart open5gs-upfd')


def parsePCF():
    documents = None
    try:
        # with open(r'pcfOld.yaml') as file:
        with open(r'/etc/open5gs/pcf.yaml') as file:
            documents = yaml.safe_load(file)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    print(documents["pcf"]["sbi"][0]["addr"])
    try:
        documents["pcf"]["sbi"][0]["addr"] = own_ip
        documents["pcf"]['sbi'][0]['port'] = 7780
    except:
        print("Paths have been changed")

    try:
        # with open('pcf.yaml', 'w') as outfile:
        with open('/etc/open5gs/pcf.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()

    os.system('sudo systemctl restart open5gs-pcfd')


def parseUDR():
    documents = None
    try:
        # with open(r'udrOld.yaml') as file:
        with open(r'/etc/open5gs/udr.yaml') as file:
            documents = yaml.safe_load(file)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    print(documents["udr"]["sbi"][0]["addr"])
    try:
        documents["udr"]["sbi"][0]["addr"] = own_ip
    except:
        print("Paths have been changed")

    try:
        # with open('udr.yaml', 'w') as outfile:
        with open('/etc/open5gs/udr.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()
       
    os.system('sudo systemctl restart open5gs-udrd')

        
def parseNSSF():
    documents = None
    try:
        # with open(r'nssf.yaml') as file:
        with open(r'/etc/open5gs/nssf.yaml') as file:
            documents = yaml.safe_load(file)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    print(documents["nssf"]["sbi"][0]["addr"])
    try:
        documents["nssf"]["sbi"][0]["addr"] = own_ip
    except:
        print("Paths have been changed")

    try:
        # with open('nssf.yaml', 'w') as outfile:
        with open('/etc/open5gs/nssf.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()        

    os.system('sudo systemctl restart open5gs-nssfd')

    
def main():
    if sys.argv[1] == "ausf":
        parseAUSF()
    elif sys.argv[1] == "udm":
        parseUDM()
    elif sys.argv[1] == "nrf":
        parseNRF()
    elif sys.argv[1] == "amf":
        parseAMF()
    elif sys.argv[1] == "smf":
        parseSMF()
    elif sys.argv[1] == "upf":
        parseUPF()
    elif sys.argv[1] == "pcf":
        parsePCF()
    elif sys.argv[1] == "udr":
        parseUDR()
    elif sys.argv[1] == "nssf":
        parseNSSF()
    else:
        print("wrong input")


if __name__ == "__main__":
    main()
