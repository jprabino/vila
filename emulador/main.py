import time
import random
import requests
from config.emulatorconfig import SERVER_IP,SERVER_PORT
class ACEmulator:

    def __init__(self, id):
        self.id=id

    def main_loop(self):

        while True:
            if self.is_server_up():
                data=self.create_emu_data()
                self.send_emu_data(data)
            time.sleep(3)

    def is_server_up(self):
        return True

    def create_emu_data(self):
        return {'device': self.get_id(),
                'temperature': self.get_temperature(),
                'humidity': self.get_humidity(),
                'compressor_status': self.get_compressor_status(),
                'fan_status': self.get_fan_status(),
                'line_current':  self.get_current(),
                'line_voltage': self.get_line_voltage()}

    def get_id(self):
        return 'TEST_ID' if not self.id else self.id
        
    def get_temperature(self):
        return str(random.randrange(25,35,1))

    def get_humidity(self):
        return str(random.randrange(50,85,1))

    def get_compressor_status(self):
        return "ON"

    def get_fan_status(self):
        return "ON"
    
    def get_current(self):
        return str(random.randrange(80,95,1)/10.0)
    
    def get_line_voltage(self):
        return str(random.randrange(2180,2240,1)/10.0)
    
    def send_emu_data(self, data):
        print (data)
        response = requests.post('http://{}:{}/ambiente/device_data_list/'.format(SERVER_IP,SERVER_PORT), 
                            data = data)
        print(response.text)
        

if __name__ == "__main__":
    acemu = ACEmulator("http://127.0.0.1:8000/ambiente/devices/2/")
    acemu.main_loop()
    