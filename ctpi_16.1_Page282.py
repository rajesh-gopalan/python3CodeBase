#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11/24/2017

@author: rajesh-gopalan

16.1 Given a sorted array of positive integers with an empty spot (zero) at the
end, insert an element in sorted order

"""

TRUE = 1
FALSE = 0
DEBUG  = FALSE

arrayVal = []
newElement = 0

def getArray(debug_flag):
    if debug_flag == 1:
        print('### getArray() - Start')
    print('Please enter the positive, sorted array values separated by spaces (last element must be a zero):')
    arrayInput = input().split(' ') # Takes in a string of numbers separated by a space
    arrayVal = [int(num) for num in arrayInput]
    if debug_flag == 1:
        print('### getArray() - End');
    return arrayVal;

def getNewElement(debug_flag):
    if debug_flag == 1:
        print('### getNewElement() - Start')
    print('Please enter the new element to be inserted:')
    if debug_flag == 1:
        print('### getNewElement() - End');
    return int(input());

def insertNewElement(debug_flag, origArrayVal, newElementVal):
    if debug_flag == 1:
        print('### insertNewElement() - Start')
    indexVal = len(origArrayVal) - 1
    if (origArrayVal[indexVal] != 0) | (newElementVal <= 0):
        if debug_flag == 1:
            print('indexVal   = ', str(indexVal))
            print('newElement = ', str(newElement))
        return origArrayVal, FALSE;
    while (indexVal >= 0) & (origArrayVal[indexVal - 1] >= newElementVal):
        if debug_flag == 1:
            print('indexVal         = ', indexVal)
            print('arrayVal[', str(indexVal), ']    = ', str(origArrayVal[indexVal - 1]))
            print('newElement       = ', str(origArrayVal[indexVal - 1]));
        origArrayVal[indexVal]     = origArrayVal[indexVal - 1]
        origArrayVal[indexVal - 1] = newElementVal;
        indexVal -= 1;
    if debug_flag == 1:
        print('### insertNewElement() - End');
    return origArrayVal, TRUE;

arrayVal = getArray(DEBUG)
newElement = getNewElement(DEBUG)
print('Original array = ', str(arrayVal))
print('New element    = ', str(newElement))
newArray, resultFlag = insertNewElement(DEBUG, arrayVal, newElement)
if resultFlag:
    print('Updated array  = ', str(newArray));
else:
    print('Erorr: Please satisfy requirements.');
