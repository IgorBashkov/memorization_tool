import db_worker as dw


class Game:

    def __init__(self):
        self.main_menu = {
            '1': ('Add flashcards', self.add_new_card),
            '2': ('Practice flashcards', self.practice),
            '3': ('Exit', self.exit),
        }
        self.input_card_menu = {
            '1': ('Add a new flashcard', self.add_card),
            '2': ('Exit', self.exit),
        }
        self.practice_menu = {
            'y': ('to see the answer:', self.show_answer),
            'n': ('to skip:', self.exit),
            'u': ('to update:', self.update_card),
        }
        self.update_menu = {
            'd': ('to delete the flashcard:', self.delete_card),
            'e': ('to edit the flashcard:', self.edit_card),
        }
        self.cards = dw.results
        self.menu(self.main_menu, key_format=lambda s: f'{s}. ')

    def menu(self, menu_items, key_format=None, **kwargs):
        def not_an_option():
            print(f'{command} is not an option\n')
        try:
            while True:
                self.print_menu(menu_items, key_format)
                command = input()
                print()
                menu_items.get(command, (None, not_an_option))[1](**kwargs)
        except StopIteration:
            pass

    @staticmethod
    def print_menu(menu, key_format=None):
        for key, value in menu.items():
            if key_format is not None:
                key = key_format(key)
            print(f'{key}{value[0]}')

    def add_card(self):  # number 1 on main menu
        dw.add_cards(self.input_true('Question'), self.input_true('Answer'))
        print()

    def practice(self):  # number 2 on main menu
        if self.cards():
            for card in self.cards():
                print(f'Question: {card.question}')
                self.menu(self.practice_menu, key_format=lambda s: f'press "{s}" ', card=card)
        else:
            print('There is no flashcard to practice!\n')

    @staticmethod  # number 3 on main menu
    def exit(**kwargs):
        raise StopIteration

    def add_new_card(self):  # number 1 on add card menu
        self.menu(self.input_card_menu, key_format=lambda s: f'{s}. ')

    @staticmethod  # get True input
    def input_true(text):
        while True:
            result = input(f'{text}:\n')
            if not result:
                continue
            return result

    def update_card(self, **kwargs):  # call menu for update cart and close
        self.menu(self.update_menu, key_format=lambda s: f'press "{s}" ', **kwargs)
        self.exit()

    @staticmethod
    def show_answer(**kwargs):
        print(f'Answer: {kwargs["card"].answer}')
        Game.exit()

    @staticmethod
    def delete_card(**kwargs):
        dw.delete_card(kwargs['card'].id)
        Game.exit()

    @staticmethod
    def edit_card(card):
        def input_format(word, val):
            return f'current {word}: {val}\nplease write a new {word}:\n'
        dw.edit_card(card.id,
                     input(input_format('question', card.question)),
                     input(input_format('answer', card.answer))
                     )
        Game.exit()


if __name__ == '__main__':
    Game()
    print('Bye!')
