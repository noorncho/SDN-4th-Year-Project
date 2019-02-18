#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def emptyNet():

    net = Mininet(topo=None, build=False, link=TCLink)

    info( '*** Adding controller\n' )
    net.addController('c0', controller=RemoteController,ip="127.0.0.1",port=6653)

    info( '*** Adding hosts\n' )
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    h5 = net.addHost('h5')
    h6 = net.addHost('h6')
    h7 = net.addHost('h7')
    h8 = net.addHost('h8')
	h9 = net.addHost('h9')
    h10 = net.addHost('h10')
    h11 = net.addHost('h11')
    h12 = net.addHost('h12')
    h13 = net.addHost('h13')
    h14 = net.addHost('h14')
    h15 = net.addHost('h15')
    h16 = net.addHost('h16')

    info( '*** Adding switch\n' )
    s1 = net.addSwitch('s1', cls=OVSSwitch) ##might need to change this to cls=OpenFlow Switch

    info( '*** Creating links\n' )

    ## host - switch
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)
    net.addLink(h5, s1)
    net.addLink(h6, s1)
    net.addLink(h7, s1)
    net.addLink(h8, s1)
	net.addLink(h9, s1)
    net.addLink(h10, s1)
    net.addLink(h11, s1)
    net.addLink(h12, s1)
    net.addLink(h13, s1)
    net.addLink(h14, s1)
    net.addLink(h15, s1)
    net.addLink(h16, s1)

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI(net)

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
