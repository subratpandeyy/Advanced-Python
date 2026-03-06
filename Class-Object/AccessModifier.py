class stu:
    def __init__(self, name, roll, sec):
        self.name = name
        self._roll = roll
        self.__sec = sec

    def print_name(self):
        print(self.name)

    def _print_roll(self):
        print(self._roll)

    def _prin_sec(self):
        print(self.__sec)


ob = stu("Subrat", 514, "J")
ob.print_name()
ob._print_roll()
ob._prin_sec()

