from xmlrpc.server import list_public_methods


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def main():
    with open('birthday.txt', 'r', encoding='UTF8') as f:
        list_name =  list(f.read().split())
        list_name.sort()
        list_A, list_B = split_list(list_name)
        
    with open('birthday.txt', 'w', encoding='UTF8') as f:
        text = ''
        cnt = 0
    
        for name in list_A:
            text += name + ' '
            cnt += 1
            if cnt==len(list_A)//2:
                text = text.rstrip()
                text += '\n'
        
        text = text.rstrip()
        text += '\n\n'
        cnt = 0
        
        for name in list_B:
            text += name + ' '
            cnt += 1
            if cnt==len(list_B)//2:
                text = text.rstrip()
                text += '\n'
            
        text = text.rstrip()
        f.write(text)

if __name__ == "__main__":
    main()