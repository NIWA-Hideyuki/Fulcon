## Fulcon VirtualPlatform

`Fulcon` is the system container tool.

## State of the project

In Fulcon, the container can be handled like VM.
Fulcon constructs the system by generating the container, logging in 
from the console, and installing the package with yum and apt, and stops 
the system with shutdown command.The container can be connected directly with
the Internet by adding virtual NIC.
Fulcon can handle CentOS 7 and Ubuntu 15.04

### Install pacage

ubuntu

$  sudo apt-get install docker.io python-ipy bridge-utils  
$  sudo systemctl enable docker.service
$  sudo systemctl start docker.service
$  sudo dpkg -i fulcon_0.3_amd64.deb
$  sudo systemctl enable fulcon.service
$  sudo systemctl start fulcon.service

CentOS

$  sudo yum install docker-io python-IPy bridge-utils  
$  sudo systemctl enable docker.service
$  sudo systemctl start docker.service
$  sudo rpm -ivh fulcon-0.3-1.el7.centos.x86_64.rpm
$  sudo systemctl enable fulcon.service
$  sudo systemctl start fulcon.service
 
### Building:

ubuntu

$  sudo apt-get install docker.io python-ipy bridge-utils  
$  sudo systemctl enable docker.service
$  sudo systemctl start docker.service
$  tar xzf fulcon.tgz  
$  cd fulcon  
$  sudo make install  
$  sudo systemctl enable fulcon.service
$  sudo systemctl start fulcon.service
  
CentOS 7  
  
$  sudo yum install docker-io python-IPy bridge-utils  
$  sudo systemctl enable docker.service
$  sudo systemctl start docker.service
$  tar xzf fulcon.tgz  
$  cd fulcon  
$  sudo make install  
$  sudo systemctl enable fulcon.service
$  sudo systemctl start fulcon.service
  
### Setup:  
  
1) The image of CentOS 7, Ubuntu15.04 and Ubuntu15.10 is prepared.  
  
$  sudo fulcon setup -d centos7  
$  sudo fulcon setup -d ubuntu1504  
$  sudo fulcon setup -d ubuntu1510  
  
It takes the minute to several ten completion.
It only has to execute only the kind of the image to be used.
This operation do only first once.

The image is builded by using Dockerfile.
If it does not go well.images are generated with following Dockerfile.  
     /var/lib/fulcon/driver/dockerfile/centos7/Dockerfile  
     /var/lib/fulcon/driver/dockerfile/ubuntu1504/Dockerfile  
     /var/lib/fulcon/driver/dockerfile/ubuntu1510/Dockerfile  
It must be builded "fulcon/centos7", "fulcon/ubuntu1504" and "fulcon/ubuntu1510"

2) The image of default is set.  
  
$  sudo fulcon set-default-image fulcon/centos7  
or  
$  sudo fulcon set-default-image fulcon/ubuntu1504  
or  
$  sudo fulcon set-default-image fulcon/ubuntu1510  
  
fulcon/centos7 is set in the following examples.  
  
### Using:  
  
#### 1.Generation of container  

In the following example, the container "webap-server" is generated.
  
$  sudo fulcon sysgen webap-server  
  
The container of "fulcon/centos7" was generated.
It is optional -c, and "fulcon/ubuntu1504" can be specified.
  
$  sudo fulcon sysgen -c fulcon/ubuntu1504 another-server  
  
#### 2.The user is added, and the password is set.  
  
In the following example, the user "niwa" is seted.
The last argument is set to passwd.
  
$  sudo fulcon add-user webap-server niwa 
 
Please use optional "-s" to give the sudo right to the user.
  
$  sudo fulcon add-user -s webap-server tom

Please use the "set-passwd" sub-command if you want to change the password.
 
$  sudo fulcon set-passwd webap-server niwa
 
The "del-user" subcommand is used to delete the user from the container. 
 
$  sudo fulcon del-user webap-server tom
 
#### 3.Virtual NIC addition  
  
$  sudo fulcon net-add webap-server 192.168.17.2/24 1
  
Information of network is able to be taken  by "fulcon net-info".  
 
$  sudo fulcon net-info  
  
When the network is connected with host's device in the container it, 
optional "-d" is used. 
IP-address specifies it within the range of same netmask as the shared device. 
 
In the following example, when it is NIC "eth1" and the address is 
"192.168.0.2/24", "192.168.0.12/24" is allocated in the container.
 
$ sudo fulcon net-add -d eth1 webap-server 192.168.0.12/24 1
  
#### 4.Attache console to the container.
  
$  sudo fulcon console webap-server  
 
You return from the console to the host if you do "Exit".
  
#### 5.When you login the container, yum and apt can be used.  
   You can login with ssh.  
   "shutdown -h now" can be used in container.  
  
#### 6.Stop and start of container  
  
$  sudo fulcon stop webap-server  
  
$  sudo fulcon start webap-server  
  
#### 7.List containers  
  
$  sudo fulcon list 
  
#### 8.Erase container  
  
$  sudo fulcon erase webap-server  
 
 
 
### ALL Sub command:  
```
  
  
add-user [ -n REAT_NUMBER ] [ -s ] CONTAINER_NAME USER [PASSWORD ]  
     A new user is registered in OS of the container.  
     The password is set with PASSWORD.  
     The password is interactively set when there is no PASSWORD.  
     -n REAT_NUMBER  
          It is specified to the container name that CONTAINER_NAME and 
          the number combined.
          ex) "AB" and 3 : AB0001, AB0002, AB0003  
     -s 
          The user gets administrator's rights.  
  
br-add BRIDGE_NUMBER ( IPADDR/MASK | NET_DEVICE ]
     The IP-address or the device is registered in the bridge.
  
br-del BRIDGE_NUMBER ( IPADDR/MASK | NET_DEVICE ]
     The IP-address or the device is deleted in the bridge.
  
br-info
     Information on the bridge where NIC that adds it is connected is displayed.  
  
clone CONTAINER_NAME NEW_IMAGENAME
     A new image is made from the container.  
     New containers of the same content can be made from a new image.  
  
console [ -n REPEAT_NUMBER ] CONTAINER_NAME  
     It enters the container with the console.   
     -n REAT_NUMBER  
          It is specified to the container name that CONTAINER_NAME and 
          the number combined.
          ex) "AB" and 3 : AB0001, AB0002, AB0003  
  
default-image  
     The default image that generates the container is displayed.  
  
del-image IMAGE_NAME ...  
     The specified image is deleted.   
  
del-ocf IMAGE_NAME  
     The specified OCF image is deleted.   
     (The OCF image becomes basic that generates the container.)  
  
del-user CONTAINER_NAME USERNAME  
     The user specified in the container is deleted.  
  
deploy [ -c IMAGE ] SRC_FILE DEST_PATH 
     SRC_FILE on the host is copied in DEST_PATH of all containers.  
     -c IMAGE
          Only a container of IMAGE is made the target.  
          IMAGE is the part of the image name.  
  
dirver-name  
     The container system that uses it as a driver of fulcon is displayed.  
  
erase CONTAINER_NAME  ...  
erase -n REPEAT_NUMBER CONTAINER_NAME  
     The specified container is deleted.   
     -n REAT_NUMBER  
          It is specified to the container name that CONTAINER_NAME and 
          the number combined.
          ex) "AB" and 3 : AB0001, AB0002, AB0003  
  
help  
     Use is displayed.  
  
image-catalog  
     The list of the registered image is displayed.  
  
list  
     The list of the made container is displayed.  
  
load-ocf IMAGE_NAME  
     The OCF image is loaded as an image used for the container.  
  
ls-image  
     The list of the image is displayed.  
  
ls-ocf  
     The list of the OCF image is displayed.  
  
net-add [-d NIC_DEVICE] [-g GATEWAY] [-b BRIDGE_NUMBER ] CONTAINER_NAME IP_ADDR/MASK VETH_NUMBER
     NIC is added to the container.   
     -d NIC_DEVICE  
          The device to connect it to an external network is specified.   
     -g GATEWAY
          GATEWAY that is used in the container
     -b BRIDGE_NUMBER
          BRIDGE that combines "'fulcon' and specified number" is added.  
          ex) BRIDGE_NUMBER is 2 -> nic "fulcon2"  
     VETH_NUMBER  
          NIC that combines "Container name and specified number" is added.  
          ex) VETH_NUMBER is 1 and container is "abc" -> nic "abc1"  
  
net-del CONTAINER_NAME VETH_NUMBER
     NIC is deleted from the container.   
     VETH_NUMBER  
          NIC that combines "Container name and specified number" is added.  
          ex) VETH_NUMBER is 1 and container is "abc" -> nic "abc1"  
  
net-info NAME  
     Information on the network where NIC that adds it is connected is displayed.  
  
rename   CONTAINER_NAME NEW_NAME  
     The container name is renamed.  
  
resource [-c CPU] [-n CPUSET] [-m MEM] NAME   
     The resource allocated in the container is displayed if there is no "-c, -n, -m" option.  
     -c CPU  
          The ratio of allocated CPU is % specified.   
     -n CPUSET  
          The allocated CPU number is specified.  
     -m MEM  
          The allocated memory size are specified.  
          "M" and "G" can be used for the unit.  
  
resume   NAME  
     Resume does the container in the state of PAUSED by suspend.  
  
save-ocf IMAGE_NAME  
     The OCF image is saved as an image used for the container.  
  
set-default-image [ IMAGE_NAME ]  
     Default image is set.  
     The default image that generates the container is displayed.  
  
set-passwd NAME USERNAME  
     User's password in the container is set.  
  
setup [[ -d ][ -n ] [ -p ] IMAGE_NAME ]
     The image is newly made.
     -d
          New image is downloaded from docker repositry.
     -n
          Generates a new image from a Dockerfile.
     -p  
          Proxy is set.  
          The value of the environment variable "Http_proxy, https_proxy, and ftp_proxy" is used.  
     The image is generated from HOST if there is no argument.
  
update-prog [ -c IMAGE ] COMMAND 
     The same command is carried out by more than one container.  
     -c IMAGE
          Only a container of IMAGE is made the target.  
          IMAGE is the part of the image name.  
  
start CONTAINER_NAME ...  
start -n REPEAT_NUMBER CONTAINER_NAME  
     The container of the specified name is started.  
     -n REAT_NUMBER  
          "User and password" is set to the container of  
          the name that NAME and the figure combined.  
          ex) "AB" and 3 : AB0001, AB0002, AB0003  
  
stop NAME  ...  
stop -n REPEAT_NUMBER NAME  
     The container of the specified name is stopped.   
     -n REAT_NUMBER  
          "User and password" is set to the container of  
          the name that NAME and the figure combined.  
          ex) "AB" and 3 : AB0001, AB0002, AB0003  
  
suspend   CONTAINER_NAME  
     The container of the specified name is suspended.  
  
sysgen [ -c IMAGE ] NAME NAME ...  
sysgen -n REPEAT_NUMBER  [ -c IMAGE ] NAME  
     The container of the specified name is generated.  
     -n REAT_NUMBER  
          "User and password" is set to the container of  
          the name that NAME and the figure combined.  
          ex) "AB" and 3 : AB0001, AB0002, AB0003  
  
update  
     All containers are renewed.   
     "Yum update" is done in centos. In ubuntu,   
     "Apt-get update" and "Apt-get upgrade" are done.   
  
  

```


