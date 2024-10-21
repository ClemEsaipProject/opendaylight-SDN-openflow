# opendaylight-SDN-openflow
opendaylight est un logiciel open source orienté réseau, 
c'est un SDN(software definied networking) qui fournie 
une architecture de contrôle de réseau flexible et modulaire.(Linux fondation)
------------------------------------------------------------------

**prérequis**:
- java
- unzip 
- mininet 

```
  sudo apt update & upgrade -y
  sudo apt-get unzip
  sudo apt-get mininet
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

**Prise en main d'Opendaylight**
```
feature:install odl-restconf odl-l2switch-all odl-msdal-all odl-
```




