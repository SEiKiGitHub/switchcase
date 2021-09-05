import random

def main():
    switch = {
        1: 'woaf',
        2: 'Meow',
        3: 'Grouink',
        4: 'meuh'
    }

    command = random.randint(1, 4)
    x = switch.get(command)
    print(x)


if __name__ == '__main__':
    main()

