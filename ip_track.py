#c0d3r: Hacknology
#Source repo:
#well, it is hard to explain. I saw it on a web site, but we had to write all codes
#to terminal, so i made it a script
#hope to enjoy
import pygeoip
data = pygeoip.GeoIP('C:\\GeoLiteCity.dat')
adres = data.record_by_addr('{}'.format(input('[*]IP number of target: ')))
for cikti in adres.items():
    print("%s: %s" %(cikti))

input()
