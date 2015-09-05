#! /usr/bin/python3.4
#-*-coding:utf-8-*-

import os

#记住.in文件中的data地址也要修改到正确地址
#在.in 文件中修改需要run那个聚类方法，以及其他参数，具体见/doc/knldoc.pdf

cmd='./kmltest -i ../test/test0.in -o ../test/t0.save'
os.system(cmd)

