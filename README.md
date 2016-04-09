Fulcon / Slot-OS Platform 0.4    Copyright (C) 2015-2016 NIWA Hideyuki
    Apache License Version 2.0

## What is Fulcon/Slot-OS?

- Slot-OS divides the HOST machine into two or more software partitions (slot). 
- Each slot can be operated like another machine of the same composition. 
- Root of the Fulcon/Slot-OS container has a strong root authority, and the same operation as root of HOST is possible. 
- The slot can dynamically compose the network. (SDN function)

## Function of Fulcon/Slot-OS
- Function to divide machine into two or more slots
- Function to generate image for slot from rootfs of HOST
- Dynamic addition and deletion (SDN) function of two or more Internet Protocol addresses
- Allocation of resource of each slot (CPU%, number of CPU, and memory size) and dynamic modification function
- Console function of slot
- Listing function of the entire slot
- Suspension (temporary stop) and resume of slot
- Automatic update-function of two or more slots
- High-speed backup function

Fulcon can handle CentOS 7, Ubuntu 15.04, 15.10, Fedora 23

### Install package

ubuntu

$  sudo apt-get install docker.io python-ipy bridge-utils openvswitch-switch
$  sudo systemctl enable docker.service
$  sudo systemctl start docker.service
$  sudo dpkg -i fulcon_0.4_amd64.deb
$  sudo systemctl enable fulcon.service
$  sudo systemctl start fulcon.service

CentOS, Fedora

$  sudo yum install docker-io python-IPy bridge-utils openvswitch
$  sudo systemctl enable docker.service
$  sudo systemctl start docker.service
$  sudo rpm -ivh fulcon-0.4-1.el7.centos.x86_64.rpm
$  sudo systemctl enable fulcon.service
$  sudo systemctl start fulcon.service
 
### Building:

ubuntu

$  sudo apt-get install docker.io python-ipy bridge-utils openvswitch-switch
$  sudo systemctl enable docker.service
$  sudo systemctl start docker.service
$  tar xzf fulcon.tgz  
$  cd fulcon  
$  sudo make install  
$  sudo systemctl enable fulcon.service
$  sudo systemctl start fulcon.service
  
CentOS, Fedora
  
$  sudo yum install docker-io python-IPy bridge-utils openvswitch
$  sudo systemctl enable docker.service
$  sudo systemctl start docker.service
$  tar xzf fulcon.tgz  
$  cd fulcon  
$  sudo make install  
$  sudo systemctl enable fulcon.service
$  sudo systemctl start fulcon.service
  
### Setup:  

#### 1. Generation of OS image (make-base-image subcommand)

If the slot-os image has not been generated yet, the slot-os image is necessary as OS of slot. 
Rootfs for slot is generated from rootfs of HOST. 
It takes 50 minutes from ten minutes for generation. (Depend on the machine performance and the size of rootfs. )
  
$  sudo fulcon make-base-image

#### 2. Making of Slot partition (build subcommand)
- HOST is divided into two or more slot. 
- The resource of Slot is automatically initialized. 
  CPU% = (all CPU the number)*100% / (slot number) 
  allocation CPU = all CPU the number
  CPU MEMORY =  512MB
- When 0 is specified for a number of Slot, all slot is deleted. 

The following examples divide HOST into three. 

$ sudo Slot-OS build 3
  
### Using:  
  
#### 3.The display the list of slot (list subcommand) 
The "list of slot" is displayed. 
Slot number, state, slot name, CPU%, CPU allocation, and memory size, 
autostart, image names, and Internet Protocol addresses

$ sudo slot-os list
 0 : RUNNING  slot00 66 % 0-1 512m A Slot-OS 172.17.0.2
 1 : STOPPED  slot01 66 % 0-1 512m - Slot-OS
 2 : STOPPED  slot02 66 % 0-1 512m - Slot-OS

#### 4. Boot of slot (start subcommand)
All slot or of specify slot is booted by the number. 

The 0th slot is booted. 
$ sudo slot-os start 0
$ sudo slot-os list
 0 : RUNNING  slot00 66 % 0-1 512m A Slot-OS
 1 : STOPPED  slot01 66 % 0-1 512m - Slot-OS
 2 : STOPPED  slot02 66 % 0-1 512m - Slot-OS

All slot is booted. 
$ sudo slot-os start all
$ sudo slot-os list
 0 : RUNNING  slot00 66 % 0-1 512m A Slot-OS
 1 : RUNNING  slot01 66 % 0-1 512m - Slot-OS
 2 : RUNNING  slot02 66 % 0-1 512m - Slot-OS

#### 5. Console of Slot
The console of Slot number 0 is opened. 

$ sudo slot-os console 0

#### 6. Update and package application (update, update-prog, and update-deploy subcommand)

It is an automatic update as for the package of all slot. 

$ sudo slot-os update all

The package is copied under/root of all slot. 

$ sudo slot-os deploy all : perl-XML-Parser-2.41-8.el7.x86_64.rpm /root

The package copied with all slot is installed. 

$ sudo slot-os update-prog all : rpm -ivh /root/perl-XML-Parser-2.41-8.el7.x86_64.rpm

The package copied with all slot is deleted. 

$ sudo slot-os update-prog all : rm -f /root/perl-XML-Parser-2.41-8.el7.x86_64.rpm

#### 7. Stop and renewal of slot (start, stop, suspend, and resume subcommand)

Shutdown

$ sudo slot-os stop 0

Boot

$ sudo slot-os start 0

Temporary stop (suspension)

$ sudo slot-os suspend 0

Restart

$ sudo slot-os resume 0

#### 8. Backup and restoration of slot (backup and restore subcommand)

Backup of slot

$ sudo slot-os backup 0 bkup1

"bkup1" describes it on of putting on the backup name. Anything is good 
in the alphanumeric character. 
The backup image name is as follows. 
slot00.bkup1

Restoration of backup

$ sudo slot-os backup-restore 0 slot00.bkkup1

List of backup

$ sudo slot-os backup-list

The initialization of slot restores slot-os. 

$ sudo slot-os backup-restore 0 slot-os

#### 9. Dynamic addition and deletion of network (net-add and net-del subcommand)

When Slot is booted, the network of 172.17.0.0/16 is added. 
This Internet Protocol address changes at each boot. 
NAT setting of network of 172.17.0.0/16

Internet Protocol address is added. The address of 192.168.18.2/24 is added to 0 of 
Slot as the first NIC. 

$ sudo slot-os net-add 0 192.168.18.2/24 1

Addition of second NIC

$ sudo slot-os net-add 0 192.168.78.3/24 2

The state of NIC is displayed. 

$ sudo slot-os net-info
slot00	eth0		172.17.0.2/16
slot00	vgslot00_1	192.168.18.2/24
slot00	vgslot00_2	192.168.78.2/24

Internet Protocol address is deleted. 
IP of the second of Slot 0 are deleted. 

$ sudo slot-os net-del 0 2

#### 10. NIC of HOST is shared (net-nic-add and net-nic-del subcommand). 

Outside HOST and slot communicates sharing NIC of HOST. 
The NIC name of HOST : with ens7f1 for address 10.124.23.91/24. 

$ sudo slot-os net-nic-add ens7f1

It adds it to the third Slot 0 by 10.124.23.101/24. 

$ sudo slot-os net-add 0 10.124.23.101/24 3

It comes to be able to access slot 0 outside HOST by 10.124.23.101. 

NIC(ens7f1) of HOST is removed. 

$ sudo slot-os net-nic-del ens7f1


### ALL Sub command:  
```
  
auotstart NAME [ on | off ] ( all | SLOT_NUMBER...)
     NAME is started automatically at the time of a system restart.

backup NUMBER NEW_NAME
     slot in NUMBER is backuped. A backup will be slotXX.NEW_NAME.

backup-del IMAGE_NAME
     A backup of IMAGE_NAME is erased.

backup-list
     A list of backups is indicated.

backup-restore SLOT_NUMBER BACKUP_IMAGE
     backup image is restored in slot.

br-add BRIDGE_NUMBER ( IPADDR/MASK | NET_DEVICE ]
     The IP-address or the device is registered in the bridge.
  
br-del BRIDGE_NUMBER
     The IP-address or the device is deleted in the bridge.
  
br-info
     Information on the bridge where NIC that adds it is connected is displayed.  
  
build NUMBER
     HOST is separated in NUMBER and slot is made.
     When 0 is specified, all slot is erased.

list [ -c ] [ NAME ]
     The list of the made slot is displayed.  
     Display term is as follows.
       NUM, Status, Container name, CPU%, CPUS, Memory, Autostart(A or -), Image name, IP address
     -c 
          It always keeps indicating list. When stopping, ^c is pushed.

help
     Help is displayed.  


list [ SLOT_NUMBER ]
     The list of the made slot is displayed.  

make-base-image
     fulcon/slot-os image is generated from HOST.
     It even takes tens of minutes for completion.

net-add SLOT_NUMBER IPADDR/MASK NIC_NUMBER 
     NIC is added to the slot.   

net-del SLOT_NUMBER NIC_NUMBER
     NIC is deleted from the slot.   

net-info [ NAME ]
     Information on the network where NIC that adds it is connected is displayed.  


resource [-c CPU] [-n CPUSET] [-m MEM] ( all | NUMBER ... )
     The resource allocated in the slot is displayed if there is no "-c, -n, -m" option.  
     -c CPU  
          The ratio of allocated CPU is % specified.   
     -n CPUSET  
          The allocated CPU number is specified.  
     -m MEM  
          The allocated memory size are specified.  
          "M" and "G" can be used for the unit.  
  

resume ( all | NUMBER ... )
     Resume does the slot in the state of SUSPENDED by suspend.  

start ( all | NUMBER ... )
     The slot of the specified NUMBER is started.  


stop ( all | NUMBER ... )
     The slot of the specified NUMMBER is stopped.   


suspend ( all | NUMBER ... )
     The NUMBER of the specified NUMBER is suspended.  


update ( all | NUMBER ...)
     All slot os packages are updated.   
     "Yum update" is done in centos. In ubuntu,   
     "Apt-get update" and "Apt-get upgrade" are done.   


update-prog ( all | NUMBER ... ) : COMMAND
     A COMMAND program for update is executed in NUMBER of slot.


update-deploy NUMBER ... : SRC_FILE DEST_PATH
     SRC_FILE on the HOST is copied in DEST_PATH of NUMBER of slot.  


  

```


