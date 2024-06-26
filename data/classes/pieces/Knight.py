import pygame

from data.classes.Piece import Piece
from data.classes.ImageLoader import resource_path


class Knight(Piece):
    def __init__(self, pos, colour, board):
        super().__init__(pos, colour, board)

        img_path = 'data/imgs/' + colour[0] + '_knight.png'
        self.img = pygame.image.load(resource_path(img_path))
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

        self.notation = 'N'

    def get_possible_moves(self, board):
        output = []
        moves = [
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2)
        ]

        for move in moves:
            new_pos = (self.x + move[0], self.y + move[1])
            if (
                    new_pos[0] < 8 and
                    new_pos[0] >= 0 and
                    new_pos[1] < 8 and
                    new_pos[1] >= 0
            ):
                output.append([
                    board.get_square_from_pos(
                        new_pos
                    )
                ])

        return output
