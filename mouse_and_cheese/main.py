import pygame as pg

from q_learning import Action, Agent, QTable, RewardTable, State


class Main:
    """Class that trains a Mouse to get to the Cheese using simple
    Q-learning."""

    def __init__(self) -> None:

        self.size = (10, 10)
        self.start = (0, 0)
        self.cats = {(i, 3) for i in range(0, self.size[0] - 2)} | \
                    {(i, 7) for i in range(2, self.size[0])}
        self.cheese = (self.size[0] - 1, self.size[1] - 1)
        learning_rate = 1
        discount_factor = 0.5

        # Create all the States and Actions
        states = {State((x, y)) for x in range(0, self.size[0])
                  for y in range(0, self.size[1])}
        actions = [
            Action(lambda x: (x[0], x[1] - 1)),     # Up
            Action(lambda x: (x[0] + 1, x[1])),     # Right
            Action(lambda x: (x[0], x[1] + 1)),     # Down
            Action(lambda x: (x[0] - 1, x[1])),     # Left
        ]

        # Pair all valid States and Actions
        states_and_actions = [
            (state, [
                action for action in actions
                if state._identifier not in self.cats | {self.cheese} and
                action.act_on(state) in states
            ])
            for state in states
        ]

        # Set up all rewards
        states_actions_rewards = []
        for state, actions in states_and_actions:
            actions_rewards = []
            for action in actions:
                if (next_identifier := action.act_on(state)._identifier) \
                    in self.cats:
                    reward = -10
                elif next_identifier == self.cheese:
                    reward = 100
                else:
                    reward = 0
                actions_rewards.append((action, reward))
            states_actions_rewards.append((state, actions_rewards))

        # Load all components
        reward_table = RewardTable(states_actions_rewards)
        q_table = QTable(states_and_actions)
        self.mouse = Agent(
            State((self.start)),
            reward_table,
            q_table,
            learning_rate,
            discount_factor,
        )

        # Pygame initialisation
        self.tile_size = 45
        screen_size = (
            self.size[0] * self.tile_size,
            self.size[1] * self.tile_size
        )
        self.screen = pg.display.set_mode(screen_size)
        pg.display.set_caption("Mouse finds Cheese")
        self.clock = pg.time.Clock()

    def check_events(self) -> None:
        """Check for new user inputs."""

        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()

    def position_to_pixels(self, position: tuple[int, int]) -> None:
        """Convert a State position to its pixel position."""
        return position[0] * self.tile_size, position[1] * self.tile_size

    def update_screen(self) -> None:
        """Draw the current frame to the screen."""

        # Wipe the last frame
        self.screen.fill('white')

        # Draw the mouse
        mouse = pg.Rect(
            (self.position_to_pixels(self.mouse.current_state._identifier)),
            (self.tile_size, self.tile_size),
        )
        pg.draw.rect(self.screen, 'grey', mouse)

        # Draw the cats
        cats = [
            pg.Rect(
                (self.position_to_pixels(cat)),
                (self.tile_size, self.tile_size)
            ) for cat in self.cats
        ]
        for cat in cats:
            pg.draw.rect(self.screen, 'black', cat)

        # Draw the cheese
        cheese = pg.Rect(
            (self.position_to_pixels(self.cheese)),
            (self.tile_size, self.tile_size),
        )
        pg.draw.rect(self.screen, 'yellow', cheese)

        #update the screen
        pg.display.flip()

    def run(self) -> None:
        """Run the main loop."""

        self.update_screen()

        while True:
            self.check_events()
            self.mouse.next_state()
            self.update_screen()
            self.clock.tick(100)

if __name__ == '__main__':
    main = Main()
    main.run()
