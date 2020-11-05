# Don't Get Volunteered https://foobar.withgoogle.com/
class Node():
    def __init__(self, cord, ):
        self._cord = cord

    def get_cord(self):
        return self._cord

    def get_up(self):
        if self.get_cord()%8:
            return self.get_cord() - 8
        return None

    def get_down(self):
        if Node.isCordNormal(self.get_cord()):
            return self.get_cord() + 8;
        return None

    def get_right(self):
        if self.get_cord() % 8 == 1:  # It has right wall
            return None
        return self.get_cord()

    @staticmethod
    def isCordNormal(cord):  # Check if cord is an allowed cordinate
        return 1 <= cord <= 64


def main():
    x = []
    for i in range(1, 65):
        x.append(Node(i))
    for item in x:
        print(item.get_cord(),item.get_up())


if __name__ == '__main__':
    main()
