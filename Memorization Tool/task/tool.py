import db_worker as dw


class Game:
    cards = dw.results

    def __init__(self):
        self.menu_items = {
            '1': ('Add flashcards', self.input_card),
            '2': ('Practice flashcards', self.practice),
            '3': ('Exit', self.exit),
        }

        self.input_card_menu = {
            '1': ('Add a new flashcard', self.add_card),
            '2': ('Exit', self.exit),
        }

        self.menu(self.menu_items)

    def input_card(self):
        self.menu(self.input_card_menu)

    def menu(self, menu_items):
        try:
            while True:
                self.print_menu(menu_items)
                command = input()
                print()
                menu_items.get(command, (None, lambda: print(f'{command} is not an option\n')))[1]()
        except StopIteration:
            pass

    @staticmethod
    def print_menu(menu):
        for key, value in menu.items():
            print(f'{key}. {value[0]}')

    def add_card(self):
        dw.add_cards(self.input_true('Question'), self.input_true('Answer'))
        print()

    @classmethod
    def practice(cls):
        phrase = 'Please press "y" to see the answer or press "n" to skip'

        if cls.cards():
            for card in cls.cards():
                print(f'Question: {card.question}')
                command = cls.input_true(phrase, ('y', 'n'))
                print()
                if command == 'y':
                    print(f'Answer: {card.answer}')
                print()
        else:
            print('There is no flashcard to practice!\n')

    @staticmethod
    def exit():
        raise StopIteration

    @staticmethod
    def input_true(text, cases=None):
        while True:
            result = input(f'{text}:\n')
            if not result or (cases is not None and result not in cases):
                continue
            return result


if __name__ == '__main__':
    Game()
    print('Bye!')
