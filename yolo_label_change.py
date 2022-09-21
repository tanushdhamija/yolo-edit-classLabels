import os

curr_dir = os.getcwd()

#if not os.path.exists('./dataset'):
    #os.makedirs('./dataset')

os.chdir(os.path.join(curr_dir, 'dataset'))
annotations = [] 

for file in sorted(os.listdir(os.getcwd())):

    # grab only the .txt files to modify
    if file.endswith('.txt') and file != 'classes.txt':
        annotations.append(file)

#print(len(annotations))

for anno in annotations:

    new_lines = []

    # read all lines of the .txt file
    with open(anno, 'r') as file:
        lines = file.readlines()
    
    #print(lines)

    # modify the lines accordingly
    for line in lines:

        line_list = list(line)
        
        # edit the required logic here
        if line_list[0] == '0':
            line_list[0] = '80'
        if line_list[0] == '1':
            line_list[0] = '81'

        line = ''.join(line_list)
        new_lines.append(line)
        #print(line)
    
    # write back modified lines to the file
    with open(anno, 'w') as file:
        file.writelines(new_lines)
        

os.chdir(curr_dir)
print('Finished!')