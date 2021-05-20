### Introduction
This is a toy project for learning how subnetting works and how address 
ranges can be split into smaller subnets. The implemented code solves the 
following question:
1. Given an IP-Address and the number of used bits for the subnet mask, how 
   many subnets of a certain size can I create? Example:
   ```
   Given the subnet 141.67.128.0/21, how many /23-subnets can I create? 
   ```
2. The code will also calculate the first and last IP-Address in a given 
   subnet as well as the total number of available IP-Addresses.

###Requirements:
TODO


###How to run:
The following prerequisites are necessary to use the project yourself. I assume
that you are using an linux or macOS system (```<>``` represents a command):

0. Install virtualenv if not already installed
```
python3 -m pip install --user virtualenv
```
1. Create a virtual python environment
```
python3 -m venv <envname>
```
2. Activate the environment in your shell
```
source <envname>/bin/activate
```
3. Install the requirements
```
pip install -r requirements.txt
```
4. In the projects root directory, run
```
python main.py
```

### Input
TODO

### Output

TODO


###Sources:
 - https://www.ittsystems.com/introduction-to-subnetting/
 - http://www.subnetmask.info/
 - https://en.wikipedia.org/wiki/Subnetwork
 - https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/
 - https://subnettingpractice.com/vlsm.html
 - https://www.baeldung.com/cs/get-ip-range-from-subnet-mask
 - https://erikberg.com/notes/networks.html