import argparse
import traceback
import os
import sys
sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('..'))
from evaluate_segmentation import evaluate_segmentation
from manually_segmentation import manually_segmentation

line = '*' * 50
menu = "\nPERFORMANCE TOOL\n" \
       "1) Press 1 to manually segment the image\n" \
       "2) Press 2 to evaluate programmatically segmentation\n"

menu = line + menu + line

if __name__ == '__main__':
    print(menu)

    selection = False

    while True:
        try:
            ans = input()
            ex = False

            if ans == '1':
                ex = manually_segmentation()

            elif ans == '2':
                ex = evaluate_segmentation()

            if not ex:
                print('Something goes wrong, repeat!')
                print(menu)
            else:
                break
        except KeyboardInterrupt:
            break
        except:
            traceback.print_exc()
