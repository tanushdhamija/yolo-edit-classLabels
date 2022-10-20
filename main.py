import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str, required=True, 
                    help='Path to save the data on your system')
parser.add_argument('-s', '--search', type=str, required=True,
                    help='The label to be modified')
parser.add_argument('-r', '--replace', type=str, required=True,
                    help='The label to replace with')
args = vars(parser.parse_args())


curr_dir = os.getcwd()
os.chdir(args['path'])

# collect all annotations from the directory
annotations = []
for file in sorted(os.listdir(os.getcwd())):

    # grab only the .txt files to modify
    if file.endswith('.txt') and file != 'classes.txt':
        annotations.append(file)

if len(annotations) == 0:
    sys.exit("No annotation files found.")

def modify_label(search_label=args['search'], replace_label=args['replace']):

    for anno in annotations:
    
        new_lines = []

        # read all lines of the .txt file
        with open(anno, 'r') as file:
            lines = file.readlines()
        
        # modify the class labels
        for line in lines:

            found = False

            for i, char in enumerate(line):
                
                if char == ' ' and line[:i] == search_label:
                    new_line = replace_label + ' ' + line[i+1:]
                    found = True
                    break
            
            if not found:
                new_line = line

            new_lines.append(new_line)
                    
        # write back to the file
        with open(anno, 'w') as file:
            file.writelines(new_lines)
    
    print('Done!')
    os.chdir(curr_dir)


if __name__ == '__main__':
    modify_label()