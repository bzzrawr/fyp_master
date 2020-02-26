"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        H1 = self.addHost( 'h1' )
        H2 = self.addHost( 'h2' )
        H3 = self.addHost( 'h3' )
        H4 = self.addHost( 'h4' )
        H5 = self.addHost( 'h5' )
        H6 = self.addHost( 'h6' )
        H7 = self.addHost( 'h7' )
        H8 = self.addHost( 'h8' )
        H9 = self.addHost( 'h9' )
        H10 = self.addHost( 'h10' )
        H11 = self.addHost( 'h11' )
        H12 = self.addHost( 'h12' )
        H13 = self.addHost( 'h13' )
        H14 = self.addHost( 'h14' )
        H15 = self.addHost( 'h15' )
        H16 = self.addHost( 'h16' )
        S1 = self.addSwitch( 's1' )
        S2 = self.addSwitch( 's2' )
        S3 = self.addSwitch( 's3' )
        S4 = self.addSwitch( 's4' )
        S5 = self.addSwitch( 's5' )
        S6 = self.addSwitch( 's6' )
        S7 = self.addSwitch( 's7' )
        S8 = self.addSwitch( 's8' )
        S9 = self.addSwitch( 's9' )
        S10 = self.addSwitch( 's10' )
        S11 = self.addSwitch( 's11' )
        S12 = self.addSwitch( 's12' )

        # Add links
        self.addLink( S1, S2 )
        self.addLink( S1, S3 )
        self.addLink( S2, S4 )
        self.addLink( S2, S5 )
        self.addLink( S4, H1 )
        self.addLink( S4, H2 )
        self.addLink( S5, H3 )
        self.addLink( S5, H4 )
        self.addLink( S3, S6 )
        self.addLink( S3, S7 )
        self.addLink( S6, H5 )
        self.addLink( S6, H6 )
        self.addLink( S7, H7 )
        self.addLink( S7, H8 )
        self.addLink( S6, S7 )
        self.addLink( S7, S9 )
        self.addLink( S7, S10 )
        self.addLink( S9, H9 )
        self.addLink( S9, H10 )
        self.addLink( S10, H11 )
        self.addLink( S10, H12 )
        self.addLink( S6, S8 )
        self.addLink( S7, S8 )
        self.addLink( S8, S11 )
        self.addLink( S8, S12 )
        self.addLink( S11, H13 )
        self.addLink( S11, H14 )
        self.addLink( S12, H15 )
        self.addLink( S12, H16 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
