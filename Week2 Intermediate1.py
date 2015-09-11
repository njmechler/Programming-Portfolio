def balancedString(parentheses):
    left_par = []
    right_par = []
    left_bracket = []
    right_bracket = []
    left_brace = []
    right_brace = []
    for character in parentheses:
        if (character == "("):
            left_par.append(character)
        elif (character == ")"):
            right_par.append(character)
        elif (character == "["):
            left_bracket.append("[")
        elif (character == "]"):
            right_bracket.append("]")
        elif (character == "{"):
            left_brace.append(character)
        elif (character == "}"):
            right_brace.append(character)
        else:
            return ("String contains invalid characters.")
            break
    if ((len(left_par) == len(right_par)) & (len(left_bracket) == len(right_bracket)) & (len(left_brace) == len(right_brace))):
        return True
    else:
        return False

print (balancedString("((){})"))
