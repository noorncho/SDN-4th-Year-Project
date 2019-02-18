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
    s1001 = net.addSwitch('s1001', cls=OVSSwitch)
    s1002 = net.addSwitch('s1002', cls=OVSSwitch)
    s1003 = net.addSwitch('s1003', cls=OVSSwitch)
    s1004 = net.addSwitch('s1004', cls=OVSSwitch)
	s2001 = net.addSwitch('s2001', cls=OVSSwitch)
    s2002 = net.addSwitch('s2002', cls=OVSSwitch)
    s2003 = net.addSwitch('s2003', cls=OVSSwitch)
    s2004 = net.addSwitch('s2004', cls=OVSSwitch)
	s2005 = net.addSwitch('s2005', cls=OVSSwitch)
    s2006 = net.addSwitch('s2006', cls=OVSSwitch)
    s2007 = net.addSwitch('s2007', cls=OVSSwitch)
    s2008 = net.addSwitch('s2008', cls=OVSSwitch)
	s3001 = net.addSwitch('s3001', cls=OVSSwitch)
    s3002 = net.addSwitch('s3002', cls=OVSSwitch)
    s3003 = net.addSwitch('s3003', cls=OVSSwitch)
    s3004 = net.addSwitch('s3004', cls=OVSSwitch)
	s3005 = net.addSwitch('s3005', cls=OVSSwitch)
    s3006 = net.addSwitch('s3006', cls=OVSSwitch)
    s3007 = net.addSwitch('s3007', cls=OVSSwitch)
    s3008 = net.addSwitch('s3008', cls=OVSSwitch)

    info( '*** Creating links\n' )

    ## host - switch
    net.addLink(h1, s3001)
    net.addLink(h2, s3001)
    net.addLink(h3, s3002)
    net.addLink(h4, s3002)
    net.addLink(h5, s3003)
    net.addLink(h6, s3003)
    net.addLink(h7, s3004)
    net.addLink(h8, s3004)
	net.addLink(h9, s3005)
    net.addLink(h10, s3005)
    net.addLink(h11, s3006)
    net.addLink(h12, s3006)
    net.addLink(h13, s3007)
    net.addLink(h14, s3007)
    net.addLink(h15, s3008)
    net.addLink(h16, s3008)

    ## switches
    net.addLink(s3001, s2001)
    net.addLink(s3001, s2002)
	net.addLink(s3002, s2001)
    net.addLink(s3002, s2002)
    net.addLink(s3003, s2003)
    net.addLink(s3003, s2004)
	net.addLink(s3004, s2003)
    net.addLink(s3004, s2004)
	net.addLink(s3005, s2005)
    net.addLink(s3005, s2006)
	net.addLink(s3006, s2005)
    net.addLink(s3006, s2006)
	net.addLink(s3007, s2007)
    net.addLink(s3007, s2008)
	net.addLink(s3008, s2007)
    net.addLink(s3008, s2008)
	
	net.addLink(s2001, s1001)
    net.addLink(s2001, s1002)
	net.addLink(s2002, s1003)
    net.addLink(s2002, s1004)
	net.addLink(s2003, s1001)
    net.addLink(s2003, s1002)
	net.addLink(s2004, s1003)
    net.addLink(s2004, s1004)
	net.addLink(s2005, s1001)
    net.addLink(s2005, s1002)
	net.addLink(s2006, s1003)
    net.addLink(s2006, s1004)
	net.addLink(s2007, s1001)
    net.addLink(s2007, s1002)
	net.addLink(s2008, s1003)
    net.addLink(s2008, s1004)

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI(net)

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
