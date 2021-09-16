def generate(lsys, total_iterations):
    lstring = lsys.start
    rules = lsys.rules
    
    for i in range(total_iterations):
        str_buf = []
        for symbol in lstring:          
            str_buf.append(rules.get(symbol, symbol))
        lstring = ''.join(str_buf)          
    return lstring        
