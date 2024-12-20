from icecream import ic
from regex import findall

class wordChecker():
    def __init__(self, word):
        self.word = word
        self.index = 0

    def check(self, char):
        if self.word[self.index] == char:
            self.index += 1
        else:
            self.index = 0
        if self.index == len(self.word):
            self.index = 0
            return True
        return False
    
    def reset(self):
        self.index = 0

def main():
    data = ""
    enabled = True
    with open('data/03.data') as f:
        data = f.read()
    checkers = {
        'mul': wordChecker('mul('),
        'do': wordChecker('do()'),
        'dont': wordChecker('don\'t()')
    }
    sumproduct = 0

    first_digit = ""
    second_digit = ""
    first_ready = False
    collecting = False

    for char in data:
        mul, do, dont = [checkers[id].check(char) for id in checkers]
        if do:
            enabled = True
        if dont:
            enabled = False
        if not enabled:
            continue
        if not mul and not collecting:
            continue
        if not collecting:
            collecting = True
            continue
        if char == ')':
            sumproduct += int(first_digit) * int(second_digit)
        if char == ',':
            first_ready = True
            continue
        try:
            int(char)
        except:
            first_digit = ""
            second_digit = ""
            first_ready = False
            collecting = False
            continue
        if not first_ready:
            first_digit += char
        else:
            second_digit += char
        if len(first_digit) > 3 or len(second_digit) > 3:
            first_digit = ""
            second_digit = ""
            first_ready = False
            collecting = False
            continue

    ic(sumproduct)

if __name__ == '__main__':
    main()
