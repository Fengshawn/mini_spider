#爬虫主程序
from DataModule import hello_world


def main():
    """Parse options and execute commands."""
    hello_world.hello()
    hello_world.goodbye()


if __name__ == '__main__':
    main()


# with open('urls', 'r') as f:
#     a = f.readline()





