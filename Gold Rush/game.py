from Matrix import Matrix
import random
class GoldRush(Matrix):
    WINNING_SCORE = 100
    COIN = "$"
    WALL = "wall"
    EMPTY = "."
    MIN_COINS = 10
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.player1_score = 0
        self.player2_score = 0
        self.winner = ""
        self.total_coins = 0

    def _is_empty_board_size(self):
        return self.rows == 0 and self.cols == 0

    def _set_empty_board(self):
        self.matrix = []
        self.total_coins = 0

    def _build_random_board(self):
        self.matrix = []
        self.total_coins = 0

        for row_index in range(self.rows):
            row = self._create_row(row_index)
            self.matrix.append(row)

    def _create_row(self, row_index):
        if self._is_wall_row(row_index):
            row = [self.WALL] * self.cols
        else:
            row = [self._random_coin_or_empty() for _ in range(self.cols)]

        self._scatter_random_cells(row)
        return row

    def _is_wall_row(self, row_index):
        return row_index % 2 == 0

    def _scatter_random_cells(self, row):
        step = random.randint(1, 2)
        for col in range(1, self.cols, step):
            row[col] = self._random_coin_or_empty()

    def _random_coin_or_empty(self):
        return random.choice([self.COIN, self.EMPTY])

    def _place_players(self):
        self.matrix[0][0] = "player1"
        self.matrix[self.rows - 1][self.cols - 1] = "player2"

    def _count_coins(self):
        return sum(cell == self.COIN for row in self.matrix for cell in row)

    def load_board(self):
        if self._is_empty_board_size():
            self._set_empty_board()
            return
        self._build_random_board()
        self._place_players()
        self.total_coins = self._count_coins()
        if self.total_coins < self.MIN_COINS:
            return self.load_board()
        return self.matrix

    def _check_win(self, player):
        player_num = player[-1]
        score = getattr(self, f"player{player_num}_score")
        if score == self.WINNING_SCORE:
            self.winner = player
            return self.winner

    def _check_other_player(self, player):
        otherPlayer = None
        if player == "player1":
            otherPlayer = "player2"
            return otherPlayer
        elif player == "player2":
            otherPlayer = "player1"
            return otherPlayer

    def _move(self, curr_row, curr_col, player, delta_row, delta_col):
        other_player = self._check_other_player(player)
        new_row, new_col = curr_row + delta_row, curr_col + delta_col

        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return

        if self.matrix[new_row][new_col] not in [self.WALL, other_player]:
            if self.matrix[new_row][new_col] == self.COIN:
                self._increase_score(player)

            self.matrix[curr_row][curr_col] = self.EMPTY
            self.matrix[new_row][new_col] = player

        return self._check_win(player)

    def _move_down(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 1, 0)

    def _move_up(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, -1, 0)

    def _move_right(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 0, 1)

    def _move_left(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 0, -1)

    def move_player(self, player, direction):
        curr_row, curr_col = None, None

        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                if value == player:
                    curr_row, curr_col = i, j
                    break
            if curr_row is not None:
                break

        if direction == "down":
            self._move_down(curr_row, curr_col, player)
        elif direction == "up":
            self._move_up(curr_row, curr_col, player)
        elif direction == "right":
            self._move_right(curr_row, curr_col, player)
        elif direction == "left":
            self._move_left(curr_row, curr_col, player)

    def _increase_score(self, player):
        player_num = player[-1]
        score_attr = f"player{player_num}_score"
        setattr(self, score_attr, getattr(self, score_attr) + 10)
        print(getattr(self, score_attr))
