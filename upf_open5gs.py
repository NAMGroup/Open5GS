import yaml
import socket


def find_IP():
    return socket.gethostbyname(socket.gethostname())


def parseYAML():
    documents = None
    doc2 = None
    try:
        with open(r'./etc/open5gs/upfOld.yaml') as file:
            documents = yaml.safe_load(file)
        with open(r'/home/ubuntu/Open5GS/upf_open5gs_input.yaml') as file2:
            doc2 = yaml.safe_load(file2)
    except Exception as e:
        print("NOT A YAML FILE")
        # print(e)
        exit()

    #    for item, doc in documents.items():
    #        print(item, ":", doc, "\n")

    own_ip = find_IP()
    # print(documents["upf"])
    # print("--------------------------------->")
    documents["upf"]["pfcp"][0]['addr'] = own_ip
    documents["upf"]["gtpu"][0]['addr'] = own_ip
    documents["upf"]["pdn"] = doc2["upf"]["pdn"]
    # print("--------------------------------->")
    # print(documents)

    with open('/etc/open5gs/upf.yaml', 'w') as outfile:
        yaml.dump(documents, outfile, default_flow_style=False)


def main():
    parseYAML()


if __name__ == "__main__":
    main()
