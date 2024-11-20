def validate(input_data):
    if input_data.find("def") == -1:
        return "missing def"
    elif input_data.find(":") == -1:
        return "missing :"
    elif input_data.find("(") == -1 or input_data.find(")") == -1:
        return "missing paren"
    if input_data.find("()") != -1:
        if input_data[input_data.find("()") - 2] != "(":
            return "missing param"
    if input_data.find("    ") == -1:
        return "missing indent"
    if input_data.find("validate") == -1:
        return "wrong name"
    if input_data.find("return") == -1:
        return "missing return"
    return True

def main():
    input_data = """def validate(input_data):
    if input_data.find("def") == -1:
        return "missing def"
    elif input_data.find(":") == -1:
        return "missing :"
    elif input_data.find("(") == -1 or input_data.find(")") == -1:
        return "missing paren"
    if input_data.find("()") != -1:
        if input_data[input_data.find("()") - 2] != "(":
            return "missing param"
    if input_data.find("    ") == -1:
        return "missing indent"
    if input_data.find("validate") == -1:
        return "wrong name"
    if input_data.find("return") == -1:
        return "missing return"
    return True"""
    result = validate(input_data)
    print("The code validity check returned: ")
    print(result)

if __name__ == "__main__":
    main()