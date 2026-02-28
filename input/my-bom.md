<!--
Maintainer:   jeffskinnerbox@yahoo.com / www.jeffskinnerbox.me
Version:      0.0.0

# convert markdown .md to MS Word .docx
pandoc -f gfm input.md -o output.docx
-->

# Bill of Materials
The tables below contain all the things needed to execute this course.

* **Hardware -**
* **Software -**
* **Code Blocks -**
* **Tools -**

## Hardware

### Line Following Robot
These items required by each student:

| Item | Quantity | Unit Cost | Source | Notes |
|:-----:|:-----:|:-----:|:-----:|:--------:|
| Robot Car Chassis | 1 | $13.00 | [Amazon][01] | car body for building robot  |
| 8 x AA Battery Holder | 1 | $3.50 | [Amazon][02] | 12V power source  |
| 6 x AA Battery Holder | 1 | $4.50 | [Amazon][03] | 9V power source  |
| 9V Battery Clip Connector | 1 | $0.50 | [Amazon][05] | 9V power source  |
| 5V Buck Converter Module | 1 | $1.00 |[Amazon][09] | board to interface with MCU |
| Raspberry Pi Pico W | 1 | $12.00 | [Amazon][07]| MCU for addvanced features |
| Robotics Board for Raspberry Pi Pico | 1 | $19.00 | [PiShop.us][08]| motor controller board to move wheels |
| IR Infrared Obstacle Avoidance Sensor | 2 | $5.00 |[Amazon][06] | sensors to detect line |
| QTRX-MD-08RC Reflectance Sensor Array | 1 | $17.00 | [Polou][10] | sensor array to detect line |
| 400 Pin Solderless Prototype Board | 1 | $1.25 |[Amazon][04] | board to interface with MCU |

[01]:https://www.amazon.com/gp/product/B01LXY7CM3/
[02]:https://www.amazon.com/ZZHXSM-Battery-Thicken-Standard-Connector/dp/B0BTLTK2LX/
[03]:https://www.amazon.com/LBTODH-Battery-Holder-Plastic-Storage/dp/B0DR88NKCZ/?th=1
[04]:https://www.amazon.com/DEYUE-breadboard-Set-Prototype-Board/dp/B07LFD4LT6/
[05]:https://www.amazon.com/Battery-Clip-Hard-Electronics-I-Type/dp/B0DRZWN3BN/?th=
[06]:https://www.amazon.com/Infrared-Avoidance-Transmitting-Receiving-Photoelectric/dp/B07PFCC76N?th=1
[07]:https://www.amazon.com/Raspberry-Pi-Pico-Wireless-Bluetooth/dp/B0B5H17CMK
[08]:https://www.pishop.us/product/robotics-board-for-raspberry-pi-pico/
[09]:https://www.amazon.com/Converter-Module-5V-30V-Voltage-Regulator/dp/B0DKTMGBHL/
[10]:https://www.pololu.com/product/4348

### Supplies for Robot
These minor electronic parts will be shared among all the students:

| Item | Quantity | Total Cost | Source | Notes |
|:-----:|:-----:|:-----:|:-----:|:--------:|
| Pin Header Connection |    20     | $6 | [Amazon][11] | 20 pack kit can be shared by all |
| 8 x AA Batteries |    20     | $10.00 | [Amazon][12] | 20 pack kit can be shared by all |
| 6 x AA Batteries |    20     | $10.00 | [Amazon][12] | 12 pack kit can be shared by all |
| 9V Batteries |    12     | $18.00 | [Amazon][13] | 12 pack kit can be shared by all |
| White 8.5x11 inch paper |    TBD     | NA | Makersmiths | paper for Robot Car line course |

[11]:https://www.amazon.com/HiLetgo-20pcs-2-54mm-Single-Header/dp/B07R5QDL8D/
[12]:https://www.amazon.com/AmazonBasics-Performance-Alkaline-Batteries-20-Pack/dp/B07KWYGTC6/?th=1
[13]:https://www.amazon.com/Amazon-Basics-Performance-All-Purpose-Batteries/dp/B0B4RSNDPG/?th=1

### Optional
These are optional but very nice to have:

| Item | Quantity | Item Cost | Source | Notes |
|:-----:|:-----:|:-----:|:-----:|:--------:|
| I2C Quad Rotary Encoder Board | 1 | $8.00 | [Adafruit][14] | for seting PID & Loop values |
| Rotary Encoder + Knob | 4 | $4.50 | [Adafruit][15] | for seting PID & Loop values |
|  Male Header / I2C STEMMA Cable | 1 | $1.50 | [Adafruit][16] | for connecting I2C devices |
|  Female Header / I2C STEMMA Cable | 1 | $1.50 | [Adafruit][17] | for connecting I2C devices |
| 128x64 Inch OLED Display Screen | 1 | $3.00 | [Amazon][08] | for displaying PID & Loop values |

[14]:https://www.adafruit.com/product/5752
[15]:https://www.adafruit.com/product/377
[16]:https://www.adafruit.com/product/3955
[17]:https://www.adafruit.com/product/3950
[18]:https://www.amazon.com/Self-Luminous-Display-Compatible-Arduino-Raspberry/dp/B09JWN8K99?th=1

### Tools

| Item | Quantity | Source | Notes |
|:-----:|:-----:|:-----:|:--------:|
| Protective Eye Gear | 1 | Student | |
| Soldering Iron | 1 | Makersmiths | |
| Spoll of Soldering | 1 | Makersmiths | |
| Solder Flux | 1 | Makersmiths | |
| Solder Wick | 1 | Makersmiths | |
| SiliconTip Solder Sucker | 1 | Makersmiths | |
| Laptop Computer | 1 | Student | |
| WiFi with Internet Access | 1 | Makersmiths | |


### Shipping Charges for All Items
These shipping charges will be shared among all the students:

| Item | Quantity | Item Cost | Source | Notes |
|:-----:|:-----:|:-----:|:-----:|:--------:|
| Amazon Shipping | NA | $0 | NA | |
| PiShop.us Shipping | NA | $8 | NA | |
| Polou Shipping | NA | $8 | NA | |
| Adafruit Shipping | NA | $8 | NA | |


## Software
For code on the Raspberry Pi Pico W, we'll be using [CircuitPython][19]
(a super set of [MicroPython][20], specifically designed to support Adafruit products).
For experienced coders, particularly Python coders,
they can work in a terminal window using the [Python REPL][21].

For less experienced coders,
there are some [block-based coding][22] tools available for MicroPython and CircuitPython.
These allowing users to program microcontrollers with a drag-and-drop interface.
The most notable options are [Piper Make][23] and [BIPES (Block based Integrated Platform for Embedded Systems)][24].

And for those people who's skills lay between beginner and experienced,
using the [Mu Editor][18] might be the answer.

[19]:https://learn.adafruit.com/welcome-to-circuitpython
[20]:https://micropython.org/
[21]:https://realpython.com/python-repl/
[22]:https://subjectguides.york.ac.uk/coding/scratch
[23]:https://www.playpiper.com/pages/piper-make?srsltid=AfmBOooPN66GibaOclgxc1JwWyIwzxgq-43qIoW0lPFQahqRiIQIw7jy
[24]:https://bipes.net.br/wp/


| Item | Source | Notes |
|:-----:|:-----:|:--------:|
| CircuitPython Installation | [Webpage][25] | |
| Mu Editor Installation | [Webpage][26] | |
| Piper Make Installation | [Webpage][27] | |
| BIPES | [Cloud][28] | you can also host it yourself, see note below |
| Circuit Canvas | [Cloud][29] | used to create circuit diagram to assist in wiring |

>**NOTE:** You can install/host BIPES on you own system, if you wish.
>See the install instruction in the [BIPES developer documentation][22].

[25]:https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython
[26]:https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor
[27]:https://bipes.net.br/3/docs/contribute/forking.html
[28]:https://bipes.net.br/ide/
[29]:https://circuitcanvas.com/

## Classroom Code Blocks
Some of the coding required could be challenging to get done in the time allotted.
To help the students to stay on schedule, some code blocks will be supplied.


| Item | Quantity | Source | Notes |
|:-----:|:-----:|:-----:|:--------:|
| PID Controller | 1 | Makersmiths | PID control for sensor array  |
| Browser User Interface | 1 | Makersmiths | supplies car UI via browser |
| RPi Pico WiFi Access Point | 1 | Makersmiths | makes RPi Pico WiFi Access Point |
| Rotary Encoders | 1 | Makersmiths | optional: for adjusting PID & Loop parameters |
| OLED Display Screen | 1 | Makersmiths | optional: for displaying PID & Loop parameters |


