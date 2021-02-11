import yaml
import socket


def find_IP():
    # This function finds the IP of the VNF that it is implemented on.
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        print("IP fetch error")


def parseYAML():
    # This function parses the yaml file and configure it according to the
    # upf_open5gs_input.yaml file.
    documents = None
    doc2 = None
    try:
        # The yaml library of python doesn't support keeping the comments during 
        # parsing. So upf.yaml is renamed in upfOld.yaml and after the configuration 
        # a new one is created. Now there are two files: 
        # - upf.yaml: the configured one
        # - upf.yaml: the original file with the comments
        with open(r'/etc/open5gs/upfOld.yaml') as file:
            documents = yaml.safe_load(file)
        with open(r'/home/ubuntu/Open5GS/upf_open5gs_input.yaml') as file2:
            doc2 = yaml.safe_load(file2)
    except Exception as e:
        print(e)
        exit()

    own_ip = find_IP()

    try:
        # Configuration of the yaml file
        documents["upf"]["pfcp"][0]['addr'] = own_ip
        documents["upf"]["gtpu"][0]['addr'] = own_ip
        documents["upf"]["pdn"] = doc2["upf"]["pdn"]
    except:
        print("Paths have been changed")


    try:
        # Creation of the new upf.yaml 
        with open('/etc/open5gs/upf.yaml', 'w') as outfile:
            yaml.dump(documents, outfile, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()


def main():
    parseYAML()


if __name__ == "__main__":
    main()
