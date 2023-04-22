# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 19:48:15 2022

@author: Dineth
"""
def file_read():
  
  file = open('inputfile.txt','r')
  for line in file:
    line_split = line.split()
    if line_split[2] == 'P':
      print(line)
  file.close()


def file_write():
  file = open('Passfile.txt','w')
  inputFile = open('inputfile.txt','r')
  for line in inputFile:
    line_split = line.split()
    if line_split[2] == 'P':
      file.write(line)
  file.close()
  inputFile.close()
