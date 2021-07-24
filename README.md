### Introduction
This project serves a toy project to learn how subnetting works and 
how address ranges can be split into smaller subnets. The implemented code 
solves the following question:
1. Given an IP-Address and the number of used bits for the subnet mask, how 
   many subnets of a certain size can I create? Example:
   ```
   Given the subnet 141.67.128.0/21, how many /23-subnets can I create? 
   ```
2. The code will also calculate the first and last IP-Address in a given 
   subnet as well as the total number of available IP-Addresses.

###Requirements:
TODO

### What is subnetting?
A subnet is a small network within a larger network. Subnets are used to 
make network traffic more efficient and safer. In big IT networks there are 
a lot of possible routes. To limit the number of routers the network 
traffic has to pass subnets provide a great tool to limit the number of 
possible routes within a network by "cutting" out a small portion of the 
available IP-Addresses and put them into a smaller network - the so-called 
subnet.
This subnet is then a part of the bigger network range but traffic does not 
leave the subnet, if it is directed at IP-Addresses from the same subnet.

#### IP Address
Every device that connects to a network (i.e. the internet) is assigned an 
unique IP (Internet Protocol) address. This IP serves as an identifier that 
is used every time a packet s sent ot the device. Every IP address consists 
of 4 so-called octets. Every octet consists of 8 Bit. For example: The first 
octet of the IP address  ``10.28.65.20`` would be `10 = 00001010`. 
The whole IP address in binary would look like this= 

``10.28.65.20 = 00001010.00011100.01000001.00010100``

#### Subnetmasks
A subnet mask is similar to an IP address but is only used within a network. 
Both elements are necessary to route a package to the intended destination. 
The subnet mask serves as an identifier for a network range in which a 
certain IP address is located. Or to be ver precise: **A subnet mask is the 
representation of the network portion of an address**.

##### Classful Networks
Every IP address can be divided into a network and host part. This does look 
like the following: Originally, IP address were designed to be part of a 
network class ranging from Class A to Class E. Commonly used are the classes 
A-C. In those classes IP addresses were split after 8 bit (Class A), 16 bit 
(Class B) and 24 bit (Class C). This leaves 24, 16 or 8 bits for the host 
identifier. This is also shown in Figure (1)
![classful networks](./images/IP-Class-Range.png "Figure 1")

##### Classless Networks
Today, most networks are classes to allow for a more flexible sizing of 
networks. In 1993, Classless Inter-Domain Routing (CIDR) was introduced. 
Since then, network ranges can be of every size (with a few exceptions). An 
IP address with CIDR notation allows for a concise notation of an IP address 
together with its subnet mask. A former class C network would be written as 
``192.168.2.1/24`` where the `24` identify the number of network bits ( the  
so-called network prefix).

#### Why use subnetting?
Subnetting has, among others, the following advantages:
* Reduce the number of unused IP addresses in a subnet  by tailoring the 
  subnet size to the actual number of IP addresses needed
* Subnetting improves the network performance since in smaller networks 
    there will be less traffic.
  

### How the calculations are done
#### Number of usable IP addresses
The number of usuable Ip addresses within a subnet is calculated as follows:
```num_of_usuable_ips = 2^host_bits - 2 ```

We have to subtract two addresses for network and the broadcast address.

#### Number of Subnets in an address block
To solve question 1 (`Given the subnet 141.67.128.0/21, how many /23-subnets 
can I create?`) the following formula can be used
`num_of_subnets = 2^(required_subnet_size - reference_block_size)`
Source: [https://www.ittsystems.com/introduction-to-subnetting/](https://www.ittsystems.com/introduction-to-subnetting/)

#### Calculate the list of subnets
After calculating how many subnets of a certain size are contained in an 
address block, it is possible to count the exact address range for each 
possible subnet. This can be done in the following steps:
1. Calculate in which octet the subnets exists. 
    * First octet: Network prefix `[/1, /8]`
    * Second octet: Network prefix `[/9, /16]`
    * Third octet: Network prefix `[/17, /24]`
    * Fourth octet: Network prefix `[/25, /32]` 
2. Take the biggest network prefix number. E.g.: `/16` for a subnet within 
   the second octet.
3. Calculate the block size of the subnet. Remember, the block size 
   represents the number of possible IP addresses within the subnet in 
   question. Formula (equal to the total number of IP addresses):
   `block_size = 2^(reference_block_size - required_subnet_size)`.
4. Calculate the address ranges by starting with the first provided network 
   and increment by the block size. 
   
#####Example:
Given the network `174.53.4.0/24`, how many `/27` networks exists and 
what are their address ranges?

0. (Calculate the number of subnets: `num_of_subnets = 2^(27 - 24) = 2^3 = 8`) 
1. The subnet exists within the 4th octet
2. The highest network prefix is 32
3. Block size: `block_size = 2^(32 - 27) = 2^5 = 32`

Therefore, the possible subnets would be:
* 174.53.4.0/27
* 174.53.4.32/27
* 174.53.4.64/27
* 174.53.4.96/27
* 174.53.4.128/27
* 174.53.4.160/27
* 174.53.4.192/27
* 174.53.4.224/27

Note, that this list only contains the address ranges for the subnets. The 
usable IP addresses range from `first_usable_adr = start_ip +1` (since 
`start_ip` == network address) to `last_usable_adr = last_ip - 1 = 
network_adr_next_subnet -2`

Source for example: [https://www.ittsystems.com/introduction-to-subnetting/](https://www.ittsystems.com/introduction-to-subnetting/)

### Variable Length Subnet Masks (VLSM)
TODO

###How to run:
The following prerequisites are necessary to use the project yourself. I assume
that you are using a linux or macOS system:

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