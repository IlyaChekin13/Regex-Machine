"""ALL COMMENTED PRINTS FOR DEBUGGING"""
import sys
sys.setrecursionlimit(2000)
my_inp = str(input()).split("|")


def single_comp(regex, string_):
    """returns True if string character matches regex character"""
    if regex == "":
        return True
    elif regex == string_:
        return True
    elif regex == "." and string_ != "":
        return True
    else:
        return False


def compare(regex, string, regex_opt, string_opt):
    #print(regex, string)
    """returns True if string matches regex pattern,
     for input string equal or shorter than regex string"""
    if regex != "":
        if string != "" or regex[0] == "$" or regex.find("?") != -1 or regex.find("*") != -1 or regex.find("+") != -1:
            if regex[0] == "$" and string == "" and regex_opt[-len(regex) - 1] != "\\":
                #print(1)
                return True
            elif regex[0] == "\\":
                #print(2)
                return compare(regex[1:], string, regex_opt, string_opt)
            elif regex[0] == "+" and regex_opt[-len(regex) - 1] != "\\":
                #print(3)
                return compare(regex[1:], string, regex_opt, string_opt)
            elif regex[0] == "*" and regex_opt[-len(regex) - 1] != "\\":
                #print(4)
                return compare(regex[1:], string, regex_opt, string_opt)
            elif regex.find("*") != -1 and not single_comp(regex[0], string[0]):
                #print(5)
                if regex[1] == "*" and regex_opt[-len(regex) - 1] != "\\":
                    #print(5.5)
                    return compare(regex[2:], string, regex_opt, string_opt)
            elif regex.find("+") != -1 and single_comp(regex[0], string[0]):
                #print(6)
                if regex[1] == "+":
                    i = 0
                    #print(6.5)
                    while single_comp(regex[0], string[i]):
                        i += 1
                        if regex[-1] == "$":
                            return compare(regex[1:], string[-len(regex[1:-2]):], regex_opt, string_opt)
                        if i == len(string):
                            break
                    return compare(regex[1:], string[i:], regex_opt, string_opt)
                else:
                    #print("6.5.5")
                    return compare(regex[1:], string[1:], regex_opt, string_opt)
            elif regex.find("*") != -1 and single_comp(regex[0], string[0]):
                #print(7)
                if regex[1] == "*":
                    i = 0
                    #print(7.5)
                    while single_comp(regex[0], string[i]):
                        i += 1
                        if regex[-1] == "$":
                            return compare(regex[1:], string[-len(regex[1:-2]):], regex_opt, string_opt)
                        if i == len(string):
                            break
                    return compare(regex[1:], string[i:], regex_opt, string_opt)
                else:
                    #print("7.5.5")
                    return compare(regex[1:], string[1:], regex_opt, string_opt)
            elif regex[0] == "?" and regex_opt[-len(regex) - 1] != "\\":
                #print(8)
                return compare(regex[1:], string, regex_opt, string_opt)
            elif regex.find("?") != -1 and not single_comp(regex[0], string[0]) and regex[0] != "?":
                #print(9)
                if regex[1] == "?":
                    #print(9.5)
                    return compare(regex[2:], string, regex_opt, string_opt)
            elif single_comp(regex[0], string[0]):
                #print(10)
                return compare(regex[1:], string[1:], regex_opt, string_opt)
            else:
                #print(11)
                return False
        else:
            #print(12)
            return False
    else:
        #print(13)
        return True


def full_compare(regex_x, string_x, regex_x_opt, string_x_opt):
    #print("main")
    """returns True if string or part of it matches regex pattern"""
    if not string_x and regex_x:
        #print("main 1")
        return False
    if compare(regex_x, string_x, regex_x_opt, string_x_opt):
        #print("main 2")
        return True
    elif regex_x[0] == "^":
        #print("main 3")
        return compare(regex_x[1:], string_x, regex_x_opt, string_x_opt)
    elif string_x != "":
        #print("main 4")
        return full_compare(regex_x, string_x[1:], regex_x_opt, string_x_opt)
    else:
        #print("main 5")
        return False


print(full_compare(my_inp[0], my_inp[1], my_inp[0], my_inp[1]))
