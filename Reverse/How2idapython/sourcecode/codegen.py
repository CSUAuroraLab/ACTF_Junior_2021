import random

def rand():
    return int(random.random() * 1000)

def run():
    with open('./code.asm','a',encoding='utf8') as f:
        affted = rand()%0x2f
        f.write("        \"mov al,[rdx+{}]\\n\"\\\n".format(affted))
        f.write("        \"add al,{}\\n\"\\\n".format(rand()%0xff))
        f.write("        \"mov [rdx+{}],al\\n\"\\\n".format(affted))
    return

if __name__ == '__main__':
    for i in range(1000):
        run()