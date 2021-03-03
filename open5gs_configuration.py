import yaml
import socket
import sys


def find_IP():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        print("IP fetch error")


def change_NRF(document):
    NRF_IP = "132.32.32.32"
    print(document["nrf"]["sbi"][0]["addr"][0])
    document["nrf"]["sbi"][0]["addr"][0] = NRF_IP


def parseAUSF():
    documents = None
    try:
        # with open(r'ausfOld.yaml') as file:
        with open(r'/etc/open5gs/ausfOld.yaml') as file:

            documents = yaml.safe_load(file)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    # print(documents["ausf"]["sbi"][0]["addr"])
    # print("--------------------------------->")
    try:
        documents["ausf"]["sbi"][0]["addr"] = own_ip
        change_NRF(documents)
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


def parseUDM():
    documents = None
    try:
        with open(r'/etc/open5gs/upfOld.yaml') as file:
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
        change_NRF(documents)
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


def parseNRF():
    documents = None
    try:
        # with open(r'nrfOld.yaml') as file:
        with open(r'/etc/open5gs/nrfOld.yaml') as file:
            documents = yaml.safe_load(file)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    # print(documents["nrf"]["sbi"]["addr"][0])
    try:
        documents["nrf"]["sbi"]["addr"][0] = own_ip
    except:
        print("Paths have been changed")

    try:
        # with open('nrf.yaml', 'w') as outfile:
        with open('/etc/open5gs/nrf.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()


def parseAMF():
    documents = None
    try:
        # with open(r'amfOld.yaml') as file:
        with open(r'/etc/open5gs/amfOld.yaml') as file:
            documents = yaml.safe_load(file)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    # print(documents["amf"]["ngap"][0]["addr"])
    try:
        documents["amf"]["ngap"][0]["addr"] = own_ip
        change_NRF(documents)
    except:
        print("Paths have been changed")

    try:
        # with open('amf.yaml', 'w') as outfile:
        with open('/etc/open5gs/amf.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()


def parseSMF():
    documents = None
    doc2 = None
    try:
        with open(r'/etc/open5gs/smfOld.yaml') as file:
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
        documents["smf"]["pfcp"][0]['addr'] = own_ip
        documents["smf"]["pdn"] = doc2["smf"]["pdn"]
        documents["upf"]["pfcp"] = doc2["upf"]["pfcp"]
        change_NRF(documents)
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


def parseUPF():
    documents = None
    doc2 = None
    try:
        with open(r'/etc/open5gs/upfOld.yaml') as file:
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
        documents["upf"]["pfcp"][0]['addr'] = own_ip
        documents["upf"]["gtpu"][0]['addr'] = own_ip
        documents["upf"]["pdn"] = doc2["upf"]["pdn"]
    except:
        print("Paths have been changed")

    try:
        with open('/etc/open5gs/upf.yaml', 'w') as outfile:
        # with open('upf.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()


def parsePCF():
    documents = None
    try:
        # with open(r'pcfOld.yaml') as file:
        with open(r'/etc/open5gs/pcfOld.yaml') as file:
            documents = yaml.safe_load(file)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    print(documents["pcf"]["sbi"][0]["addr"])
    try:
        documents["pcf"]["sbi"][0]["addr"] = own_ip
        change_NRF(documents)
    except:
        print("Paths have been changed")

    try:
        # with open('pcf.yaml', 'w') as outfile:
        with open('/etc/open5gs/pcf.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()


def parseUDR():
    documents = None
    try:
        # with open(r'udrOld.yaml') as file:
        with open(r'/etc/open5gs/udrOld.yaml') as file:
            documents = yaml.safe_load(file)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()
    print(documents["udr"]["sbi"][0]["addr"])
    try:
        documents["udr"]["sbi"][0]["addr"] = own_ip
        change_NRF(documents)
    except:
        print("Paths have been changed")

    try:
        # with open('udr.yaml', 'w') as outfile:
        with open('/etc/open5gs/udr.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()


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
    else:
        print("wrong input")


if __name__ == "__main__":
    main()