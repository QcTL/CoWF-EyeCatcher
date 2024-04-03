from . import Eye


class EyeContainer:

    def __init__(self):
        self._mEyes = {}

    def getTotalEyes(self) -> list[tuple[str, Eye]]:
        return [(i[0], i[1]) for i in self._mEyes.items()]

    def getUniqueEye(self, uuidEye: str) -> tuple[str, Eye]:
        return uuidEye, self._mEyes[uuidEye]

    def addNewEye(self, uuidEye: str, eye: Eye, dNewValue: float):
        if uuidEye not in self._mEyes:
            self._mEyes[uuidEye] = eye
        self._mEyes[uuidEye].addNewValue(dNewValue)
