from typing import List


class SubnetMask:
    def __init__(self, mask: str):
        self.mask = mask
        self.octets = mask.split('.')

    def check_octet_length(self) -> bool:
        return True if len(self.octets) == 4 else False

    def check_min_max(self, octet: int) -> bool:
        return True if octet == 0 or octet == 255 else False

    def check_octet_values(self) -> bool:
        tmp = []
        for octet in self.octets:
            tmp.append(self.check_min_max(octet=int(octet)))

        return all(tmp)

    def valid(self) -> bool:
        if self.mask == '0.0.0.0':
            return False
        tmp = [self.check_octet_length(), self.check_octet_values()]

        return all(tmp)

    def get_mask_suffix(self):
        """
        Calculate CIDR number/routing prefix from subnet mask. Use this logic:
        - Split the netmask by dots, so that each octet is in a list.
        - Retrieve binary representation for each octet
        - Convert binary back to string and count '1's
        - Sum over all ones

        Code from: https://cyruslab.net/2020/09/28/python-convert-ipv4-subnet-mask-to-cidr-representation/

        :return:
        """
        tmp: List[int] = []
        for octet in self.mask.split("."):
            tmp.append(str(bin(int(octet))).count("1"))
        return sum(tmp)




if __name__ == '__main__':
    mask = SubnetMask('0.0.0.0')
    print(mask.valid())

