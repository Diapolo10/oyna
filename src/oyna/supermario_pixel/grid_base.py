from itertools import cycle
from time import sleep

images = [
    """
          🟥🟥🟥🟥🟥
        🟥🟥🟥🟥🟥🟥🟥🟥🟥
        🟫🟫🟫🟨🟨⬛️🟨
      🟫🟨🟫🟨🟨🟨⬛️🟨🟨🟨
      🟫🟨🟫🟫🟨🟨🟨⬛️🟨🟨🟨
        🟫🟨🟨🟨🟨⬛️⬛️⬛️⬛️
          🟨🟨🟨🟨🟨🟨
        🟥🟥🟦🟥🟥🟦🟥🟥
      🟥🟥🟥🟦🟥🟥🟦🟥🟥🟥
    🟥🟥🟥🟥🟦🟥🟥🟦🟥🟥🟥🟥
    🟨🟨🟥🟥🟦🟦🟦🟦🟥🟥🟨🟨
    🟨🟨🟨🟦🟦🟦🟦🟦🟦🟨🟨🟨
    🟨🟨🟦🟦🟦🟦🟦🟦🟦🟦🟨🟨
        🟦🟦🟦    🟦🟦🟦
      🟫🟫🟫        🟫🟫🟫
    🟫🟫🟫🟫        🟫🟫🟫🟫
    """,
    """
          🟥🟥🟥🟥🟥    🟨🟨🟨
        🟥🟥🟥🟥🟥🟥🟥🟥🟥🟨🟨
        🟫🟫🟫🟨🟨⬛️🟨  🟥🟥🟥
      🟫🟨🟫🟨🟨🟨⬛️🟨🟨🟨🟥🟥
      🟫🟨🟫🟫🟨🟨🟨⬛️🟨🟨🟨🟥
        🟫🟨🟨🟨🟨⬛️⬛️⬛️⬛️🟥🟥    ♥️  SUPER MARIO ♥️
          🟨🟨🟨🟨🟨🟨🟥🟥🟥
        🟥🟥🟦🟥🟥🟦🟥🟥🟥
      🟥🟥🟥🟦🟥🟥🟦🟥🟥🟥
    🟥🟥🟥🟥🟦🟥🟥🟦🟥🟥
    🟨🟨🟥🟥🟦🟦🟦🟦🟥🟥
    🟨🟨🟨🟦🟦🟦🟦🟦🟦🟦
    🟨🟨🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦    🟦🟦🟦
      🟫🟫🟫        🟫🟫🟫
    🟫🟫🟫🟫        🟫🟫🟫🟫
    """,
]


def run() -> None:
    for image in cycle(images):
        print("\033[H\033[J" + image)
        sleep(0.5)


if __name__ == "__main__":
    run()
