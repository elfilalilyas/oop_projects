# creating the grid
import os
import time
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Grid:
    # init_data = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    def __init__(self):
        self.grid_data = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    def draw_grid(self):
        print('\n')
        print('\t\t\t_____________')
        for i in range(0, 9, 3):
            print(f"\t\t\t| {' | '.join(self.grid_data[i:i + 3])} |")
        # print(f"\t\t\t\t| {' | '.join(self.grid_data[0:3])} |")
        # print(f"\t\t\t\t| {' | '.join(self.grid_data[3:6])} |")
        # print(f"\t\t\t\t| {' | '.join(self.grid_data[6:9])} |")
        print('\t\t\t-------------')
        print('\n')

    def update_grid(self, num, mark):
        if num in range(1, 10) and self.grid_data[num - 1] == '-':
            self.grid_data[num - 1] = mark
            return True
        return False

    def empty_places(self):
        # loop over the grid and return the index of all '-'
        # I can use it to play against pc
        empty_places = []
        for ind, place in enumerate(self.grid_data):
            if place == '-':
                empty_places.append(ind + 1)
        return empty_places

    def reset_grid(self):
        # self.grid_data = Grid.init_data
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
            # print(f'Player {num}, your Mark is {player_mark}')
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
        # clear_screen()
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
        # self.turn = 1 - self.turn

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
            # self.turn = (self.turn + 1) % len(self.players)
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

        # if result is None:
        #     print("'DRAW'. Game ended without a winner.")
        # else:
        #     print(f'Player {result[0]} with mark {result[1]} is the winner')

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
            # all(not i.isdigit() for i in grid_data)
            # if all(i.isalpha() for i in grid_data):   # generator expression. its not stored
            #     return True
            # else:
            #     return False

# now I have to add new features
tictactoe = Game()
tictactoe.start_game()











# def play_game(self):
#     input('Press ENTER To Start The Game.')
#     self.g.draw_grid()
#     while True:
#         self.player_turn()
#         self.g.draw_grid()
#         if self.check_winner(self.g.grid_data) == self.players[self.turn].mark:
#             result = self.players[self.turn].name, self.players[self.turn].mark
#             break
#         if not self.check_winner(self.g.grid_data):
#             result = None
#             break
#         # the other if is for DRAW case
#     self.display_result(result)
#     choice = self.menu.display_end_game()
#     self.restart_game(choice)
#
#
# def player_turn(self):
#     player = self.players[self.turn]
#     print(f"{self.players[0].name}({self.players[0].mark}) Turn")
#     while True:
#         try:
#             place = int(input(f'{player.name} choose a cell (1-9): '))
#             if self.g.update_grid(place, player.mark):
#                 break
#             else:
#                 print('Invalid Cell Choice. Try Again')
#         except ValueError:
#             print('You Can Only Enter Numbers in region (1-9)')
#     self.turn = (self.turn + 1) % len(self.players)
#     # self.turn = 1 - self.turn
#
#
# def restart_game(self, choice):
#     self.g.reset_grid()
#     if choice == 1:
#         self.play_game()
#     else:
#         self.quit_game()
#
#     self.play_game()
#
#
# def quit_game(self):
#     return 'Thanks for playing game'
#
#
# def check_winner(self, grid_data):
#     if all(i == 'X' for i in grid_data[0:3]) or all(i == 'O' for i in grid_data[0:3]):
#         return grid_data[0]
#     if all(i == 'X' for i in grid_data[3:6]) or all(i == 'O' for i in grid_data[3:6]):
#         return grid_data[3]
#     if all(i == 'X' for i in grid_data[6:9]) or all(i == 'O' for i in grid_data[6:9]):
#         return grid_data[6]
#
#     # if grid_data[0] == grid_data[1] == grid_data[2]:
#     #     return grid_data[0]
#     # elif grid_data[3] == grid_data[4] == grid_data[5]:
#     #     return grid_data[3]
#     # elif grid_data[6] == grid_data[7] == grid_data[8]:
#     #     return grid_data[6]
#     # elif grid_data[0] == grid_data[3] == grid_data[6]:
#     #     return grid_data[0]
#     # elif grid_data[1] == grid_data[4] == grid_data[7]:
#     #     return grid_data[1]
#     # elif grid_data[2] == grid_data[5] == grid_data[8]:
#     #     return grid_data[2]
#     # elif grid_data[0] == grid_data[4] == grid_data[8]:
#     #     return grid_data[0]
#     # elif grid_data[2] == grid_data[4] == grid_data[6]:
#     #     return grid_data[2]
#     # else:
#     #     if any(i == '-' for i in grid_data):
#     #         return True
#     #     else:
#     #         return False


def display_result(self, result):
    print("""***********************GAME OVER!***********************""")
    if result is None:
        print("'DRAW' Game ended without winner. You are even")
    else:
        print(f'Player {result[0]} with mark {result[1]} is the winner')

# my class game
# class Game:
#     def __init__(self):
#         self.g = Grid()
#         self.players = [Player(), Player()]
#         self.menu = GameMenu()
#         self.turn = 0
#
#     def start_game(self):
#         self.g.draw_grid()
#         choice = self.menu.display_main_menu()
#         if choice == 2:
#             self.quit_game()
#         else:
#             self.setup_players()
#             x = self.play_game()
#             return x
#
#     def setup_players(self):
#         for ind, player in enumerate(self.players):
#             print(f"Player{ind + 1} enter your details: \n")
#             player.choose_name()
#             player.choose_mark()
#             # clear_screen()
#
#     def play_game(self):
#
#         answer = input(f"do you know the rules:")
#         if answer.upper() == 'NO':
#             self.g.get_rules()
#         print('\n\n')
#         print('Now Both of you know the rules. Lets Get Started.....\n\n')
#         # clear_screen()
#         print(
#             f"********** {self.players[0].name}({self.players[0].mark}) -VS- {self.players[1].name}({self.players[1].mark}) **********\n\n")
#         input('Press ENTER To Start The Game.')
#         while True:
#             # self.turn = 0
#             # self.g.draw_grid()
#             # player1 = self.players[self.turn]
#             # while True:
#             #     place = int(input(f'Player {player1.name} chose your goal (1---9): '))
#             #     if self.g.update_grid(place, player1.mark):
#             #         break
#
#             self.player_turn()
#             if not self.check_winner(self.g.grid_data):
#                 break
#             if self.check_winner(self.g.grid_data) == self.players[self.turn].mark:
#                 choice = self.restart_game()
#                 break
#             self.turn = (self.turn + 1) % len(self.players)
#             # self.turn = 1
#             # self.g.draw_grid()
#             # player2 = self.players[self.turn]
#             # while True:
#             #     place = int(input(f'Player {player2.name} chose your goal (1---9): '))
#             #     if self.g.update_grid(place, player2.mark):
#             #         break
#             # self.g.draw_grid()
#             # if not self.check_winner(self.g.grid_data):
#             #     ret = None
#             #     break
#             # if self.check_winner(self.g.grid_data) == player2.mark:
#             #     ret = player2.name, player2.mark
#             #     break
#         return ret
#
#     def player_turn(self):
#         self.g.draw_grid()
#         player = self.players[self.turn]
#         while True:
#             try:
#                 place = int(input(f'Player {player.name} chose your goal (1---9): '))
#                 if self.g.update_grid(place, player.mark):
#                     break
#                 else:
#                     print('Invalid Cell Choice. Try Again')
#             except ValueError:
#                 print('You Can Only Enter Numbers in region (1, 9)')
#
#     def restart_game(self):
#         self.g.reset_grid()
#         if self.menu.display_end_game() == 1:
#             self.setup_players()
#             self.play_game()
#         else:
#             self.quit_game()
#
#     def quit_game(self):
#         return 'Thanks for playing game'
#
#     def check_winner(self, grid_data):
#         if grid_data[0] == grid_data[1] == grid_data[2]:
#             return grid_data[0]
#         elif grid_data[3] == grid_data[4] == grid_data[5]:
#             return grid_data[3]
#         elif grid_data[6] == grid_data[7] == grid_data[8]:
#             return grid_data[6]
#         elif grid_data[0] == grid_data[3] == grid_data[6]:
#             return grid_data[0]
#         elif grid_data[1] == grid_data[4] == grid_data[7]:
#             return grid_data[1]
#         elif grid_data[2] == grid_data[5] == grid_data[8]:
#             return grid_data[2]
#         elif grid_data[0] == grid_data[4] == grid_data[8]:
#             return grid_data[0]
#         elif grid_data[2] == grid_data[4] == grid_data[6]:
#             return grid_data[2]
#         else:
#             if any(i == '-' for i in grid_data):
#                 return True
#             else:
#                 return False
#
#     def display_result(self, result):
#         if result is None:
#             print("'DRAW' Game ended without winner. You are even")
#         else:
#             print(f'Player {result[0]} with mark {result[1]} is the winner')
#
#
# tictactoe = Game()
# res = tictactoe.start_game()
# tictactoe.display_result(res)
# while True:
#     res = tictactoe.restart_game()
#     if res is None:
#         break
#     tictactoe.display_result(res)




















# data = [['-', '-', '-'],
#         ['-', '-', '-'],
#         ['-', '-', '-']]
# data2 = ['00', '01', '02',
#          '10', '11', '12',
#          '20', '21', '22']
#
# g = Grid(data)
# p = Player()
# game = TicTacToe(g, p)
# res = game.Start_game()
# print('Game over!..')
# game.display_result(res)
# g.draw_grid()
# g.reset_grid()
# g.draw_grid()
# print(Player.marks)
# data = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
# g = Grid()
# g.draw_grid()
# g.update_grid(5, 'O')
# g.draw_grid()
# print(g.grid_data)
# g.reset_grid()
# print(g.grid_data)


















# class Grid:
#     start_data = [['-', '-', '-'],
#                   ['-', '-', '-'],
#                   ['-', '-', '-']]
#     def __init__(self, grid_data):
#         self.grid_data = grid_data
#
#     def draw_grid(self):
#         print('\n\n')
#         print('\t\t\t\t-------------')
#         for row in self.grid_data:
#             print(f"\t\t\t\t| {' | '.join(row)} |")
#         print('\t\t\t\t-------------')
#         print('\n\n')
#
#     def place_mark(self, num, mark, data2):
#         if num in range(1, 10) and data2[num - 1].isdigit():
#             place = data2[num - 1]
#             user_choice = list(map(int, list(place)))
#             data[user_choice[0]][user_choice[1]] = mark
#             data2[num - 1] = mark
#             return True
#         else:
#             return False
#
#     # def check_winner(self):
#     #     if self.grid_data[0][0] == self.grid_data[0][1] == self.grid_data[0][2]:
#     #         return data[0][0]
#     #     elif self.grid_data[1][0] == self.grid_data[1][1] == self.grid_data[1][2]:
#     #         return data[1][0]
#     #     elif self.grid_data[2][0] == self.grid_data[2][1] == self.grid_data[2][2]:
#     #         return data[2][0]
#     #     elif self.grid_data[0][0] == self.grid_data[1][0] == self.grid_data[2][0]:
#     #         return data[0][0]
#     #     elif self.grid_data[0][1] == self.grid_data[1][1] == self.grid_data[2][1]:
#     #         return data[0][1]
#     #     elif self.grid_data[0][2] == self.grid_data[1][2] == self.grid_data[2][2]:
#     #         return data[0][2]
#     #     elif self.grid_data[0][0] == self.grid_data[1][1] == self.grid_data[2][2]:
#     #         return data[0][0]
#     #     elif self.grid_data[0][2] == self.grid_data[1][1] == self.grid_data[2][0]:
#     #         return data[0][2]
#     #     else:
#     #         if any(i.isdigit() for i in data2):
#     #             return True
#     #         else:
#     #             return False
#
#     def reset_grid(self):
#         self.grid_data = Grid.start_data
#
#
#     def get_rules(self):
#         print("""
#         ****************************RULES******************************
#         ----First you will choose your mark----------------------------
#         ----The grid is 3 * 3 matrix-----------------------------------
#         ----Your goal is to get 3 of your marks in a line--------------
#         ----The player who finish the row first  wins------------------
#         """)
#         print('''
#         | X | X | X |              | - | X | - |
#         | - | - | - |              | - | X | - |
#         | - | - | - |              | - | X | - |''')
#         print('''
#         | - | - | - |              | - | - | X |
#         | X | X | X |              | - | - | X |
#         | - | - | - |              | - | - | X |''')
#         print('''
#         | - | - | - |              | X | - | - |
#         | - | - | - |              | - | X | - |
#         | X | X | X |              | - | - | X |''')
#         print('''
#         | X | - | - |              | - | - | X |
#         | X | - | - |              | - | X | - |
#         | X | - | - |              | X | - | - |''')
#         print('''
#         ----The game ends without winner if none of you finished a line''')
#
# class Player:
#     marks = ['O', 'X']
#     def __init__(self, name='', mark=''):
#         self.name = name
#         self.mark = mark
#     def player(self, num):
#         name = input(f'Player {num}, please enter your name: ')
#         if len(Player.marks) == 2:
#             player_mark = ''
#             while player_mark not in Player.marks:
#                 player_mark = input(f'Player {num}, enter your Mark please (X/O): ').upper()
#             Player.marks.remove(player_mark)
#             return Player(name, player_mark)
#         else:
#             player_mark = Player.marks[0]
#             Player.marks = ['O', 'X']
#             print(f'Player {num}, your Mark is {player_mark}')
#             return Player(name, player_mark)
#
#         # if len(Player.marks) == 2:
#         #     mark = ''
#         #     while mark != 'X' and mark != 'O':
#         #         mark = input('Enter your Mark please (X/O): ').upper()
#         #     Player.marks.remove(mark)
#         #     return Player(name, mark)
#         # else:
#         #     return Player(name, Player.marks[0])
#
#     def choose_name(self, num):
#         player_name = input(f'Player {num}, please enter your name(alphabets only): ')
#         while not player_name.isalpha():
#             player_name = input(f'Invalid name, please enter your name(letters only): ')
#         self.name = player_name
#
#     def choose_mark(self, num):
#         if len(Player.marks) == 2:
#             player_mark = ''
#             while player_mark not in Player.marks:
#                 player_mark = input(f'Player {num}, enter your Mark please (X/O): ').upper()
#             Player.marks.remove(player_mark)
#             self.mark = player_mark
#         else:
#             player_mark = Player.marks[0]
#             Player.marks = ['O', 'X']
#             print(f'Player {num}, your Mark is {player_mark}')
#             self.mark = player_mark
#
#     def display_self(self):
#         # print(f"Player {self.name} you are welcome.")
#         # print(f'in this turn {self.mark} is your Mark.')
#         return f"{self.name}({self.mark})"
#
#
#     def make_move(self, grid):
#         place = int(input(f'Player {self.name} chose your goal (1---9): '))
#         while not grid.place_mark(place, self.mark, data2):
#             place = int(input(f'Player {self.name} chose your goal (1---9): '))
#
# class GameMenu:
#     def display_main_menu(self):
#         print("""WELCOME TO THE TIC TAC TOE GAME""")
#         print("""1- Start Game\n2- Quit Game""")
#         while True:
#             choice = int(input('Enter 1 To Start The Game, 2 To Quit The Game: '))
#             if choice == 1 or choice == 2:
#                 break
#             print('Invalid Choice. You Have Only Two Options (1 or 2)')
#         return choice
#
#     def display_end_game(self):
#         print("""GAME OVER!""")
#         print("""1- Restart Game\n2- Quit Game""")
#         while True:
#             choice = int(input('Enter 1 To Restart The Game, 2 To Quit The Game: '))
#             if choice == 1 or choice == 2:
#                 break
#             print('Invalid Choice. You Have Only Two Options (1 or 2)')
#         return choice
#
# class TicTacToe:
#     def __init__(self, grid, player):
#         self.g = grid
#         self.p = player
#
#     def Start_game(self):
#         self.g.draw_grid()
#         print("""WELCOME TO THE TIC TAC TOE GAME""")
#         player1 = self.p.player(1)
#         player2 = self.p.player(2)
#         answer = input(f"do you know the rules:")
#         if answer.upper() == 'NO':
#             self.g.get_rules()
#         print('\n\n')
#         print('Now Both of you know the rules. Lets Get Started.....\n\n')
#         # clear_screen()
#         print(f"********** {player1.display_self()} -VS- {player2.display_self()} **********\n\n")
#         input('Press ENTER To Start The Game.')
#         while True:
#             player1.make_move(self.g)
#             self.g.draw_grid()
#             if not self.check_winner(self.g.grid_data):
#                 return None
#             if self.check_winner(self.g.grid_data) == player1.mark:
#                 return player1.name, player1.mark
#             player2.make_move(self.g)
#             self.g.draw_grid()
#             if not self.check_winner(self.g.grid_data):
#                 return None
#             if self.check_winner(self.g.grid_data) == player2.mark:
#                 return player2.name, player2.mark
#
#     def restart_game(self):
#         pass
#
#     def quit_game(self):
#         pass
#
#     def check_winner(self, grid_data):
#         if grid_data[0][0] == grid_data[0][1] == grid_data[0][2]:
#             return data[0][0]
#         elif grid_data[1][0] == grid_data[1][1] == grid_data[1][2]:
#             return data[1][0]
#         elif grid_data[2][0] == grid_data[2][1] == grid_data[2][2]:
#             return data[2][0]
#         elif grid_data[0][0] == grid_data[1][0] == grid_data[2][0]:
#             return data[0][0]
#         elif grid_data[0][1] == grid_data[1][1] == grid_data[2][1]:
#             return data[0][1]
#         elif grid_data[0][2] == grid_data[1][2] == grid_data[2][2]:
#             return data[0][2]
#         elif grid_data[0][0] == grid_data[1][1] == grid_data[2][2]:
#             return data[0][0]
#         elif grid_data[0][2] == grid_data[1][1] == grid_data[2][0]:
#             return data[0][2]
#         else:
#             if any(i.isdigit() for i in data2):
#                 return True
#             else:
#                 return False
#
#     def display_result(self, result):
#         if result is None:
#             print('Game ended without winner. You are even')
#         else:
#             print(f'Player {result[0]} with mark {result[1]} is the winner')
#
#
#
# data = [['-', '-', '-'],
#         ['-', '-', '-'],
#         ['-', '-', '-']]
# data2 = ['00', '01', '02',
#          '10', '11', '12',
#          '20', '21', '22']
#
# g = Grid(data)
# p = Player()
# game = TicTacToe(g, p)
# res = game.Start_game()
# print('Game over!..')
# game.display_result(res)
# g.draw_grid()
# g.reset_grid()
# g.draw_grid()
# print(Player.marks)













# from turtle import Turtle, Screen
# window = Screen()
# window.setup(width=600, height=600)
# window.bgcolor('black')               # bgcolor = background color
# window.title('Octucode:* Turtles Race *')
#
#
# border = Turtle()
# border.speed(0)
# border.hideturtle()
# def draw_grid():
#     border.penup()
#     border.color('white')
#     border.goto(240, 240)
#     border.pendown()
#     border.pensize(5)
#     for i in range(4):
#         border.right(90)
#         border.forward(480)
#
#     border.right(90)
#     border.goto(240, 80)
#     border.right(90)
#     border.forward(480)
#     border.left(90)
#     border.forward(160)
#     border.left(90)
#     border.forward(480)
#     border.penup()
#     border.goto(80, -240)
#     border.pendown()
#     border.left(90)
#     border.forward(480)
#     border.left(90)
#     border.forward(160)
#     border.left(90)
#     border.forward(480)
#
#
# def draw_x(x, y):
#     border.setheading(180)
#     border.penup()
#     border.goto(x, y)
#     border.left(45)
#     border.pendown()
#     border.goto(x - 140, y - 140)
#     border.penup()
#     border.goto(x, y - 140)
#     border.pendown()
#     border.setheading(180)
#     border.right(45)
#     border.goto(x - 140, y)
#
#
# def draw_O(x, y):
#     border.setheading(0)
#     border.penup()
#     border.goto(x, y)
#     border.pendown()
#     border.circle(70)
#
#
# draw_grid()
# x_draws = ((-90, 230), (70, 230), (230, 230), (-90, 70), (70, 70),
#            (230, 70), (-90, -90), (70, -90), (230, -90))
#
# o_draws = ((-160, 90), (0, 90), (160, 90), (-160, -70), (0, -70),
#            (160, -70), (-160, -230), (0, -230), (160, -230))
#
#
#
#
# # while True:
# #     choice = int(window.textinput('Inputs', 'enter plac (1-9)'))
# #     draw_x(*x_draws[choice - 1])
# #     if choice not in range(1, 10):
# #         break
#
#
#
#
#
#
#
#
# window.exitonclick()





















# class Grid:
#     marks = ['O', 'X']
#     def __init__(self, grid_data):
#         self.grid_data = grid_data
#
#     def draw_grid(self):
#         print('\n\n')
#         print('\t\t\t\t-------------')
#         for row in self.grid_data:
#             print(f"\t\t\t\t| {' | '.join(row)} |")
#         print('\t\t\t\t-------------')
#         print('\n\n')
#
#
#
#     def player(self, num):
#         name = input(f'Player {num}, please enter your name: ')
#         if len(Grid.marks) == 2:
#             mark = ''
#             while mark != 'X' and mark != 'O':
#                 mark = input('Enter your Mark please (X/O): ').upper()
#             Grid.marks.remove(mark)
#             return Player(name, mark)
#         else:
#             return Player(name, Grid.marks[0])
#
#     def get_rules(self):
#         print("""
#         ****************************RULES******************************
#         ----First you will choose your mark----------------------------
#         ----The grid is 3 * 3 matrix-----------------------------------
#         ----Your goal is to get 3 of your marks in a line--------------
#         ----The player who finish the row first  wins------------------
#         """)
#         print('''
#         | X | X | X |              | - | X | - |
#         | - | - | - |              | - | X | - |
#         | - | - | - |              | - | X | - |''')
#         print('''
#         | - | - | - |              | - | - | X |
#         | X | X | X |              | - | - | X |
#         | - | - | - |              | - | - | X |''')
#         print('''
#         | - | - | - |              | X | - | - |
#         | - | - | - |              | - | X | - |
#         | X | X | X |              | - | - | X |''')
#         print('''
#         | X | - | - |              | - | - | X |
#         | X | - | - |              | - | X | - |
#         | X | - | - |              | X | - | - |''')
#         print('''
#         ----The game ends without winner if none of you finished a line''')
#
#
#
# class Player:
#     def __init__(self, name, mark):
#         self.name = name
#         self.mark = mark
#     def display_self(self):
#         print(f"Player {self.name} you are welcome.")
#         print(f'in this turn {self.mark} is your Mark.')
#
# def update_data(num, mark, data, data2):
#     if data2[num - 1].isdigit():
#         place = data2[num - 1]
#         user_choice = list(map(int, list(place)))
#         data[user_choice[0]][user_choice[1]] = mark
#         data2[num - 1] = mark
#         return True
#     else:
#         return False
#
# def check_winner(data):
#     if data[0][0] == data[0][1] == data[0][2]:
#         return data[0][0]
#     elif data[1][0] == data[1][1] == data[1][2]:
#         return data[1][0]
#     elif data[2][0] == data[2][1] == data[2][2]:
#         return data[2][0]
#     elif data[0][0] == data[1][0] == data[2][0]:
#         return data[0][0]
#     elif data[0][1] == data[1][1] == data[2][1]:
#         return data[0][1]
#     elif data[0][2] == data[1][2] == data[2][2]:
#         return data[0][2]
#     elif data[0][0] == data[1][1] == data[2][2]:
#         return data[0][0]
#     elif data[0][2] == data[1][1] == data[2][0]:
#         return data[0][2]
#     else:
#         if any(i.isdigit() for i in data2):
#             return True
#         else:
#             return False
#
#
#
# data = [['-', '-', '-'],
#         ['-', '-', '-'],
#         ['-', '-', '-']]
# data2 = ['00', '01', '02',
#          '10', '11', '12',
#          '20', '21', '22']
#
# g = Grid(data)
#
# def TicTacToe():
#     g.draw_grid()
#     print("""WELCOME TO THE TIC TAC TOE GAME""")
#     player1 = g.player(1)
#     player2 = g.player(2)
#     answer = input(f"do you know the rules:")
#     if answer.upper() == 'NO':
#         g.get_rules()
#     print('\n\n')
#     print('Now Both of you know the rules. Lets Get Started.....')
#     input('Press ENTER To Start The Game.')
#     while True:
#         r1 = int(input(f'Player {player1.name} chose your goal (1---9): '))
#         while not update_data(r1, player1.mark, data, data2):
#             r1 = int(input(f'Player {player1.name} chose your goal (1---9): '))
#         g.draw_grid()
#         if not check_winner(data):
#             return None
#         if check_winner(data) == player1.mark:
#             return player1.name, player1.mark
#         r2 = int(input(f'Player {player2.name} chose your goal (1---9): '))
#         while not update_data(r2, player2.mark, data, data2):
#             r2 = int(input(f'Player {player2.name} chose your goal (1---9): '))
#         g.draw_grid()
#         if not check_winner(data):
#             return None
#         if check_winner(data) == player2.mark:
#             return player2.name, player2.mark
#
#
#
# result = TicTacToe()
# print('Game over!..')
# if result is None:
#     print('Game ended without winner. You are even')
# else:
#     print(f'Player {result[0]} with mark {result[1]} is the winner')





