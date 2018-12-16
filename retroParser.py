id = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
const=range(101)
line_num=range(1001)
command = ['IF','GOTO','PRINT','STOP']
op = ['+','-','<','=']

def scanner(file):
    token_list = []
    for line in file:
        if line[:-1].split(' ')!=['']:
            token_list.append(line.strip(' ').replace('\n','').split(' '))
    for i in token_list:
        if i[0] not in line_num:
            return False
        if i[1] in op:
            return False
        for j in range(1,len(i)):
            if i[j] not in id:
                if i[j] not in command:
                    if i[j] not in op:
                        if i[j] not in line_num:
                            return False
            if j+1 == len(i):
                if i[j] in command or i[j] in op:
                    if i[j] != 'STOP':
                        return False
            if i[j] in op and i[j+1] not in id and i[j+1] not in const:
                return False
    return token_list

def parser_to_file(token):
    out_file = open("output"+filename,"w+")
    out = ''
    for i in token:
        out += '\n10 '
        for j in range(len(i)):
            if j == 0:
                out += str(i[j])+' '
            else:
                if i[j] == 'IF':
                    out += '13 0 '
                elif i[j] == 'GOTO':
                    out += '14 '
                elif i[j] == 'PRINT':
                    out += '15 0 '
                elif i[j] == 'STOP':
                    out += '16 0'
                elif i[j] in op:
                    out += '17 '+str(op.index(i[j])+1)+' '
                elif i[j] in id:
                    out += '11 '+str(id.find(i[j])+1)+' '
                else:
                    if j > 1 and i[j-1] not in command and i[j-1] not in op:
                        out += '14 '
                    elif j > 1 and i[j-1] == 'GOTO':
                        out += ''
                    else:
                        out += '12 '
                    out += str(i[j])+' '
    out += '\n0'
    out_file.write(out)
    out_file.close()
    print('')
    print(out)
    print('')
    print("finished write output")
    
while True:
    try:
        filename = input("input filename >> ").strip()
        file = open(filename, "r")
        if scanner(file) == False:
            print("InvalidSyntax")
        file.close()
            exit(0)
        break
    except FileNotFoundError:
        print("InvalidFilename")

parser_to_file(scanner(file))
file.close()
