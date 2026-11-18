full_dot = '●'
empty_dot = '○'

def create_character(name, STR, INT, CHA):
    if type(name) is not str:
        return 'The character name should be a string'
    elif name == '':
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif ' ' in name:
        return 'The character name should not contain spaces'
    elif type(STR) is not int or type(INT) is not int or type(CHA) is not int:
        return 'All stats should be integers'
    elif STR < 1 or INT < 1 or CHA < 1:
        return 'All stats should be no less than 1'
    elif STR > 4 or INT > 4 or CHA > 4:
        return 'All stats should be no more than 4'
    elif STR + INT + CHA != 7:
        return 'The character should start with 7 points'
    else:
        str_line = f"STR {full_dot * STR}{empty_dot * (10 - STR)}"
        int_line = f"INT {full_dot * INT}{empty_dot * (10 - INT)}"
        cha_line = f"CHA {full_dot * CHA}{empty_dot * (10 - CHA)}"
        
        return f"{name}\n{str_line}\n{int_line}\n{cha_line}"
