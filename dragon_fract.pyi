import turtle
axiom = "b"
axmTemp = ""
itr = 8  # итераций 
dl = 3   # длина черты

turtle.hideturtle()
turtle.penup()
turtle.setpos(-400,-300) # начальная позиция
turtle.pendown()
turtle.tracer(0)

# код переделан,
# если символ переходит в новую строку без изменений,
# то его не обязательно вносить в правила
translate={ "a" : "b-a-b"  , 
            "b" : "a+b+a"  }

for k in range(itr):
    for ch in axiom:
			if ch in translate:
				axmTemp += translate[ch]
			else:
				axmTemp += ch
    axiom = axmTemp
    axmTemp = ""
    
for ch in axiom:
    if ch == "+":       #+
        turtle.right(60)
    elif ch == "-":     #-
        turtle.left(60)
    else:               # a b
        turtle.forward(dl)
        
turtle.update()        
#turtle.mainloop()
