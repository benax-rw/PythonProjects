#!/usr/bin/env python3

import serial

ser = serial.Serial(
        port='/dev/tty.usbmodemR9YR80CSJHB2', #plz change this according to your port number
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

ser.flush()


if __name__ == '__main__':
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            f=open("myphone.txt","a")
            f.write(line)
            f.write("\n")
            f.close()
            print(line)
