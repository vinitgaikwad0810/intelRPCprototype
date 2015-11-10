import mraa as m
import random as rand

# Excuse the super boring example, I was out of fun devices to play with, this
# will write and read the same data back to itself, a few 100 times, just short
# MISO & MOSI on your board

dev = m.Spi(0)

for x in range(0,100):
  txbuf = bytearray(4)
  for y in range(0,4):
    txbuf[y] = rand.randrange(0, 256)
  rxbuf = dev.write(txbuf)
  if rxbuf != txbuf:
    print("We have an error captain!")
    break
    exit(1)