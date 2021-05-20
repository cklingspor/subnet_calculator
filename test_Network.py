import unittest
from unittest import TestCase

from Network import ClassfulNetwork, ClasslessNetwork
from faker import Faker

from Subnetmask import SubnetMask

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

CLASSLESS_NETWORKS = {
    "1": ClasslessNetwork(cidr='192.168.0.10/24'),
    "2": ClasslessNetwork(cidr='192.168.0.10/30'),
    "3": ClasslessNetwork(cidr='10.0.0.0/20')
}


class TestNetwork(TestCase):
    def test_split_into_equal_sized_subnets(self):
        cidrs = ['174.53.4.0/24', '141.67.128.0/21', '131.80.0.0/12']
        correct_subnets = [
            ['174.53.4.0/27',
             '174.53.4.32/27',
             '174.53.4.64/27',
             '174.53.4.96/27',
             '174.53.4.128/27',
             '174.53.4.160/27',
             '174.53.4.192/27',
             '174.53.4.224/27'],
            ['141.67.128.0/23',
             '141.67.130.0/23',
             '141.67.132.0/23',
             '141.67.134.0/23'],
            ['131.80.0.0/13',
             '131.88.0.0/13']
        ]
        required_subnet_sizes = [27, 23, 13]
        for cidr, correct, required_subnet_size in zip(cidrs,
                                                       correct_subnets,
                                                       required_subnet_sizes):
            network = ClasslessNetwork(cidr=cidr)
            subnets = network.split_into_equal_sized_subnets(
                required_subnet_size=required_subnet_size)
            self.assertEqual(correct, subnets)

    def test_calculate_first_ip_adr_classful(self):
        for network, ip in zip(CLASSFUL_NETWORKS.values(), ['1.0.0.0',
                                                            '128.0.0.0',
                                                            '192.0.0.0']):
            self.assertEqual(ip, network.first_ip)

    def test_calculate_lasts_ip_adr_classful(self):
        for network, ip in zip(CLASSFUL_NETWORKS.values(), ['1.255.255.255',
                                                            '128.0.255.255',
                                                            '192.0.0.255']):
            self.assertEqual(ip, network.last_ip)

    def test_calculate_first_ip_adr_classless(self):
        for network, ip in zip(CLASSLESS_NETWORKS.values(), ['192.168.0.0',
                                                             '192.168.0.8',
                                                             '10.0.0.0']):
            self.assertEqual(ip, network.first_ip)

    def test_calculate_lasts_ip_adr_classless(self):
        for network, ip in zip(CLASSLESS_NETWORKS.values(), ['192.168.0.255',
                                                             '192.168.0.11',
                                                             '10.0.15.255']):
            self.assertEqual(ip, network.last_ip)


if __name__ == '__main__':
    unittest.main()