from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
import math

#calling arduino
#from pyfirmata import Arduino, util
import time
#window.size=360,460
from time import sleep

#connect the board
#board=Arduino('port#')
#initialing an iteration
#iterator=util.iterator(board)
#iterator.start()

#read the pin i/o voltage
#v1=board.get_pin('a:0:i')
#R1= board.get_pin('d:11:p')
#LED= board.get_pin('d:13:o')
#time.sleep(1.0)


#read pin 0 and convert to degreeC
#print((v1.read()*5000.0-500.0)/10.0)

#turn on relay
#R1.write(1)
#time.sleep(30.0)

#read pin 0 and convert to degreeC
#print((v1.read()*5000.0-500.0)/10.0)

#turn off Realay
#R1.write(0.0)
#board.exit

class Function(Screen):
    pass
    #def switch_led(self, switchObject, switchValue):
       #if switchValue is True:
            #board.digital[pin].write(1)
       # else:
            #board.digital[pin].write(0)

    #def temp_sensor(self):
        #spin = str(math.floor(self.ids.spin_value.value))
        #if int(spin)>100:
            #activateServo(spin,spin)
        #else:
            #board.digital[pin].write(0)

class InfraredLightApp(MDApp):
    def build(self):
        Builder.load_file('layout.kv')
        return Function()

InfraredLightApp().run()
