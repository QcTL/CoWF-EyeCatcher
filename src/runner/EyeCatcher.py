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
        self._EyeContainer.addNewEye("tTest", Eye("Paco", "Mendez", "12/12"), 0)
        self._EyeContainer.addNewEye("tTest", Eye("Paco", "Mendez", "12/12"), 1)
        self._appWeb: AppWebEye = AppWebEye(self._EyeContainer)

    def start(self):
        other_thread = threading.Thread(target=self.loopReceiver)
        other_thread.start()
        self._appWeb.start()

    def loopReceiver(self):
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect(("127.0.0.1", 8888))

        while True:
            data = clientSocket.recv(4 + 32)
            if not data:
                print("Connection closed by the server")
                break
            # Unpack the float value (first 4 bytes)
            int_value = struct.unpack('i', data[:4])[0]

            # Decode the string (remaining 32 bytes)
            received_string = data[4:].decode('utf-8', errors='ignore').rstrip()

            fDateNow = datetime.now().strftime("%d/%m %H:%M")
            isNew = self._EyeContainer.addNewEye(received_string,
                                                 Eye(received_string.split('-')[0], received_string.split('-')[1],
                                                     fDateNow), int_value)
            if isNew:
                self._appWeb.updateList(received_string,
                                        Eye(received_string.split('-')[0], received_string.split('-')[1],
                                            fDateNow))
