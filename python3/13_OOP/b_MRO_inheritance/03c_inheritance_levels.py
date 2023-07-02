"""
Purpose: No Limit of Inheritance levels
"""


class Level1:
    def level1_method(self):
        print("Level 1")


class Level2(Level1):
    def level2_method(self):
        print("Level 2")


class Level3(Level2):
    def level3_method(self):
        print("Level 3")


class Level4(Level3):
    def level4_method(self):
        print("Level 4")


class Level5(Level4):
    def level5_method(self):
        print("Level 5")


class Level6(Level5):
    def level6_method(self):
        print("Level 6")


class Level7(Level6):
    def level7_method(self):
        print("Level 7")


class Level8(Level7):
    def level8_method(self):
        print("Level 8")


class Level9(Level8):
    def level9_method(self):
        print("Level 9")


class Level10(Level9):
    def level10_method(self):
        print("Level 10")


class Level11(Level10):
    def level11_method(self):
        print("Level 11")


# Usage
obj = Level11()
obj.level1_method()
obj.level2_method()
obj.level3_method()
obj.level4_method()
obj.level5_method()
obj.level6_method()
obj.level7_method()
obj.level8_method()
obj.level9_method()
obj.level10_method()
obj.level11_method()
