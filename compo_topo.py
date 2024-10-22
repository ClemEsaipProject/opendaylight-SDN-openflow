from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def createNetwork():
    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)

    # Ajout du contrôleur OpenDaylight
    c0 = net.addController('c0', controller=RemoteController, ip='192.168.222.137', port=6633)

    # Ajout des switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # Ajout des hôtes
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    h3 = net.addHost('h3', ip='10.0.0.3')
    h4 = net.addHost('h4', ip='10.0.0.4')

    # Ajout du serveur de stockage
    server1 = net.addHost('server1', ip='10.0.0.100')

    # Connexions
    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s2, h3)
    net.addLink(s2, h4)
    net.addLink(s1, server1)
    net.addLink(s2, server1)
    net.addLink(s1, s2)

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createNetwork()
