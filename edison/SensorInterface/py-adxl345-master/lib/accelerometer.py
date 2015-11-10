import mraa as m
import random as rand
import time

# Excuse the super boring example, I was out of fun devices to play with, this
# will write and read the same data back to itself, a few 100 times, just short
# MISO & MOSI on your board


print (m.getVersion())
while True:
    try:
        x = m.Aio(0)
        print (x.read())
        print ("%.5f" % x.readFloat())
    except:
        print ("Are you sure you have an ADC?")
	time.sleep(1)
	# fo = open("reading.txt", "w")
	# fo.write(x.read())
	# fo.close()