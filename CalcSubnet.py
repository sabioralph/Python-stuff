import ipaddress as ipAdd
import math
import os
import pandas as pd
def subnet_calc(net,num_subnet):
    try:
        net = ipAdd.IPv4Network(net, strict = False)
        new_prefix_len = net.prefixlen + math.ceil(math.log2(num_subnet))
        subnets = list(net.subnets(new_prefix=new_prefix_len))
        if len(subnets) < num_subnet:
            raise ValueError ("not enough available subnets")
        results = []
        for subnet in subnets [: num_subnet]:
            result = {
                "subnet network address": str(subnet.network_address),
                "Broadcast address": str(subnet.netmask),
                "Number of Usable  hosts":subnet.num_addresses - 2,
                "First Usuable Hosts": str(subnet.network_address + 1),
                "Last usuable host": str(subnet.broadcast_address - 1)
            } 
            results.append(result)
        return results
    except ValueError as e:
        return [{"Error": str(e)}]
    
def main():
    network = input("Enter the network address ex. 192.162.10.0/24: ")
    num_subnet = int(input("Enter the numver of subnets: "))

    results = subnet_calc(network,num_subnet)
    dataFr = pd.DataFrame(results)
    
    scripts_dir = os.path.dirname(os.path.realpath(__file__))
    outFile = os.path.join(scripts_dir,"subnet_calculator_output.csv")
    dataFr.to_csv(outFile,index = False)
    print(f"result saved to0 {outFile}")

if __name__ == "__main__":
    main()