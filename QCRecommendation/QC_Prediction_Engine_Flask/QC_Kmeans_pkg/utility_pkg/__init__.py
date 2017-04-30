import item_presentation as ip
import os

if __name__ == '__main__':
    test_uti = ip.util()
    print os.path.dirname(os.path.abspath(__file__))
    test_uti.parse_save('types.txt')