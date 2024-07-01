import pygame as pg

from mouse_and_cheese.base_visual import BaseVisual
from mouse_and_cheese.entity import Entity, EntityCollection


class Design(BaseVisual):
    """Class for placing the Mouse, Cats and Cheese."""

    def __init__(self, settings: dict) -> None:

        # Pygame initialisation
        super().__init__(settings)
        pg.display.set_caption("Mouse finds Cheese")
        
        # Track current design
        self.start = (0, 0)
        self.cats = set()
        self.cheese = (self.grid_size[0] - 1, self.grid_size[1] - 1)

        # Track current mode
        self.current_entity = Entity.CAT

    def check_events(self) -> bool:
        """Check for Mouse, Cats and Cheese placement.
        
        Returns True if the pg.K_RETURN is pressed.
        """

        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()

            elif event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                cell = (
                    pos[0] // (self.tile_size + self.PADDING),
                    pos[1] // (self.tile_size + self.PADDING),
                )
                match self.current_entity:
                    case Entity.CAT:
                        if cell not in {self.start, self.cheese}:
                            self.cats.add(cell)
                    case Entity.CHEESE:
                        if cell not in self.cats | {self.start}:
                            self.cheese = cell
                    case Entity.MOUSE:
                        if cell not in self.cats | {self.cheese}:
                            self.start = cell
                    case Entity.NONE:
                        self.cats.discard(cell)

            elif event.type == pg.KEYDOWN:

                if event.key == pg.K_LEFT:
                    self.current_entity = Entity(
                        (self.current_entity.value - 1) % len(Entity)
                    )

                elif event.key == pg.K_RIGHT:
                    self.current_entity = Entity(
                        (self.current_entity.value + 1) % len(Entity)
                    )

                elif event.key == pg.K_RETURN:
                    return True

        return False

    def draw_current_entity(self) -> None:
        """Draw the current entity on the mouse position."""

        pos = pg.mouse.get_pos()
        entity_rect = pg.Rect((0,0), (self.tile_size // 2, self.tile_size // 2))
        entity_rect.center = pos
        match self.current_entity:
            case Entity.CAT:
                sprite = super().cat_sprite
            case Entity.CHEESE:
                sprite = super().cheese_sprite
            case Entity.MOUSE:
                sprite = super().mouse_sprite
            case Entity.NONE:
                return
        pg.transform.scale(sprite, (self.tile_size // 2, self.tile_size // 2))
        self.screen.blit(sprite, entity_rect)

    def update_screen(self) -> None:
        """Draw the current frame to the screen."""

        self.screen.fill('white')
        super().draw_grid()
        super().draw_cats()
        super().draw_cheese()
        super().draw_mouse(self.start)
        self.draw_current_entity()
        pg.display.flip()

    def run(self) -> EntityCollection:
        """Run the main loop."""

        self.update_screen()

        while not self.check_events():
            self.update_screen()
            self.clock.tick(60)

        return EntityCollection(self.start, self.cats, self.cheese)
