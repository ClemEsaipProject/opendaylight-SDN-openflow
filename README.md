# opendaylight-SDN-openflow
opendaylight est un logiciel open source orienté réseau, 
c'est un SDN(software definied networking) qui fournie 
une architecture de contrôle de réseau flexible et modulaire.(Linux fondation)
------------------------------------------------------------------

**prérequis**:
- java
- unzip 
- mininet
- python

```
  sudo apt update & upgrade -y
  sudo apt-get install unzip
  sudo apt-get install mininet
  sudo apt-get install python3
  
```
-------------------------------------------------------------------
**installation de JAVA**
```
sudo apt-get install openjdk-8-jre
sudo update-alternatives --config java
sudo echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre' #source ~/.bashrc
echo $JAVA_HOME
```
--------------------------------------------------------------------
**installation de opendaylight**
```
sudo wget https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/opendaylight/0.10.0/
unzip karaf
cd karaf/bin
sudo ./karaf
```
![image](https://github.com/user-attachments/assets/bf4e9a36-a4b1-4218-888e-8b985f70bd4a)


**Prise en main d'Opendaylight**
```
feature:install odl-restconf odl-l2switch-switch odl-dluxapps-topology odl-dluxapps-yangman odl-dluxapps-yangui
```
```
ip a or ifcong
```
recupere votre ip et ouvré votre navigateur à l'adresse http://votre_ip:8181/index.html#/
![image](https://github.com/user-attachments/assets/ec083590-dfec-4d97-9fa4-d5baf133d9fc)


Ajout des differentes équipements
**script**
download python files compo_topo.py
![image](https://github.com/user-attachments/assets/e82c3df4-7016-4eb4-a0b5-59583ca33c9d)

use mininet for make simple request ``pingall` & `links` & `net`
![image](https://github.com/user-attachments/assets/02ef416a-ab86-4244-a7c0-ae0fc625b353)


