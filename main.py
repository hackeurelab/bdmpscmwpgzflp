#!/usr/bin/env python
import os

def main():
    print('start play')
    os.system('ffplay -autoexit -nodisp -v 0 assets/bonjour.mp3')
    print('stop play')
    return

if __name__ == '__main__':
    main()