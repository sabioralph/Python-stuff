This is a calculator for subnets and it sends the result of the calculation using data frame. I got this idea from a youtube video.
The formula for this is, usable hosts. So /24 as an example means 32 bit - the 24 bit (the CIDR) means the last 8 bits are for hosts portion
2 ^ 8 = 256, thats the total address. But we have to reserve the network and broadcast addresses so we have 256- 2 = so only 254 usablehopst ip address.
so for this example: 192.168.10.0/24, the first address is 192.162.10.1 and the last one is at 192.162.10.254.Also it will depend on the number of subnets you want to use, you have to divide it by how many subnets you have ( ex 4 subnets , 256 / 4 = 64 thus  .1 and .62 is the usable host on the first network and .0 and .63 is the network and broadcast address respectively).
You can also read the output during my testing for this program


