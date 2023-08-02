# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 16:29:11 2023

@author: agam
"""

import logging
logging.basicConfig(filename=("test2.log"), level = logging.DEBUG, format= '%(asctime)s %(name)s %(levelname)s %(message)s' )
l = [1,2,3,4,5,6,7,8,9, "agam", "nitai", "gaura", "krsna"]
l1 = []
l2 = []
for i in l:
    logging.info("inside the loop")
    if type(i)==int:
        logging.info("inside the int checking loop for integer "+str(i))
        l1.append(i)
        logging.info("the integer "+str(i)+" is added to the list l1")
    else :
        logging.info("inside the str checking loop for string "+ i)
        l2.append(i)
        logging.info("the string " + i +" is added to the list l2")
logging.info("The resultant list of integers is {l1} and the resultant list for string is {l2}".format(l1 = l1, l2 = l2))
        