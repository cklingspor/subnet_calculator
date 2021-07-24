import unittest

import Subnetmask

SUBNET_MASKS_GOOD = [
    Subnetmask.SubnetMask("255.0.0.0"),
    Subnetmask.SubnetMask("255.255.0.0"),
]

SUBNET_MASKS_MALFORMED = [
    Subnetmask.SubnetMask("256.0.0"),
    Subnetmask.SubnetMask("-1.0.0"),
]


class TestSubnetMask(unittest.TestCase):
    def test__check_length(self):
        for mask in SUBNET_MASKS_GOOD:
            self.assertTrue(mask.check_octet_length())
        for mask in SUBNET_MASKS_MALFORMED:
            self.assertFalse(mask.check_octet_length())

    def test__check_min_max(self):
        self.assertFalse(Subnetmask.SubnetMask.check_min_max(None, octet=-1))
        self.assertFalse(Subnetmask.SubnetMask.check_min_max(None, octet=128))
        self.assertTrue(Subnetmask.SubnetMask.check_min_max(None, octet=255))
        self.assertTrue(Subnetmask.SubnetMask.check_min_max(None, octet=0))
        self.assertFalse(Subnetmask.SubnetMask.check_min_max(None, octet=256))

    def test__check_octets(self):
        for mask in SUBNET_MASKS_GOOD:
            self.assertTrue(mask.check_octet_values())
        for mask in SUBNET_MASKS_MALFORMED:
            self.assertFalse(mask.check_octet_values())

    def test_valid(self):
        for mask in SUBNET_MASKS_GOOD:
            self.assertTrue(mask.valid())
        for mask in SUBNET_MASKS_MALFORMED:
            self.assertFalse(mask.valid())

        self.assertFalse(Subnetmask.SubnetMask("0.0.0.0").valid())


if __name__ == "__main__":
    unittest.main()
