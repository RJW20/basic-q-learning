import pygame as pg

from mouse_and_cheese.base_visual import BaseVisual
from q_learning import Action, Agent, QTable, RewardTable, State


class Train(BaseVisual):
    """Class that trains a Mouse to get to the Cheese using simple
    Q-learning."""

    def __init__(
        self,
        settings: dict,
        start: tuple[int, int],
        cats: set[tuple[int, int]],
        cheese: tuple[int,int],
    ) -> None:
        
        # Pygame initialisation
        super().__init__(settings)
        pg.display.set_caption("Mouse finds Cheese")

        # Store the set up
        self.cats = cats
        self.cheese = cheese

        # Unpack the settings
        learning_rate = settings['learning_rate']
        discount_factor = settings['discount_factor']

        # Create the QTable
        states = self.states
        states_and_actions = [
            (state, [
                action for action in self.actions
                if state._identifier not in self.cats | {self.cheese} and
                action.act_on(state) in states
            ])
            for state in states
        ]
        q_table = QTable(states_and_actions)

        # Create the RewardTable
        states_actions_rewards = []
        for state, actions in states_and_actions:
            actions_rewards = []
            for action in actions:
                if (next_identifier := action.act_on(state)._identifier) \
                    in self.cats:
                    reward = -10    # -10 for hitting a Cat
                elif next_identifier == self.cheese:
                    reward = 100    # 100 for eating the Cheese
                else:
                    reward = 0
                actions_rewards.append((action, reward))
            states_actions_rewards.append((state, actions_rewards))
        reward_table = RewardTable(states_actions_rewards)
        
        # Create the Agent
        self.mouse = Agent(
            State((start)),
            reward_table,
            q_table,
            learning_rate,
            discount_factor,
        )

    @property
    def states(self) -> set[State]:
        """Return a set of all possible States.
        
        This is comprised of all positions contained in the grid with size
        self.grid_size.
        """

        return {State((x, y)) for x in range(0, self.grid_size[0])
                  for y in range(0, self.grid_size[1])}
    
    @property
    def actions(self) -> list[Action]:
        """Return a list of all possible Actions.
        
        This is comprised of movements to adjacent grid positions.
        """

        return [
            Action(lambda x: (x[0], x[1] - 1)),     # Up
            Action(lambda x: (x[0] + 1, x[1])),     # Right
            Action(lambda x: (x[0], x[1] + 1)),     # Down
            Action(lambda x: (x[0] - 1, x[1])),     # Left
        ]

    def check_events(self) -> None:
        """Check for new user inputs."""

        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()

    def update_screen(self) -> None:
        """Draw the current frame to the screen."""

        self.screen.fill('white')
        super().draw_grid()
        super().draw_cats()
        super().draw_cheese()
        super().draw_mouse(self.mouse.current_state._identifier)
        pg.display.flip()

    def run(self) -> None:
        """Run the main loop."""

        self.update_screen()

        while True:
            self.check_events()
            self.mouse.next_state()
            self.update_screen()
            self.clock.tick(100)
