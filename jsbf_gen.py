START="_=[+[]+[]][+[]]+[];__=[{_:[]}][+[]]+[];__=__[[++[++[++[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]+__[[++[++[++[++[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]+__[[[++[+[]][+[]]][+[]]+[]]+[[+[]][+[]]+[]]]+__[[[++[+[]][+[]]][+[]]+[]]+[[++[+[]][+[]]][+[]]+[]]]+__[[[++[+[]][+[]]][+[]]+[]]+[[++[++[+[]][+[]]][+[]]][+[]]+[]]]+__[[[++[+[]][+[]]][+[]]+[]]+[[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]+[]]];"
ALPHABET = {
    "a": "[[[][[]]--][+[]]+[]][+[]][[++[+[]][+[]]][+[]]+[]]",
    "b": "[[{_:[]}][+[]]+[]][+[]][[++[++[+[]][+[]]][+[]]][+[]]+[]]",
    "c": "[eval(__)+[]][+[]][[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]+[]]",
    "d": "[[][[]]+[]][+[]][[++[++[+[]][+[]]][+[]]][+[]]+[]]",
    "e": "[[][[]]+[]][+[]][[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]+[]]",
    "f": "[eval(__)+[]][+[]][[+[]][+[]]+[]]",
    "g": "eval([[{_:[]}][+[]]+[]][+[]][[++[++[+[]][+[]]][+[]]][+[]]+[]]+[[-[++[+[]][+[]]/+[]][+[]]][+[]]+[]][+[]][[++[++[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]+[[{_:[]}][+[]]+[]][+[]][[++[+[]][+[]]][+[]]+[]]+[[[][[]]--][+[]]+[]][+[]][[++[+[]][+[]]][+[]]+[]]+[[eval(__)+[]][+[]][[[++[+[]][+[]]][+[]]+[]]+[[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]]][+[]]+[++[++[+[]][+[]]][+[]]][+[]]+[]+[[eval(__)+[]][+[]][[[++[+[]][+[]]][+[]]+[]]+[[++[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]]][+[]])[[++[+[]][+[]]][+[]]+[]]",
    "i": "[[][[]]+[]][+[]][[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]",
    "l": "[[[+[]][+[]]+[]==[[][[]]+[]][+[]]][+[]]+[]][+[]][[++[++[+[]][+[]]][+[]]][+[]]+[]]",
    "n": "[[][[]]+[]][+[]][[++[+[]][+[]]][+[]]+[]]",
    "o": "[[{_:[]}][+[]]+[]][+[]][[++[+[]][+[]]][+[]]+[]]",
    "r": "[[[+[]][+[]]+[]==[+[]][+[]]+[]][+[]]+[]][+[]][[++[+[]][+[]]][+[]]+[]]",
    "s": "[[[+[]][+[]]+[]==[[][[]]+[]][+[]]][+[]]+[]][+[]][[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]+[]]",
    "t": "[[-[++[+[]][+[]]/+[]][+[]]][+[]]+[]][+[]][[++[++[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]",
    "u": "[[][[]]+[]][+[]][[+[]][+[]]+[]]",
    "v": "[eval(__)+[]][+[]][[[++[++[+[]][+[]]][+[]]][+[]]+[]]+[[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]]",
    "y": "[[-[++[+[]][+[]]/+[]][+[]]][+[]]+[]][+[]][[++[++[++[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]",
    "I": "[[-[++[+[]][+[]]/+[]][+[]]][+[]]+[]][+[]][[++[+[]][+[]]][+[]]+[]]",
    "N": "[[[][[]]--][+[]]+[]][+[]][[++[++[+[]][+[]]][+[]]][+[]]+[]]",
    "O": "[[{_:[]}][+[]]+[]][+[]][[++[++[++[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]",
    "-": "[[-[++[+[]][+[]]/+[]][+[]]][+[]]+[]][+[]][[+[]][+[]]+[]]",
    "[": "[[{_:[]}][+[]]+[]][+[]][[+[]][+[]]+[]]",
    "]": "[[{_:[]}][+[]]+[]][+[]][[[++[+[]][+[]]][+[]]+[]]+[[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]]",
    "(": "[[eval(__)+[]][+[]][[[++[+[]][+[]]][+[]]+[]]+[[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]]][+[]]",
    ")": "[[eval(__)+[]][+[]][[[++[+[]][+[]]][+[]]+[]]+[[++[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]]][+[]]",
    "{": "[[eval(__)+[]][+[]][[[++[+[]][+[]]][+[]]+[]]+[[++[++[++[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]]][+[]]",
    "}": "[[eval(__)+[]][+[]][[[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]+[]]+[[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]+[]]]][+[]]",
    "0": "[+[]][+[]]+[]",
    "1": "[++[+[]][+[]]][+[]]+[]",
    "2": "[++[++[+[]][+[]]][+[]]][+[]]+[]",
    "3": "[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]+[]",
    "4": "[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]+[]",
    "5": "[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]",
    "6": "[++[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]",
    "7": "[++[++[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]",
    "8": "[++[++[++[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]",
    "9": "[++[++[++[++[++[++[++[++[++[+[]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]][+[]]+[]"
}

CODE = 'console.log("start");console.log("----------");for($_=0;$_<10;++$_){console.log("count",$_);};console.log("----------");console.log("end");'

def replace(js_code):
    result = START + ';' + "eval("
    for character in js_code:
        try:
            result += ALPHABET[character] + "+"
        except:
            if character == '"':
                result += '"\\' + character + '"+'
            else:
                result += '"' + character + '"+'

    result = result[:-1] + ")"
    return result

if __name__ == '__main__':
    print replace(CODE)
    
    
