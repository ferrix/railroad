# Model Railroad Traffic Control

This is the source code for my dad's model railroad's traffic control.

## Hardware

- Raspberry Pi with some operating system with Python 3
- Enough 74HC595D shift registers
- Power source
- Keyboard

I have ordered five shift register driver boards from JLCPCB using the
[PCB designed][1] by [Caleb Marting][2]

## Software

- The pi74HC595 library
- Raspberry Pi GPIO library

[1]: https://oshwlab.com/cmarting99/shiftregmosfet
[2]: https://github.com/calebmarting