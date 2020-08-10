# -*- coding: utf-8 -*-

import os


def main():
    old_path = './txt'
    new_path = './newtxt'
    gt_list = os.listdir(old_path)
    for gt in gt_list:
        with open(os.path.join(old_path, gt), 'r', encoding='utf-8') as rf, open(os.path.join(new_path, gt), 'a', encoding='utf-8') as wf:
            for line in rf.readlines():
                line = line.strip().split(',')
                four_points = []
                four_points.extend(line[0:2])
                four_points.extend([line[2], line[1]])
                four_points.extend(line[2:4])
                four_points.extend([line[0], line[3]])
                new_line = four_points + line[4:]
                wf.write(','.join(new_line) + '\n')


if __name__ == "__main__":
    main()
