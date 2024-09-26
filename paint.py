
# was never finished because i moved classes
# thought i would share because i thought it was kinda cool
# objects are used because i didnt read the documentation right
# "It is sometimes necessary to use global values. In that event, you can use either an app or a shape property"
# -- /docs/unavailablePython
# uncompleted Vi type editor. not functional at all but will keep for archival purposes
# mostly just a paint app, but the 'terminal' is kinda cool

# oh gosh i hope this is optimized !
app.stepsPerSecond = 30
# INITIALIZE
app.currentApp = 'desktop'
globalData1 = Label('null',0,0,visible=False) # edit mode, cursorPositionY, cursorPositionX, bold=clr on key

# funny desktop message
message = randrange(0,5)
if (message == 0):
    message = "I miss C"
elif(message == 1):
    message = "Hello, World!"
elif(message == 2):
    message = "read src"
elif(message == 3):
    message = "almost hyprland"
elif(message == 4):
    message = "drink water"
else:
    message = "how did you get here?"
# DESKTOP
desktopBackground = Group(
    Rect(0,0,400,400,fill=gradient(rgb(18,10,16),rgb(18,12,40),start='top')),
    Label(message,5,375,font='orbitron',size=28,fill=rgb(62,60,74),bold=True),
    Rect(-10,50,420,300,fill=None,border=rgb(109,109,109),borderWidth=6)
    )
    # forgot what i was going to put here
desktopBackground.children[1].centerX = (desktopBackground.children[1].width/2)+desktopBackground.children[1].centerX
desktopBackground.visible=False
# possible terminal inside desktop?
linefont = 'monospace'
Lines = Group(
        Label('Hello',5, 70,size=18,fill='white',font=linefont,bold=True),
        Label('Hello',5, 90,size=18,fill='white',font=linefont,bold=True),
        Label('Hello',5,110,size=18,fill='white',font=linefont,bold=True),
        Label('Hello',5,130,size=18,fill='white',font=linefont,bold=True),
        Label('Hello',5,150,size=18,fill='white',font=linefont,bold=True),
        Label('Hello',5,170,size=18,fill='white',font=linefont,bold=True),
        Label('Hello',5,190,size=18,fill='white',font=linefont,bold=True),
        Label('Hello',5,210,size=18,fill='white',font=linefont,bold=True),
        Label('Hello',5,230,size=18,fill='white',font=linefont,bold=True),
        Label('Hello',5,250,size=18,fill='white',font=linefont,bold=True),
        Label('Hello',5,270,size=18,fill='white',font=linefont,bold=True),
        Label('Hello',5,290,size=18,fill='white',font=linefont,bold=True),
        Label('Hello',5,310,size=18,fill='white',font=linefont,bold=True),
        Label('Hello',5,330,size=18,fill='white',font=linefont,bold=True) # 13 lines
    )
cursor = Rect(0,0,11,18,fill='white')
Lines.visible = False
# END DESKTOP
# PAINT
bg = Rect (0,0,400,400,fill='grey',visible=False) # background
workspace = Rect (50,75,300,300,fill='white',visible=False) # workspace/canvas
toolbox = Rect (0,0,400,50,fill='dimGrey',visible=False) # tools
brushIcon = Group (Rect(10,10,30,30,fill='brown'),Label('!',25,25,font='monospace',size=35,rotateAngle=45)) # no nerd font :'(
eraserIcon = Group (Rect(50,10,30,30,fill='pink'),Label('!',65,25,font='symbols',size=35,rotateAngle=45))
brushIcon.visible = False
eraserIcon.visible = False
color1 = Rect (90,10,30,30,visible=False)
color2 = Rect (125,10,30,30,fill='hotPink',visible=False)
color3 = Rect (160,10,30,30,fill='red',visible=False)
color4 = Rect (195,10,30,30,fill='blue',visible=False)
color5 = Rect (230,10,30,30,fill='green',visible=False)
color6 = Rect (265,10,30,30,fill='grey',visible=False)
color7 = Rect (300,10,30,30,fill='yellow',visible=False)
color8 = Rect (335,10,30,30,fill='springGreen',visible=False)
app.value = 'brush'
canvas = Group()
cellSize = 15
cwf = makeList(workspace.width//cellSize,workspace.height//cellSize) # Current Working File
currentColor = Label('black',0,0,visible=False)
cellX = workspace.width//cellSize
cellY = workspace.height//cellSize
saved = Label("Saved",200,75,fill=gradient('purple','midnightBlue',start='right'),size=50,visible=False)
# END PAINT
# EDIT
cwt = makeList(50,1,'')
help = makeList(50,1,'')
if (True):
    help[0][0]  = "Use HJKL to move cursor.        K   "
    help[1][0]  = "Combine with a number         H   L "
    help[2][0]  = "to move n<dir>                  J   "
    help[3][0]  = " Key | Sub | Description            "
    help[4][0]  = "-----+-----+------------------------"
    help[5][0]  = "  :  |     | Enter command mode     "
    help[6][0]  = "  g  |<num>| Cursor to <num>        "
    help[7][0]  = "  i  |     | Insert mode at cursor  "
    help[8][0]  = "  a  |     | Insert mode at cursor+1"
    help[9][0]  = "  A  |     | Insert mode at endl    "
    help[10][0] = "  d  |  d  | Cut line               "
    help[11][0] = "  d  |  $  | Cut from cursor to endl"
    help[12][0] = "  v  |     | Enter visual mode      "
    help[13][0] = "  g  |  G  | Cursor to EOF          "
    help[14][0] = ""
    help[15][0] = ""
    help[16][0] = ""
# END EDIT
def onMousePress(mouseX, mouseY): # drag does not pick up a click without movement
    saved.visible = False
    if (app.currentApp == 'paint'):
        if (workspace.contains(mouseX,mouseY)):
            gX = ((mouseX - workspace.left)//cellSize)
            gY = ((mouseY - workspace.top)//cellSize)
            x = ((mouseX - workspace.left)//cellSize) * cellSize + workspace.left
            y = ((mouseY - workspace.top)//cellSize) * cellSize + workspace.top
            if (app.value == "brush"):
                for child in canvas.children:
                    if (child.left == x and child.top == y):
                        canvas.remove(child)
                        break
                cwf[gX][gY] = getColorInt(currentColor.value)
                canvas.add(Rect(x,y,cellSize,cellSize,fill=currentColor.value))
            elif (app.value == "erase"):
                for child in canvas.children:
                    if (child.left == x and child.top == y):
                        canvas.remove(child)
                        cwf[gX][gY] = 0
                        break
        elif (brushIcon.children[0].contains(mouseX,mouseY)):
            eraserIcon.children[0].borderWidth = 0
            brushIcon.children[0].border = 'white'
            brushIcon.children[0].borderWidth = 2
            app.value = "brush"
        elif (eraserIcon.children[0].contains(mouseX,mouseY)):
            brushIcon.children[0].borderWidth = 0
            eraserIcon.children[0].border = 'white'
            eraserIcon.children[0].borderWidth = 2
            app.value = 'erase'
        elif (color1.contains(mouseX,mouseY)):
            currentColor.value = color1.fill
        elif (color2.contains(mouseX,mouseY)):
            currentColor.value = color2.fill
        elif (color3.contains(mouseX,mouseY)):
            currentColor.value = color3.fill
        elif (color4.contains(mouseX,mouseY)):
            currentColor.value = color4.fill
        elif (color5.contains(mouseX,mouseY)):
            currentColor.value = color5.fill
        elif (color6.contains(mouseX,mouseY)):
            currentColor.value = color6.fill
        elif (color7.contains(mouseX,mouseY)):
            currentColor.value = color7.fill
        elif (color8.contains(mouseX,mouseY)):
            currentColor.value = color8.fill
def onMouseDrag(mouseX, mouseY):
    if (app.currentApp == 'paint'):
        if (workspace.contains(mouseX,mouseY)):
            gX = ((mouseX - workspace.left)//cellSize)
            gY = ((mouseY - workspace.top)//cellSize)
            x = ((mouseX - workspace.left)//cellSize) * cellSize + workspace.left
            y = ((mouseY - workspace.top)//cellSize) * cellSize + workspace.top
            if (app.value == "brush"):
                for child in canvas.children:
                    if (child.left == x and child.top == y):
                        canvas.remove(child)
                        break
                cwf[gX][gY] = getColorInt(currentColor.value)
                canvas.add(Rect(x,y,cellSize,cellSize,fill=currentColor.value))
            elif (app.value == "erase"):
                for child in canvas.children:
                    if (child.left == x and child.top == y):
                        cwf[gX][gY] = 0
                        canvas.remove(child)
def getColorInt(color):
    print(color)
    if (color == color1.fill):
        return 1
    elif (color == color2.fill):
        return 2
    elif (color == color3.fill):
        return 3
    elif (color == color4.fill):
        return 4
    elif (color == color5.fill):
        return 5
    elif (color == color6.fill):
        return 6
    elif (color == color7.fill):
        return 7
    elif (color == color8.fill):
        return 8
    else:
        return 0
def openPaint(*file):
    app.value = 'none'
    bg.visible = True
    workspace.visible = True
    toolbox.visible = True
    brushIcon.visible = True
    eraserIcon.visible = True
    color1.visible = True
    color2.visible = True
    color3.visible = True
    color4.visible = True
    color5.visible = True
    color6.visible = True
    color7.visible = True
    color8.visible = True
    canvas.clear()
    for i in range(workspace.height//cellSize):
        for k in range(workspace.width//cellSize):
            cwf[i][k] = 0
    # decode file
    if (file):
        # decode holoy
        for i in range(workspace.height//cellSize):
            for k in range(workspace.width//cellSize):
                color = file[0][i][k] # i dont know how this works, but it works. do not change it
                if (color == 1):
                    canvas.add(Rect(workspace.left + (i*cellSize),workspace.top + (k * cellSize),cellSize,cellSize,fill=color1.fill))
                elif(color == 2):
                    canvas.add(Rect(workspace.left + (i*cellSize),workspace.top + (k * cellSize),cellSize,cellSize,fill=color2.fill))
                elif(color == 3):
                    canvas.add(Rect(workspace.left + (i*cellSize),workspace.top + (k * cellSize),cellSize,cellSize,fill=color3.fill))
                elif(color == 4):
                    canvas.add(Rect(workspace.left + (i*cellSize),workspace.top + (k * cellSize),cellSize,cellSize,fill=color4.fill))
                elif(color == 5):
                    canvas.add(Rect(workspace.left + (i*cellSize),workspace.top + (k * cellSize),cellSize,cellSize,fill=color5.fill))
                elif(color == 6):
                    canvas.add(Rect(workspace.left + (i*cellSize),workspace.top + (k * cellSize),cellSize,cellSize,fill=color6.fill))
                elif(color == 7):
                    canvas.add(Rect(workspace.left + (i*cellSize),workspace.top + (k * cellSize),cellSize,cellSize,fill=color7.fill))
                elif(color == 8):
                    canvas.add(Rect(workspace.left + (i*cellSize),workspace.top + (k * cellSize),cellSize,cellSize,fill=color8.fill))
                elif(color == 0):
                    pass
                else:
                    print("Corrupt file!")
                cwf[i][k] = file[0][i][k]
def edit():
    updateLines("deleting",0,'clr')
    updateLines("____________________________________",13,None)
    updateLines("run :help to open help page",14,None)
def editEvent(key):
    if (globalData1.value == 'null'):
        if (key == ':' and globalData1.value != 'command'):
            globalData1.value = 'command'
            globalData1.centerX = 14
            updateLines(key, 14, None)
        pass
    elif (globalData1.value == 'insert'):
        pass
    elif (globalData1.value == 'command'):
        updateLines(key, 14, 'add')
        pass
    pass
def updateEdit(dy, cmd):
    pass
def clean():
    # rm paint
    color1.visible=False
    color2.visible=False
    color3.visible=False
    color4.visible=False
    color5.visible=False
    color6.visible=False
    color7.visible=False
    color8.visible=False
    eraserIcon.visible=False
    brushIcon.visible=False
    bg.visible=False
    workspace.visible=False
    toolbox.visible=False
    canvas.clear()
    # rm desktop
    desktopBackground.visible=False
    updateLines("deleting",0,'clr')
    Lines.visible=False
def loadDesktop():
    globalData1.centerX = 1
    Lines.visible=True
    desktopBackground.visible=True
    updateLines("deleting",0,'clr')
def updateLines(str, line, special):
    cY = 0
    if (str == 'space'):
        str = ' '
    elif (str == 'backspace'):
        if (globalData1.value == 'command' and Lines.children[line-1].value == ':'):
            globalData1.value = 'null'
        str = ''
        Lines.children[line-1].value = Lines.children[line-1].value[:-1]
    elif (str == 'enter'):
        if (Lines.children[line-1].value != '' and app.currentApp == 'desktop'):
            runcommand(Lines.children[line-1].value)
            globalData1.centerX += 1
            line += 1
        elif (Lines.children[line-1].value != ''):
            if (app.currentApp == 'edit'):
                if (Lines.children[line-1].value == ':help'):
                    globalData1.value = 'null'
                    updateLines("",14,None)
                    # open help[50][1]
        str = ''
    elif (str == 'tab'):
        str = '    '
    elif (str == 'left'):
        globalData1.centerY -= 1
        str = ''
    elif (str == 'right'):
        globalData1.centerY += 1
        str = ''
    elif (str == 'up'):
        cY -= 1
        str = ''
    elif (str == 'down'):
        cY += 1
        str = ''
    if (special == 'clr'):
        for xline in Lines.children:
            xline.value = ''
        globalData1.centerX = 1
    elif (special == 'add'):
        Lines.children[line-1].value = Lines.children[line-1].value + str
    else:
        Lines.children[line-1].value = str
    for xline in Lines.children:
        xline.left = 5
    print(cY)
    y = line-(1+cY)
    cursor.centerX = cursor.width/2 + Lines.children[line-1].right+2
    cursor.centerY = Lines.children[y].centerY
def runcommand(cmd):
    globalData1.centerX+=1
    if (cmd == 'help'):
        updateLines('deleting',0,'clr')
        updateLines("Desktop help page.",1,None)
        updateLines("------------------------------------ ",2,None)
        updateLines("Command        Description",3,None)
        updateLines("paint <file?>  open paint",4,None)
        updateLines("edit           open text editor",5,None)
        updateLines("help           display this page",6,None)
        updateLines("info           echo some information",7,None)
        updateLines("------------------------------------",8,None)
        updateLines("Shortcut       Description",9,None)
        updateLines("SHIFT + `      Open desktop",10,None)
        updateLines("SHIFT + S      Save to file",11,None)
        globalData1.centerX = 12
        globalData1.bold = True
    elif (cmd == 'info'):
        updateLines('deleting',0,'clr')
        updateLines("This is my first python project.",1,None)
        updateLines("I hope you enjoy.",2,None)
        updateLines("Everything by me.",3,None)
        globalData1.bold = True
    elif (cmd.split(' ')[0] == 'paint'):
        app.currentApp = 'paint'
        if ( len(cmd.split(' ')) > 1):
            if (cmd.split(' ')[1] == 'file'):
                openPaint(file)
            else:
                updateLines("> Invalid file",globalData1.centerX,None)
                app.currentApp = 'desktop'
        else:
            openPaint()
    elif (cmd.split(' ')[0] == 'edit'):
        app.currentApp = 'edit'
        if ( len(cmd.split(' ')) > 1):
            edit(cmd.split(' ')[1])
        else:
            edit()
    else:
        if (globalData1.centerX == 10):
            updateLines("deleting",0,'clr')
        updateLines("> Invalid command",globalData1.centerX,None)
        globalData1.centerX += 1
        updateLines("> Enter 'help' for help",globalData1.centerX,None)
def savePicture():
    for i in range(workspace.width//cellSize):
        for k in range(workspace.height//cellSize):
            file[i][k] = cwf[i][k]
    saved.visible = True
def onKeyPress(key, mod):
    saved.visible = False
    if (key == '~' and mod[0] == "shift"):
        app.currentApp = 'desktop'
        clean()
        loadDesktop()
    elif (app.currentApp == 'desktop'):
        if (globalData1.bold == True):
            updateLines('deleting',0,'clr')
            globalData1.bold = False
        updateLines(key,globalData1.centerX,'add')
    elif (app.currentApp == 'paint'):
        if (key == 'S' and mod[0] == "shift"):
            savePicture()
    elif (app.currentApp == 'edit'):
        editEvent(key)
file = makeList(workspace.width//cellSize,workspace.height//cellSize) # god i love embedded
for i in range(workspace.height//cellSize):
    for k in range(workspace.height//cellSize):
        file[i][k] = randrange(0,9)
loadDesktop()
                
                
                
                
                
                
                
            
                
            
