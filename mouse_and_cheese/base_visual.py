from functools import lru_cache

import pygame as pg


class BaseVisual:
    """Class that draws all elements of the designing and training."""

    PADDING = 2     # Width of grid lines - should be even

    def __init__(self, settings: dict) -> None:

        # Prepare the Cat and Cheese positions
        self.cats: set[tuple[int, int]]
        self.cheese: tuple[int,int]

        # Limit the screen size to 1600x900
        self.grid_size = settings['grid_size']
        self.tile_size = min(
            (1600 - self.PADDING) // self.grid_size[0],
            (900 - self.PADDING) // self.grid_size[1],
        ) - self.PADDING
        screen_size = (
            self.grid_position_to_pixels((self.grid_size[0], self.grid_size[1]))
        )

        # Pygame initialisation
        self.screen = pg.display.set_mode(screen_size)
        self.clock = pg.time.Clock()

    def gridline_position_to_pixels(self, position: tuple[int, int]) -> None:
        """Convert a gridline position to its pixel position.
        """

        return (
            position[0] * (self.PADDING + self.tile_size) + self.PADDING//2 - 1,
            position[1] * (self.PADDING + self.tile_size) + self.PADDING//2 - 1,
        )
    
    def draw_grid(self) -> None:
        """Draw the grid lines."""

        for i in range(0, self.grid_size[0] + 1):
            pg.draw.line(
                self.screen,
                'grey',
                self.gridline_position_to_pixels((i, 0)),
                self.gridline_position_to_pixels((i, self.grid_size[1] + 1)),
                width = self.PADDING,
            )

        for j in range(0, self.grid_size[1] + 1):
            pg.draw.line(
                self.screen,
                'grey',
                self.gridline_position_to_pixels((0, j)),
                self.gridline_position_to_pixels((self.grid_size[0] + 1, j)),
                width = self.PADDING,
            )

    @lru_cache
    def grid_position_to_pixels(self, position: tuple[int, int]) -> None:
        """Convert a grid position to its pixel position."""

        return (
            position[0] * (self.PADDING + self.tile_size) + self.PADDING,
            position[1] * (self.PADDING + self.tile_size) + self.PADDING,
        )
    
    def draw_cats(self) -> None:
        """Draw a Cat at all grid positions in self.cats."""

        cats = [
            pg.Rect(
                (self.grid_position_to_pixels(cat)),
                (self.tile_size, self.tile_size)
            ) for cat in self.cats
        ]
        for cat in cats:
            pg.draw.rect(self.screen, 'black', cat)
    
    def draw_cheese(self) -> None:
        """Draw the Cheese on the grid."""

        cheese = pg.Rect(
            (self.grid_position_to_pixels(self.cheese)),
            (self.tile_size, self.tile_size),
        )
        pg.draw.rect(self.screen, 'yellow', cheese)

    def draw_mouse(self, mouse_position: tuple[int, int]) -> None:
        """Draw the Mouse on the grid."""

        mouse = pg.Rect(
            (self.grid_position_to_pixels(mouse_position)),
            (self.tile_size, self.tile_size),
        )
        pg.draw.rect(self.screen, 'grey', mouse)
