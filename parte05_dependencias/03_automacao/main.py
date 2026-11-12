import pyautogui as auto


def main():
    auto.PAUSE = 0.75

    auto.press("win")
    auto.write("chrome")
    auto.press("enter")
    auto.sleep(2)
    auto.write("globo.com")
    auto.press("enter")
    auto.hotkey("ctrl","t")
    auto.sleep(2)
    auto.write("sistemafibra.org.br/senai")
    auto.press("enter")
    auto.hotkey("ctrl","shift","n")
    auto.sleep(3)
    auto.write("metropoles.com")
    auto.press("enter")


if __name__ == "__main__":
    main()