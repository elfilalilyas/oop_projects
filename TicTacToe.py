# creating the grid
import os
import time
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Grid:
    def __init__(self):
        self.grid_data = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    def draw_grid(self):
        print('\n')
        print('\t\t\t_____________')
        for i in range(0, 9, 3):
            print(f"\t\t\t| {' | '.join(self.grid_data[i:i + 3])} |")
        print('\t\t\t-------------')
        print('\n')

    def update_grid(self, num, mark):
        if num in range(1, 10) and self.grid_data[num - 1] == '-':
            self.grid_data[num - 1] = mark
            return True
        return False

    def empty_places(self):
        empty_places = []
        for ind, place in enumerate(self.grid_data):
            if place == '-':
                empty_places.append(ind + 1)
        return empty_places

    def reset_grid(self):
        self.grid_data = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    def get_rules(self):
        print("""
        ****************************RULES******************************
        ----First you will choose your mark----------------------------
        ----The grid is 3 * 3 matrix-----------------------------------
        ----Your goal is to get 3 of your marks in a line--------------
        ----The player who finish the row first  wins------------------
        """)
        print('''
        | X | X | X |              | - | X | - |
        | - | - | - |              | - | X | - |
        | - | - | - |              | - | X | - |''')
        print('''
        | - | - | - |              | - | - | X |
        | X | X | X |              | - | - | X |
        | - | - | - |              | - | - | X |''')
        print('''
        | - | - | - |              | X | - | - |
        | - | - | - |              | - | X | - |
        | X | X | X |              | - | - | X |''')
        print('''
        | X | - | - |              | - | - | X |
        | X | - | - |              | - | X | - |
        | X | - | - |              | X | - | - |''')
        print('''
        ----The game ends without winner if none of you finished a line''')


class Player:
    marks = ['O', 'X']
    def __init__(self, name='', mark=''):
        self.name = name
        self.mark = mark

    def choose_name(self):
        player_name = input(f'\tplease enter your name(alphabets only): ')
        while not player_name.isalpha():
            player_name = input(f'\tInvalid name, please enter your name(letters only): ')
        self.name = player_name


    def choose_mark(self):
        if len(Player.marks) == 2:
            player_mark = ''
            while player_mark not in Player.marks:
                player_mark = input(f'\tenter your Mark please (X/O): ').upper()
            Player.marks.remove(player_mark)
            self.mark = player_mark
        else:
            player_mark = Player.marks[0]
            Player.marks = ['O', 'X']
            if self.name == 'Computer':
                print(f"\tThe Computer's mark is {player_mark}")
            else:
                print(f'\tyour Mark is {player_mark}')
            self.mark = player_mark


class GameMenu:
    def display_main_menu(self):
        print('Choose..')
        print("""\t1- Start Game\n\t2- Quit Game""")
        while True:
            choice = int(input('Enter 1 To Start The Game, 2 To Quit The Game: '))
            if choice == 1 or choice == 2:
                break
            print('Invalid Choice. You Have Only Two Options (1 or 2)')
        return choice

    def display_end_game(self):
        print("\n\nWould You Like To Play Again!.")
        print("""\t\t1- To Restart Game\n\t\t2- To Quit Game""")
        while True:
            choice = int(input('Enter 1 To Restart The Game, 2 To Quit The Game: '))
            if choice == 1 or choice == 2:
                break
            print('Invalid Choice. You Have Only Two Options (1 or 2)')
        return choice


class Game:
    def __init__(self, degree='easy'):
        self.g = Grid()
        self.players = [Player(), Player()]
        self.menu = GameMenu()
        self.degree = degree
        self.init_turn = 0
        self.turn = self.init_turn


    def start_game(self):
        print("""\n\n\t\tWELCOME TO THE TIC-TAC-TOE GAME""")
        self.g.draw_grid()
        choice = self.menu.display_main_menu()
        time.sleep(1)
        if choice == 2:
            self.quit_game()
        else:
            self.setup_players()
            self.presente_game()
            self.play_game()

    def vs_players(self):
        print('\n\nSelect Your Enemy...\n\t1- Computer\n\t2- Friend')
        while True:
            choice = int(input('Enter 1 To Play Against The Computer, 2 Your Friend: '))
            if choice == 1 or choice == 2:
                break
            print('Invalid Choice. You Have Only Two Options (1 or 2)')
        return choice

    def setup_players(self):
        clear_screen()
        if self.vs_players() == 2:
            clear_screen()
            for ind, player in enumerate(self.players):
                print(f"\nPlayer{ind + 1} enter your details:")
                player.choose_name()
                player.choose_mark()
                
        else:
            level = input('\nWhat level of the Computer you want to face?(Hard/medium/easy): ')
            if level.lower() == 'hard':
                self.degree = 'hard'
            elif level.lower() == 'medium':
                self.degree = 'medium'
            time.sleep(1)
            clear_screen()
            print(f"\nPlayer{1} enter your details:")
            self.players[0].choose_name()
            self.players[0].choose_mark()
            self.players[1] = Player('Computer')
            print(f"\nPlayer{2} is the Computer")
            self.players[1].choose_mark()
            time.sleep(1)
        

    def presente_game(self):
        input('\nPress enter..')
        clear_screen()
        print(f"\n********** {self.players[0].name}({self.players[0].mark}) -VS- {self.players[1].name}({self.players[1].mark}) **********\n")
        answer = input(f"\nDo You Know The Rules?: ")
        if answer.upper() == 'NO':
            self.g.get_rules()
        print('Preparing The Grid in Progress...')
        time.sleep(3)
        
        

    def play_game(self):
        clear_screen()
        print(f"\n********** {self.players[0].name}({self.players[0].mark}) -VS- {self.players[1].name}({self.players[1].mark}) **********\n")
        self.g.draw_grid()
        input('Now Both of you know the rules. Lets Get Started(Press Enter).....\n')
        while True:
            if self.players[self.turn].name != 'Computer':
                self.player_turn()
            else:
                self.pc_turn()
            self.g.draw_grid()
            if self.check_winner(self.g.grid_data) or self.check_draw(self.g.grid_data):
                break
        time.sleep(1)
        self.display_result()
        time.sleep(2)
        choice = self.menu.display_end_game()
        self.restart_game(choice)

    def player_turn(self):
        player = self.players[self.turn]
        print(f"{self.players[self.turn].name}({self.players[self.turn].mark}) Turn")
        time.sleep(1)
        while True:
            try:
                place = int(input(f'{player.name} choose a cell (1-9): '))
                if self.g.update_grid(place, player.mark):
                    break
                else:
                    print('Invalid Cell Choice. Try Again')
            except ValueError:
                print('You Can Only Enter Numbers in region (1-9)')
        self.turn = (self.turn + 1) % len(self.players)
        # or we use: self.turn = 1 - self.turn

    def pc_turn(self):
        pc = self.players[self.turn]
        player = self.players[self.turn - 1]
        print(f"{pc.name} will choose a cell(1-9) now: ")
        time.sleep(1)
        if self.degree == 'hard':
            if self.hard_level(pc, player):
                pc_choice = self.hard_level(pc, player)
            else:
                pc_choice = random.choice(self.g.empty_places())
            self.g.update_grid(pc_choice, pc.mark)
        elif self.degree == 'medium':
            if self.medium_level(pc):
                pc_choice = self.medium_level(pc)
            else:
                pc_choice = random.choice(self.g.empty_places())
            self.g.update_grid(pc_choice, pc.mark)
        else:
            pc_choice = self.easy_level()
            self.g.update_grid(pc_choice, pc.mark)
        self.turn = (self.turn + 1) % len(self.players)

    def easy_level(self):
        return random.choice(self.g.empty_places())

    def medium_level(self, pc):
        empty_places = self.g.empty_places()
        grid_check = self.g.grid_data.copy()
        for place in empty_places:
            grid_check[place - 1] = pc.mark
            if self.check_pc_winner(grid_check):
                return place
            grid_check[place - 1] = '-'
        return None

    def hard_level(self, pc, player):
        empty_places = self.g.empty_places()
        grid_check = self.g.grid_data.copy()
        for place in empty_places:
            grid_check[place - 1] = pc.mark
            if self.check_pc_winner(grid_check):
                return place
            grid_check[place - 1] = player.mark
            if self.check_winner(grid_check):
                return place
            grid_check[place - 1] = '-'
        return None

    def display_result(self):
        print("""***********************GAME OVER!***********************""")
        if self.check_winner(self.g.grid_data):
            tup = self.check_winner(self.g.grid_data)
            winner = self.players[tup[1] - 1]
            print(f'Player {winner.name} with mark {winner.mark} is the winner')
        else:
            print("'DRAW'. Game ended without a winner.")

    def restart_game(self, choice):
        self.g.reset_grid()
        self.turn = (self.init_turn + 1) % len(self.players)
        self.init_turn = self.turn
        if choice == 1:
            self.play_game()
        else:
            self.quit_game()

    def quit_game(self):
        return 'Thanks For Playing The Game'

    def check_winner(self, grid_data):
        if grid_data[0] == grid_data[1] == grid_data[2] and grid_data[0].isalpha():
            return grid_data[0], self.turn
        elif grid_data[3] == grid_data[4] == grid_data[5] and grid_data[3].isalpha():
            return grid_data[3], self.turn
        elif grid_data[6] == grid_data[7] == grid_data[8] and grid_data[6].isalpha():
            return grid_data[6], self.turn
        elif grid_data[0] == grid_data[3] == grid_data[6] and grid_data[0].isalpha():
            return grid_data[0], self.turn
        elif grid_data[1] == grid_data[4] == grid_data[7] and grid_data[1].isalpha():
            return grid_data[1], self.turn
        elif grid_data[2] == grid_data[5] == grid_data[8] and grid_data[2].isalpha():
            return grid_data[2], self.turn
        elif grid_data[0] == grid_data[4] == grid_data[8] and grid_data[0].isalpha():
            return grid_data[0], self.turn
        elif grid_data[2] == grid_data[4] == grid_data[6] and grid_data[2].isalpha():
            return grid_data[2], self.turn
        else:
            return False

    def check_pc_winner(self, grid_data):
        if grid_data[0] == grid_data[1] == grid_data[2] and grid_data[0].isalpha():
            return grid_data[0], self.turn
        elif grid_data[3] == grid_data[4] == grid_data[5] and grid_data[3].isalpha():
            return grid_data[3], self.turn
        elif grid_data[6] == grid_data[7] == grid_data[8] and grid_data[6].isalpha():
            return grid_data[6], self.turn
        elif grid_data[0] == grid_data[3] == grid_data[6] and grid_data[0].isalpha():
            return grid_data[0], self.turn
        elif grid_data[1] == grid_data[4] == grid_data[7] and grid_data[1].isalpha():
            return grid_data[1], self.turn
        elif grid_data[2] == grid_data[5] == grid_data[8] and grid_data[2].isalpha():
            return grid_data[2], self.turn
        elif grid_data[0] == grid_data[4] == grid_data[8] and grid_data[0].isalpha():
            return grid_data[0], self.turn
        elif grid_data[2] == grid_data[4] == grid_data[6] and grid_data[2].isalpha():
            return grid_data[2], self.turn
        else:
            return False


    def check_draw(self, grid_data):
        # I can ignore this if because the play_game checks the Win first then the Draw
        if not self.check_winner(grid_data):
            return all(i.isalpha() for i in grid_data)


tictactoe = Game()
tictactoe.start_game()


def display_result(self, result):
    print("""***********************GAME OVER!***********************""")
    if result is None:
        print("'DRAW' Game ended without winner. You are even")
    else:
        print(f'Player {result[0]} with mark {result[1]} is the winner')






