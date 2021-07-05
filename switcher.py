TEST = 'ABCDE'

def wanker():
    print('Wanker')

def old_man():
    print('Old Man')

def jesus():
    print('jesus')

def saint():
    print('Saint')

def hate():
    print('Blind Fish')

def call(arg):
    switcher = {
       0: old_man(),
       1: wanker(),
       2: jesus(),
       3: saint(),
    }
    switcher.get(arg, hate())

if __name__ == "__main__":
    for nme in TEST:
        call(nme)
