import re
global err_msg
import sys 
log = []
import datetime
import os
now = datetime.datetime.now()
def Valid_password_mixed_case(password):
    letters = set(password)
    global log
    mixed = any(letter.islower() for letter in letters) and any(letter.isupper() for letter in letters)
    return mixed

def unUsed_variables (lines):
    line_count = 0
    repet = 0
    global log
    for x_line in lines:
        line_count = line_count + 1
        repet = 0
        line_array = re.split(r'\s',x_line)
        if (line_array[0] == "local") and (line_array[1] != "function"):
            for line in lines:
                if line.find(line_array[1].strip(',')) != -1:
                    repet = repet + 1
            if repet == 1 :
              log.append("Line Number[ERROR]"+str(line_count)+": The Variable '"+line_array[1]+"' Not Used anywhere.")
      
def variable_check(line):
   global err_msg
   global log
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
    global log
    err_msg= "This line contain's more than 250 Character try to split for readablity"
    return len(x) < 250
    
def check_extraline(x , lines , num):
    global err_msg
    global log
    nextLine = "no-line"
    if len(lines)-1 > num:
        nextLine = lines[num+1].strip()
    if (x.strip() == "") and (nextLine == ""):
        err_msg = "Please remove this Extra Line."
        return False
    else:
        return True

def check_extraspace(x):
    global err_msg
    global log
    if ("=" in x):
        if (re.search(r"\s\=\s" , x) == None and re.search(r"\s\===\s" , x) == None and re.search(r"\s\<=\s" , x) == None and re.search(r"\s\>=\s" , x) == None and re.search(r"\s\~=\s" , x) == None and re.search(r"\s\!=\s" , x) == None and re.search(r"\s\==\s",x) == None and  ("$" not in x) and ("div" not in x) and ("%="  not in x) and ("img" not in x) and ("form" not in x) and ("span" not in x) and ("<p" not in x) and ("hr" not in x) and ("script" not in x) and  ("get" not in x) and ("post" not in x) and  ("option" not in x) and ("id" not in x) and ("value" not in x) and ("h1" not in x)):
            err_msg = "Please leave space before and after for '=' or '==' or '~=' or '!='"
            return False
            
def check_StringBoolean(x):
    global log
    global err_msg
    if (re.search(r'"true"',x) != None or re.search(r'"false"',x) != None) and  ("$" not in x ) and ("<" not in x ) and (">" not in x):
        err_msg = "Don't use Boolean as String"
        return False

def check_nil(line , num):
    global log
    global err_msg
    line_split = re.split(r'\s',line.strip())
    if (re.search(r"\s\if\s",line) != None and re.search(r"\sthen\s",line) != None):
        err_msg = "CONDITION CHECK found check if any nil check needed(leave this if not applicable)"
        return False
        
def commaCheck(lines):
    global log
    log.append("================== COMMA CHECK FOR TABLE ===================")
    end_check = True
    num_count = 0
    count_last = 0
    f =  open(sys.argv[1], "r").readlines()
    while num_count < len(lines):
        end_check = True
        split_line = re.split(r'\s',lines[num_count].strip())
        if(split_line[0] == "local" and split_line[len(split_line)-1] == "{"):
            num_check = num_count +1
            while end_check:
                if("}" == lines[num_check].strip(",").strip()):
                    end_check = False
                    if(lines[num_check-1].strip().endswith(',')):
                        count_last = count_last + 1 
                        log.append("Line Number[ERROR]: " +str(num_check) + "  Please remove comma ','for last value")
                elif(not lines[num_check].strip().endswith(',')) and ("}" not in  lines[num_check+1].strip(",").strip()) and ("{" not in  lines[num_check].strip()) and  (end_check):
                    count_last = count_last+1
                    log.append("Line Number[ERROR]: " +str(num_check+1) + "  Please put comma ',' in end of line")
                num_check = num_check +1
        num_count = num_count + 1
    if count_last != 0:
        log.append("====================== ERROR ===================================")
    else:
        log.append("NO ERROR")
        log.append("====================== SUCCESS ===================================")
    log.append('\n')
        
def  code_repetation(lines):
    global log
    avoid_rep = []
    log.append("========================== CODE DUPLICATION CHECK =============================")
    counter = 0
    for line in lines:
        counter =  counter + 1
        count_dup = 0
        if  ('--' not in line.strip()) and  ('ul' not in line.strip()) and ('break' not in line.strip()) and ('td>' not in line.strip()) and ('session' not in line.strip()) and ('==' not in line.strip()) and ('++' not in line.strip()) and ('ngx' not in line.strip()) and ('false' not in line.strip()) and ('table' not in line.strip()) and ('tr>' not in line.strip())  and ('return' not in line.strip()) and ('th>' not in line.strip()) and ('span' not in line.strip()) and ('thead' not in line.strip()) and('type' not in line.strip()) and ("true" not in line.strip()) and ("div" not in line.strip()) and ("<br>" not in line.strip()) and ("{" not in line.strip()) and ("}" not in line.strip()) and ("%>" not in line.strip()) and ("<%" not in line.strip()) and ("if" not in line.strip()) and ("else" not in line.strip())and ("return true" not in line.strip()) and ("<div>" not in line.strip()) and (line.strip() != "") and ("<script>" not in line.strip()) and ("</div>" not in line.strip()) and ("<%end%>"  not in line) and ("end" not in line.strip()):
            for _all in lines:
                if (line.strip() == _all.strip()):
                    count_dup = count_dup+1
        if (count_dup>2) and (line.strip() not in avoid_rep):
            avoid_rep.append(line.strip())
            log.append(line.strip())
            log.append("Line Number[IMPROVEMENT] " + str(counter) + " Above line Repeted "+str(count_dup)+ " time's please optimize it if possible")
    log.append("===============================================================================")
    log.append('\n')
def check_function_desp(all_line):
    global log
    count_des_check = 0
    log.append("========================== FUNCTION DESCRIPTION CHECK =============================")
    for l in all_line:
        count_des_check = count_des_check +1
        line_array = re.split(r'\s',l)
        if("local" in line_array[0]) and ("function" in line_array[1]):
            if("--" not in all_line[count_des_check-1]):
                log.append("Line Number[IMPROVEMENT] " +str(count_des_check) +" No Descrption given for this function :"+line_array[2])
    log.append("===============================================================================")
    log.append('\n')
    
def divCount(lines):
    global log
    log.append('\n')
    divOpen = 0
    divClose = 0
    div_line = 0
    for x in lines:
        div_line = div_line + 1
        if(re.search("div" , x) != None) and ("$" not in x):
            divOpen = divOpen + x.count("<div")
            divClose = divClose + x.count("</div")
    log.append("================== DIV CHECK ===================")
    log.append("NO. OF DIV OPENED:  " + str(divOpen))
    log.append("NO. OF DIV ClOSED:  " + str(divClose))
    if (divOpen != divClose):
         log.append("================== ERROR ===================")
    else:
         log.append("================== SUCCESS ===================")
    log.append('\n')
    
def create_new_file():
    line_c = 0
    file_name = "internalReview_comments_"+str(now.day) +":"+str(now.month)+":"+str(now.year)+":"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+".log"
    file = open(file_name, "w")
    curent_time = str(now.day) +":"+str(now.month)+":"+str(now.year)
    file.write("*********************************************************************")
    file.write('\n')
    file.write("* Created User : "+os.uname()[1]+"                                  ")
    file.write('\n')
    file.write("* Created Date : "+curent_time+"                                    ")
    file.write('\n')
    file.write("* File Name    : "+file_name+"                                    ")
    file.write('\n')
    file.write("* serial No    : "+str(len(log))+"                                    ")
    file.write('\n')
    file.write("*********************************************************************")
    file.write('\n')
    for x in log:
        if x != '\n' and "====" not in x:
            line_c = line_c + 1
            num_l = line_c
        else:
            num_l = ""
        file.write(str(num_l)+" "+x)
        file.write('\n')
    file.write("***********************************Thank You*************************************")
    file.close()
    print("File created as: " +file_name)
    
def display_logs():
    for x in log:
        print(x)
    print("***********************************Thank You*************************************")

def check_for_break(b_lines):
    b_count = 0
    flag = True
    log.append("================================= BREAK CHECK =================================")
    for b_l in b_lines:
        b_count = b_count + 1
        line_array = re.split(r'\s',b_l)
        if (("for" in b_l) and ("do" in b_l)):
            for i in range(b_count+1 , len(b_lines)):
                if  "if" in b_lines[i]:
                    log.append("Line Number[IMPROVEMENT]:" + str(i+1) +" Check for 'break' or 'return' inside if to increase the productivity")
                    break
                if "end" in b_lines[i]:
                    break
    log.append("===============================================================================")
                       
def internalReview(file):
    f = open(sys.argv[1], "r")
    lines  =  open(sys.argv[1], "r").readlines()
    count = 0
    log.append("============================== GENERAL COMMENTS ======================================")
    unUsed_variables(lines)
    for x in f:
      if variable_check(x) == False:
        log.append("Line Number[ERROR]: " +str(count+1) + "  "+err_msg)
      if numberOfCharacter(x) == False:
        log.append("Line Number[IMPROVEMENT]: " +str(count+1) + "  "+err_msg)
      if check_extraline(x , lines ,count) == False:
        log.append("Line Number[ERROR]: " +str(count+1) + "  "+err_msg)
      if check_extraspace(x) == False:
        log.append("Line Number[ERROR]: " +str(count+1) + "  "+err_msg)
      if check_StringBoolean(x) == False:
        log.append("Line Number[ERROR]: " +str(count+1) + "  "+err_msg)
      if check_nil(x , count) == False:
        log.append("Line Number[WARNING]: " +str(count+1) + "  "+err_msg)
      count = count + 1
    log.append("===============================================================================")  
    divCount(lines)
    commaCheck(lines)
    code_repetation(lines)
    check_function_desp(lines)
    check_for_break(lines)
#init function
internalReview(sys.argv[1])

user_input= input("Press 1 for save log in File:" +'\n' +"Press 2 for show log here:"+'\n')
if user_input == "1":
    create_new_file()
elif user_input == "2":
    display_logs()
else:
    print("Wrong Input")
    create_new_file()