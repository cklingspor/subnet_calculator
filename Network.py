from Subnetmask import SubnetMask


class Network:
    valid = False

    def __init__(self, network_bits, subnet_mask: SubnetMask, ip: str):
        self.subnet_mask = subnet_mask
        self.ip = ip
        self.network_bits = network_bits
        self.host_bits = 32 - network_bits
        self.number_of_ip_adr_per_network = pow(2, self.host_bits)
        # usable ip adr = all ips - broadcast adr - network adr
        self.number_of_usable_ip_adr = self.number_of_ip_adr_per_network - 2
        self.first_ip = self.calculate_first_ip_adr()
        self.last_ip = self.calculate_lasts_ip_adr()
        self.valid = True


    def split_into_equal_sized_subnets(self, required_subnet_size: int):
        """
        Split the Network into multiple subnets. Solves this question:
        Given an address block (e.g. /24), how many '/27'-networks are there
        and what is their CIDR notation?
        Algorithm:
        1. Calculate number of possible subnets in given address block:
            num_of_possible_subnets = pow(2, (required_subnet_size -
            reference_block_size))
        2. Calculate the block size (number of addresses):
            block_size = pow(2, (max_num_bits - required_subnet_size))

        see also: https://www.ittsystems.com/introduction-to-subnetting/

        :param required_subnet_size: Equal to required_subnet_size
        :return: subnets: list : List of subnet ranges
        """
        num_of_possible_subnets = pow(2, (required_subnet_size -
                                          self.network_bits))
        octet_num, max_num_bits = self.__get_subnet_octet(
            suffix=required_subnet_size)
        block_size = pow(2, (max_num_bits - required_subnet_size))
        self.subnets = []
        ip = self.first_ip.split('.')
        origial_octet_val = int(ip[octet_num])
        for idx in range(num_of_possible_subnets):
            ip[octet_num] = str(origial_octet_val + idx * block_size)
            self.subnets.append(f'{".".join(ip)}/{required_subnet_size}')

        return self.subnets

    def __get_subnet_octet(self, suffix):
        """
        Figure out the subnet in which a subnet exists. See_
        https://www.ittsystems.com/introduction-to-subnetting/

        :return:
            octet : int : Zero base octet number.
            max_num_bits : int : Maximum number of bit in the octet.
        """
        if suffix <= 8:
            return 0, 8
        elif 9 <= suffix <= 16:
            return 1, 16
        elif 17 <= suffix <= 24:
            return 2, 24
        elif 24 <= suffix <= 32:
            return 3, 32
        else:
            raise ValueError('Suffix was not in range 0-32')


    def calculate_first_ip_adr(self):
        """Calculate bitwise AND between IP and subnet mask."""
        tmp = []
        for octet_ip, octet_mask in zip(self.ip.split('.'),
                                        self.subnet_mask.octets):
            num = int(octet_ip) & int(octet_mask)
            tmp.append(str(num))

        return '.'.join(tmp)

    def calculate_lasts_ip_adr(self):
        """Calculate the last IP address by adding the bitwise binary
        inverse of the subnet mask to the first IP address."""
        ip = self.first_ip
        tmp = []
        for octet_ip, octet_mask in zip(ip.split('.'), self.subnet_mask.octets):
            a = f'{int(octet_ip):08b}'
            b = self.__invert_binary_number(f'{int(octet_mask):08b}')
            tmp.append(str(int(a, 2) + int(b, 2)))

        return '.'.join(tmp)

    def __invert_binary_number(self, num: str):
        b_dict = {'0': '1', '1': '0'}
        inverse = ''
        for bit in num:
            inverse += b_dict[bit]
        return inverse


class ClassfulNetwork(Network):
    def __init__(self, subnet_mask: SubnetMask, num_of_networks: int, ip: str):
        self.number_of_networks = num_of_networks
        super().__init__(network_bits=subnet_mask.get_mask_suffix(),
                         subnet_mask=subnet_mask,
                         ip=ip)


class ClasslessNetwork(Network):

    def __init__(self, cidr):
        network_bits = int(cidr.split('/')[-1])
        ip = cidr.split('/')[0]
        super().__init__(network_bits=network_bits,
                         subnet_mask=SubnetMask(self.calculate_subnet_mask(
                             network_bits=network_bits)),
                         ip=ip)

    def calculate_subnet_mask(self, network_bits):
        subnet_mask = '1' * network_bits + '0' * (32 - network_bits)
        subnet_mask = self.split_string_into_octets(string=subnet_mask)
        subnet_mask = [str(self.convert_bin_2_decimal(string=x)) for x in \
                       subnet_mask]
        return '.'.join(subnet_mask)

    def split_string_into_octets(self, string):
        tmp = []
        for i in range(0, len(string), 8):
            tmp.append(string[i:i + 8])

        return tmp

    def convert_bin_2_decimal(self, string: str):
        return int(string, 2)

