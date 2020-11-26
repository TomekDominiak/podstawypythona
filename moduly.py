import piramida as draw
import Izogram as morda
import rąb
import sys # moduły gotowe
import platform # moduły gotowe
if __name__ == '__main__':
    draw.piramida(10)
    morda.izogram("tomek")
    rąb.piramida(20)

print(sys.platform)
print(platform.system())