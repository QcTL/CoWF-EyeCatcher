from datetime import datetime

from . import Eye


class EyeContainer:
    """
    Class that saves the list of active Eyes that the application has sent.
    """

    def __init__(self):
        self._mEyes = {}

    def getTotalEyes(self) -> list[tuple[str, Eye]]:
        """
        Get the total list of values saved in the class

        :return: A list of tuples of string uuid of the eye and a reference of the eye object with its values.
        """
        return [(i[0], i[1]) for i in self._mEyes.items()]

    def getUniqueEye(self, uuidEye: str) -> tuple[str, Eye]:
        """
        Given the uuidEye return its associated reference eye
        :param uuidEye: The uuidEye of the returned, it has to exists in the list
        :return: A tuple having the str uuidEntered and the Eye class referenced with that uuid
        """
        return uuidEye, self._mEyes[uuidEye]

    def addNewEye(self, uuidEye: str, eye: Eye, dNewValue: float, dTimeValue: int) -> bool:
        """
        Function to add a new created eye to the storage
        :param uuidEye: A new unique uuid string of the eye that hasn't been introduced before
        :param eye: The reference of the class Eye that you want to save
        :param dNewValue:  The first value that the eye has
        :param dTimeValue:  The simulated timestamp where the eye was introduced
        :return: Returns a bool if the Eye was successfully stored.
        """
        bNew = False
        if uuidEye not in self._mEyes:
            self._mEyes[uuidEye] = eye
            bNew = True

        self._mEyes[uuidEye].addNewValue(dNewValue, dTimeValue)
        self._mEyes[uuidEye].eLast = datetime.now().strftime("%d/%m %H:%M")
        return bNew
