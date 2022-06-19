import random


class PasswordGen:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def generate_pass(self):
        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        pass_letter = [random.choice(self.letters) for n in range(nr_letters)]
        pass_symbol = [random.choice(self.symbols) for n in range(nr_symbols)]
        pass_number = [random.choice(self.numbers) for n in range(nr_numbers)]

        password_list = pass_letter + pass_symbol + pass_number

        random.shuffle(password_list)

        password = "".join(password_list)

        return password