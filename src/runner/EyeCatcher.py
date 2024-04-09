import socket
import struct
import threading
from datetime import datetime

from src.runner.Eye.Eye import Eye
from src.runner.Eye.EyeContainer import EyeContainer
from src.web.AppWebEye import AppWebEye


class EyeCatcher:

    def __init__(self):
        self._EyeContainer: EyeContainer = EyeContainer()
        self._appWeb: AppWebEye = AppWebEye(self._EyeContainer)

    def start(self):
        other_thread = threading.Thread(target=self.loopReceiver)
        other_thread.start()
        self._appWeb.start()

    def loopReceiver(self):
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect(("127.0.0.1", 8888))

        while True:
            data = clientSocket.recv(4 + 4 + 32)
            if not data:
                print("Connection closed by the server")
                break

            int_value = struct.unpack('i', data[:4])[0]
            long_value = struct.unpack('i', data[4:8])[0]
            received_string = data[8:].decode('utf-8', errors='ignore').rstrip()

            fDateNow = datetime.now().strftime("%d/%m %H:%M")
            nEye = Eye(received_string.split('-')[0], received_string.split('-')[1], fDateNow)
            isNew = self._EyeContainer.addNewEye(received_string,
                                                 nEye, int_value, long_value)

            if isNew:
                self._appWeb.updateList(received_string,nEye)
            else:
                self._appWeb.updateGraf(received_string,nEye)
