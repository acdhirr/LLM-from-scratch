

def run():

    with open("../resources/the-verdict-edith-wharton.txt", "r", encoding="utf-8") as textfile:
        raw = textfile.read()
        print(raw)


if __name__ == '__main__':
    run()

