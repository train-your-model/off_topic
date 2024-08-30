import string
import random


class PasswordGen:
    """
    Generates passwords for the users.
    """

    def generate_alphabets(self):
        random_letter = random.choice(string.ascii_letters)
        return random_letter

    def generate_numerics(self):
        random_number = random.randrange(10)
        return str(random_number)

    def generate_symbols(self):
        symbol_list = ["!", "@", "#", "$", "%", "&", "*"]
        random_symbol = random.choice(symbol_list)
        return random_symbol

    def final_pwd(self):
        return_str = ""
        for i in range(9):
            data = self.generate_alphabets() + self.generate_numerics() + self.generate_symbols()
            return_str += random.choice(data)
        shuffle_return_str = random.sample(return_str, len(return_str))
        joined_str = ''.join(shuffle_return_str)
        return joined_str
