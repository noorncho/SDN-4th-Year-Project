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

    info( '*** Adding switch\n' )
    s1 = net.addSwitch('s1', cls=OVSSwitch)
    s2 = net.addSwitch('s2', cls=OVSSwitch)
    s3 = net.addSwitch('s3', cls=OVSSwitch)
    s4 = net.addSwitch('s4', cls=OVSSwitch)
    s5 = net.addSwitch('s5', cls=OVSSwitch)
    s0 = net.addSwitch('s0', cls=OVSSwitch) ##may need to be a new class, OpenFlowSwitch

    info( '*** Creating links\n' )

    ## host - switch
    net.addLink(h1, s1)
    net.addLink(h2, s2)
    net.addLink(h3, s3)
    net.addLink(h4, s4)
    net.addLink(h5, s5)

    ## switches
    net.addLink(s1, s0)
    net.addLink(s2, s0)
    net.addLink(s3, s0)
    net.addLink(s4, s0)
    net.addLink(s5, s0)
	
    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI(net)

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
