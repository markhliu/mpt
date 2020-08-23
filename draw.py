#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle as t 

t.Screen() 
t.setup(600,500,100,200) 
t.bgcolor('light green') 
t.title('Python Turtle Graphics') 
t.pensize(1) 
t.shape('turtle')
t.up() 
t.pencolor('red') 
for x in range(0,200,5): 
  print("X:{}",x) 
  for i in range(50): 
    t.goto(-200+5*i,-150+x) 
    t.down() 
    t.goto(-200+5*i+3,-150+x) 
    t.up() 
    print("i:{}",i) 
t.hideturtle() 
t.goto(x=5,y=10) 
t.done() 
try: 
    t.bye() 
except t.Terminator: 
    pass 
