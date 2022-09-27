from platform import release
import re

to_validate = input()


class Validator:
    def __init__(self, input: str):
        self.input = input

    def validate(self):
        pass


class LengthValidator(Validator):
    def validate(self):
        if len(self.input) < 8:
            print("Less than 8 characters")
        else:
            return "OK"


class LowerCaseValidator(Validator):
    def validate(self):
        if re.search("[a-z]", self.input) is None:
            print("No lowercase letters")
        else:
            return "OK"


class UpperCaseValidator(Validator):
    def validate(self):
        if re.search("[A-Z]", self.input) is None:
            print("No uppercase letters")
        else:
            return "OK"


class HasNumberValidator(Validator):
    def validate(self):
        if re.search("[0-9]", self.input) is None:
            print("No numbers")
        else:
            return "OK"


class SymbolValidator(Validator):
    def validate(self):
        if re.search(r"[^a-zA-Z\d\s:]", self.input) is None:
            print("No symbols")
        else:
            return "OK"


class RepetitionValidator(Validator):
    def validate(self):
        for i in range(len(self.input) - 3):
            if len(
                set(
                    [self.input[i],
                     self.input[i + 1],
                     self.input[i + 2],
                     self.input[i + 3]])) == 1:
                print("Character repetition")
                return
        return "OK"


class ConsecutiveNumberValidator(Validator):
    def validate(self):
        for i in range(len(self.input) - 3):
            if self.input[i:i+4] in "01234567890SHIT09876543210":
                print("Number sequence")
                return
        return "OK"


class ConsecutiveLetterValidator(Validator):
    def validate(self):
        for i in range(len(self.input) - 3):
            if self.input[i:i+4].lower() in "abcdefghijklmnopqrstuvwxyzSHITzyxwvutsrqponmlkjihgfedcba":
                print("Letter sequence")
                return
        return "OK"


class KeyboardPatternValidator(Validator):
    def transform(self, input: str):
        return input.lower()

    def validate(self):
        shit = self.transform(self.input)
        for i in range(len(shit) - 3):
            shiittt = shit[i:i+4]
            if shiittt in "qwertyuiopSHITpoiuytrewq" or shiittt in "asdfghjklSHITlkjhgfdsa" or shiittt in "zxcvbnmSHITmnbvcxz" or shiittt in "!@#$%^&*()_+SHIT+_)(*&^%$#@!":
                print("Keyboard pattern")
                return
        return "OK"


validators = (
    LengthValidator, LowerCaseValidator, UpperCaseValidator, HasNumberValidator,
    SymbolValidator, RepetitionValidator, ConsecutiveNumberValidator,
    ConsecutiveLetterValidator, KeyboardPatternValidator)

โอ = True

for validator in validators:
    if validator(to_validate).validate() != "OK":
        โอ = False

if โอ:
    print("OK")
