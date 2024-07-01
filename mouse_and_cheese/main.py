from mouse_and_cheese.design import Design
from mouse_and_cheese.settings import settings
from mouse_and_cheese.train import Train


def main() -> None:

    designer = Design(settings)
    train = Train(settings, *designer.run())
    train.run()
