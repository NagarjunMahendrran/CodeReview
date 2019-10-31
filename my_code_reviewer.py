import re
global err_msg

def Valid_password_mixed_case(password):
    letters = set(password)
    mixed = any(letter.islower() for letter in letters) and any(letter.isupper() for letter in letters)
    return mixed

def unUsed_variables (lines):
    line_count = 0
    repet = 0
    for x_line in lines:
        line_count = line_count + 1
        repet = 0
        line_array = re.split(r'\s',x_line)
        if (line_array[0] == "local") and (line_array[1] != "function"):
            for line in lines:
                if line.find(line_array[1].strip(',')) != -1:
                    repet = repet + 1
            if repet == 1 :
              print("Line Number[ERROR]"+str(line_count)+": The Variable '"+line_array[1]+"' Not Used anywhere.")
      

def variable_check(line):
   global err_msg
   line_array = re.split(r'\s',line)
   if (line_array[0] == "var") or (line_array[0] == "local") and (line_array[1] != "function"):
       if len(line_array[1]) > 8 :
           if Valid_password_mixed_case(line_array[1]) == False and ("_" in line_array[1]) ==  False :
               err_msg = "please use camelCasing or use _ in vaiable names"
               return False
   else:
        return True
        
def numberOfCharacter(x):
    global err_msg
    err_msg= "This line contain's more than 250 Character try to split for readablity"
    return len(x) < 250
    
def check_extraline(x , lines , num):
    global err_msg
    nextLine = ""
    try:
        nextLine = lines[num + 1]
    except IndexError:
        pass
    if(len(x.strip()) == 0 and len(nextLine.strip()) == 0):
        err_msg = "Please remove this Extra Line."
        return False
    else:
        return True

def check_extraspace(x , count):
    global err_msg
    if ("=" in x):
        if (re.search(r"\s\=\s" , x) == None and re.search(r"\s\<=\s" , x) == None and re.search(r"\s\>=\s" , x) == None and re.search(r"\s\~=\s" , x) == None and re.search(r"\s\!=\s" , x) == None and re.search(r"\s\==\s",x) == None and ("div" not in x) and ("%="  not in x) and ("img" not in x) and ("form" not in x) and ("span" not in x) and ("<p" not in x) and ("hr" not in x) and ("script" not in x) and  ("get" not in x) and ("post" not in x) and ("option" not in x) and ("id" not in x) and ("value" not in x) and ("h1" not in x)):
            err_msg = "Please leave space before and after for '=' or '==' or '~=' or '!='"
            return False
def check_StringBoolean(x):
    global err_msg
    if (re.search(r'"true"',x) != None or re.search(r'"false"',x) != None):
        err_msg = "Don't use Boolean as String"
        return False

def check_nil(line , num):
    global err_msg
    line_split = re.split(r'\s',line.strip())
    if (re.search(r"\s\if\s",line) != None and re.search(r"\sthen\s",line) != None):
        err_msg = "CONDITION CHECK found check if any nil check needed(leave this if not applicable)"
        return False
def divCount(lines):
    divOpen = 0
    divClose = 0
    div_line = 0
    for x in lines:
        div_line = div_line + 1
        if(re.search("div" , x) != None) and ("$" not in x):
            print(x)
            divOpen = divOpen + x.count("<div")
            divClose = divClose + x.count("</div")
    print('\n')
    if (divOpen != divClose):
         print("================== ERROR ===================")
    else:
         print("================== SUCCESS ===================")
    print("NO. OF DIV OPENED:  " + str(divOpen))
    print("NO. OF DIV ClOSED:  " + str(divClose))
    
    
def internalReview():
    f = open("arjun.txt", "r")
    lines  =  open("arjun.txt", "r").readlines()
    count = 0
    unUsed_variables(lines)
    for x in f:
      count = count + 1
      if variable_check(x) == False:
        print("Line Number[ERROR]: " +str(count) + "  "+err_msg)
      if numberOfCharacter(x) == False:
        print("Line Number[WARNING]: " +str(count) + "  "+err_msg)
      if check_extraline(x , lines ,count) == False:
        print("Line Number[ERROR]: " +str(count) + "  "+err_msg)
      if check_extraspace(x , count) == False:
        print("Line Number[ERROR]: " +str(count) + "  "+err_msg)
      if check_StringBoolean(x) == False:
        print("Line Number[ERROR]: " +str(count) + "  "+err_msg)
      if check_nil(x , count) == False:
        print("Line Number[WARNING]: " +str(count) + "  "+err_msg)
    divCount(lines)
internalReview()