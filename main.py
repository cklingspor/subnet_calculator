from Network import ClassfulNetwork, ClasslessNetwork
from faker import Faker

from Subnetmask import SubnetMask

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

CLASSFUL_NETWORKS = {
    "class_a": ClassfulNetwork(subnet_mask=SubnetMask('255.0.0.0'),
                               num_of_networks=128,
                               ip='1.0.0.0'),
    "class_b": ClassfulNetwork(SubnetMask('255.255.0.0'),
                               num_of_networks=16384,
                               ip='128.0.0.0'),
    "class_c": ClassfulNetwork(SubnetMask('255.255.255.0'),
                               num_of_networks=2097152,
                               ip='192.0.0.0')
}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    faker = Faker()
    ip = faker.ipv4()
    ip = '10.0.0.0'
    suffix = '20'
    cidr = f'{ip}/{suffix}'

    network = ClassfulNetwork(SubnetMask('255.255.255.0'),
                              num_of_networks=2097152,
                              ip=ip)
    print(network.__dict__)
    network = ClasslessNetwork(cidr=cidr)
    print(network.__dict__)


    ip = '174.53.4.0'
    suffix = '24'
    cidr = f'{ip}/{suffix}'
    network = ClasslessNetwork(cidr=cidr)
    print(network.__dict__)
    subnets = network.split_into_equal_sized_subnets(required_subnet_size=27)
    for elem in subnets:
        print(elem)

    ip = '141.67.128.0'
    suffix = '21'
    cidr = f'{ip}/{suffix}'
    network = ClasslessNetwork(cidr=cidr)
    print(network.__dict__)
    subnets = network.split_into_equal_sized_subnets(required_subnet_size=23)
    for elem in subnets:
        print(elem)
    # print(CLASSFUL_NETWORKS['class_c'].calculate_start_ip_adr())
    # print('Welcome to the subnet calculator!')
    # subnet_mask = SubnetMask('0.0.0.0')
    # while not subnet_mask.valid():
    #     print('Enter subnet mask in dot-format(e.g.:255.0.0.0). Allowed octet values are "0" or "255":')
    #     subnet_mask = SubnetMask(str(input()))
    #     if not subnet_mask.valid():
    #         print("Subnet mask was not valid!")
    #
    # print(subnet_mask)
    #
    #
    #
    # num_subnets = 1
