from Network import ClassfulNetwork, ClasslessNetwork

from Subnetmask import SubnetMask


CLASSFUL_NETWORKS = {
    "class_a": ClassfulNetwork(
        subnet_mask=SubnetMask("255.0.0.0"), num_of_networks=128, ip="1.0.0.0"
    ),
    "class_b": ClassfulNetwork(
        SubnetMask("255.255.0.0"), num_of_networks=16384, ip="128.0.0.0"
    ),
    "class_c": ClassfulNetwork(
        SubnetMask("255.255.255.0"), num_of_networks=2097152, ip="192.0.0.0"
    ),
}


def prompt_user_for_ip_and_range():
    """
    Prompt user for input IP and network bits.

    :return: Network: Object representing the given network.
    """
    print("Welcome to the subnet calculator!")

    network = ClasslessNetwork(cidr="174.53.4.0/24")
    network.valid = False
    while not network.valid:
        print(
            "Please enter and IP address and number of network bits (e.g. "
            "174.53.4.0/24)"
        )
        cidr = str(input())
        network = ClasslessNetwork(cidr=cidr)
        if not network.valid:
            print("IP address was not valid!")

    return network


def ask_user_for_required_subnet_size():
    """
    Propmt users for desired size of subnets they want to create.

    :return: int: Disred subnet address range as integer
    """
    range_ok = False
    while not range_ok:
        print("Please enter required subnet size ( network bits < int < 32).")
        required_subnet_size = int(input())
        if 0 < required_subnet_size < 32:
            return required_subnet_size
        else:
            print("Please provide integer between 0 and 32 !")


if __name__ == "__main__":

    network = prompt_user_for_ip_and_range()
    required_subnet_size = ask_user_for_required_subnet_size()
    network.split_into_equal_sized_subnets(
        required_subnet_size=required_subnet_size
    )
    print(network.subnets)
