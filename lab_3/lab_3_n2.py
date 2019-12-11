import smbus
import time

bus = smbus.SMBus(1)
address = 0x29

bus.write_byte(address, 0xa0)
bus.write_byte(address, 0x03)
time.sleep(0.5)

while True:
	bus.write_byte(address, 0xac)
	a = bus.read_byte(address)
	bus.write_byte(address, 0xad)
	b = bus.read_byte(address)
	print a + b*256
	time.sleep(0.1)