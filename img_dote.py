import sys
from random import *
import pygame
import time
from collections import deque
from math import *
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN,Rect,MOUSEBUTTONDOWN,K_SPACE
pygame.init()
FPSCLOCK = pygame.time.Clock()
size=(985,1000)
SURFACE = pygame.display.set_mode(size)

Dote={
      "background":[
         [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      ],

      "I":[[
            [0,0,0,0],
            [1,1,1,1],
            [0,0,0,0],
            [0,0,0,0]
         ],[
            [0,0,1,0],
            [0,0,1,0],
            [0,0,1,0],
            [0,0,1,0]
         ],[
            [0,0,0,0],
            [0,0,0,0],
            [1,1,1,1],
            [0,0,0,0]
         ],[
            [0,1,0,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,1,0,0]
         ],
      ],

      "J":[[
            [1,0,0,0],
            [1,1,1,0],
            [0,0,0,0],
            [0,0,0,0]
         ],[
            [0,1,1,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,0,0,0]
         ],[
            [0,0,0,0],
            [1,1,1,0],
            [0,0,1,0],
            [0,0,0,0]
         ],[
            [0,1,0,0],
            [0,1,0,0],
            [1,1,0,0],
            [0,0,0,0]
         ],
      ],

      "L":[[
            [0,0,1,0],
            [1,1,1,0],
            [0,0,0,0],
            [0,0,0,0]
         ],[
            [0,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,0,0]
         ],[
            [0,0,0,0],
            [1,1,1,0],
            [1,0,0,0],
            [0,0,0,0]
         ],[
            [1,1,0,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,0,0,0]
         ],
      ],

      "O":[[
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0],
            [0,0,0,0]
         ],[
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0],
            [0,0,0,0]
         ],[
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0],
            [0,0,0,0]
         ],[
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0],
            [0,0,0,0]
         ],
      ],

      "S":[[
            [0,1,1,0],
            [1,1,0,0],
            [0,0,0,0],
            [0,0,0,0]
         ],[
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,0,0]
         ],[
            [0,0,0,0],
            [0,1,1,0],
            [1,1,0,0],
            [0,0,0,0]
         ],[
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,0,0,0]
         ],
      ],
    
      "T":[[
            [0,1,0,0],
            [1,1,1,0],
            [0,0,0,0],
            [0,0,0,0]
         ],[
            [0,1,0,0],
            [0,1,1,0],
            [0,1,0,0],
            [0,0,0,0]
         ],[
            [0,0,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [0,0,0,0]
         ],[
            [0,1,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,0,0,0]
         ],
      ],

      "Z":[[
            [1,1,0,0],
            [0,1,1,0],
            [0,0,0,0],
            [0,0,0,0]
         ],[
            [0,0,1,0],
            [0,1,1,0],
            [0,1,0,0],
            [0,0,0,0]
         ],[
            [0,0,0,0],
            [1,1,0,0],
            [0,1,1,0],
            [0,0,0,0]
         ],[
            [0,1,0,0],
            [1,1,0,0],
            [1,0,0,0],
            [0,0,0,0]
         ],
      ],

      "blank":[
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
      ]

}

def dote(name):
    return Dote[name]