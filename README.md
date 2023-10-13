# sbai-course
sbai-course

# Python Environment Setup

1. First, install ´pip´ and ´virtualenv´:
```bash
sudo apt-get install python3-pip -y
pip3 install virtualenv 
```

2. Create and activate virtualenv (`.sbai`):
```bash
python3 -m virtualenv .sbai
source .sbai/bin/activate
```

3. Install remain python dependecies:
```bash
pip install -r requirements.txt
```

# Arduino Environment Setup

1. Download [Arduino IDE](https://www.arduino.cc/en/software);

2. Install Arduino:
```
chmod + x arduino..
./arduino-ide
```

3. Open Arduino IDE;

4. Go to `File > Preferences`. Enter the following link into the `Additional Board Manager URLs` field and click **OK**:
```
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json 
```

5. Open the Boards Manager. Go to `Tools > Board >Boards Manager` and search for ESP32.

6. Install the ESP32 by Espressif Systems;

7. USB permission:

```bash
sudo adduser $USER $(stat --format="%G" /dev/ttyACM0 )
```

# References

- [How to install virtualenv](https://gist.github.com/frfahim/73c0fad6350332cef7a653bcd762f08d);
