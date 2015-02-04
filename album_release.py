#!/usr/bin/python

import sys
import urllib, lxml
from lxml import etree

def main():
    
    # parse input
    artist = parse_cli_input()
    
    print "Looking up " + artist + " on musicbrainz.org ..."
    
    print unicode("http://musicbrainz.org/ws/2/artist/?query=artist:%s" % (artist) )
    
    # get artist ID 
    artist_id = get_artist_id(artist)

    print artist + "'s artist ID is: " + str(artist_id) 
    
    # get releases
    #get_releases(artist_id)

    

def parse_cli_input():

    artist = ""
    
    if len(sys.argv) == 1:
        print "No artist name given" 
    
    else:
        artist = sys.argv[1]

        idx = 2
        while len(sys.argv) > idx:
            artist += " " + sys.argv[idx]
            idx += 1

    return artist
        
        

def get_artist_id(artist):

    # q = "http://musicbrainz.org/ws/2/recording?query=%s" + artist
  
    f = urllib.urlopen( "http://musicbrainz.org/ws/2/artist/?query=artist:%s" % (artist) )
   
    s = f.read()

    tree = lxml.etree.HTML(s)
    
    # <artist id="3e8bd859-7d82-49e0-b267-84fc46e2bf68" type="Person" ext:score="100">
    # tag name? artist
    # where?  ext:score='"1000"
    # want?   id="?"   (id.value)
    
    artist_id = tree.xpath("//artist[@*[name()='ext:score']='100']/@id")

    f.close()
    
    return artist_id[0]




if __name__ == "__main__": main()

