import re
import json

def get_space_end(level):
    return '  ' * level + '-'

def get_space_expand(level):
    return '  ' * level + '+'

def make_it_clear(targets, level, file):
    keys = iter(targets)
    for each in keys:
        if type(targets[each]) is not dict:
            file.write(get_space_end(level) + str(each) + ' : ' + str(targets[each]) + '\n')
        else:
            next_level = level+1
            file.write(get_space_expand(level) + each + '\n')
            make_it_clear(targets[each], next_level, file)

def main():
    with open("g_page_config.txt", "r", encoding="utf-8") as file1:
        g_page_config = json.loads(file1.read())
        with open("make_it_cleat.txt", "w", encoding="utf-8") as file2:
            make_it_clear(g_page_config, 1, file2)
    
if __name__ == "__main__":
    main()
