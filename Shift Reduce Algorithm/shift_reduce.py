action_table = {
            (0, 'id'): 'shift 5',
            (0, '('): 'shift 4',
            (1, '+'): 'shift 6',
            (1, '$'): 'accept',
            (2, '+'): 'reduce 2',
            (2, '*'): 'shift 7',
            (2, ')'): 'reduce 2',
            (2, '$'): 'reduce 2',
            (3, '+'): 'reduce 4',
            (3, '*'): 'reduce 4',
            (3, ')'): 'reduce 4',
            (3, '$'): 'reduce 4',
            (4, 'id'): 'shift 5',
            (4, '('): 'shift 4',
            (5, '+'): 'reduce 6',
            (5, '*'): 'reduce 6',
            (5, ')'): 'reduce 6',
            (5, '$'): 'reduce 6',
            (6, 'id'): 'shift 5',
            (6, '('): 'shift 4',
            (7, 'id'): 'shift 5',
            (7, '('): 'shift 4',
            (8, '+'): 'shift 6',
            (8, ')'): 'shift 11',
            (9, '+'): 'reduce 1',
            (9, '*'): 'shift 7',
            (9, ')'): 'reduce 1',
            (9, '$'): 'reduce 1',
            (10, '+'): 'reduce 3',
            (10, '*'): 'reduce 3',
            (10, ')'): 'reduce 3',
            (10, '$'): 'reduce 3',
            (11, '+'): 'reduce 5',
            (11, '*'): 'reduce 5',
            (11, ')'): 'reduce 5',
            (11, '$'): 'reduce 5'}
table = {
            (0, 'E'): '1',
            (0, 'T'): '2',
            (0, 'F'): '3',
            (4, 'E'): '8',
            (4, 'T'): '2',
            (4, 'F'): '3',
            (6, 'T'): '9',
            (6, 'F'): '3',
            (7, 'F'): '10',
            (11, 'E'): '12'}
grammar = {
    (1, 'E+T'): 'E',
    (2, 'T'): 'E',
    (3, 'T*F'): 'T',
    (4, 'F'): 'T',
    (5, '(E)'): 'F',
    (6, 'id'): 'F'}

print("Enter your string:")
string = input()
stack = ['0']
input_buffer = list(string) + ['$']
index = 0
ETF = None
previous_symbol = None
while True:
    state = int(stack[-1])
    symbol = input_buffer[index]
    if symbol == 'i':
        index += 1
        symbol = symbol + input_buffer[index]

    action = action_table.get((state, symbol))

    if action is None:
        print("INVALID string entered. SYNTAX ERROR!")
        break

    if action == 'accept':
        print("VALID string entered. ACCEPTED!")
        break
    if action.startswith('shift'):
        _, next_state = action.split()
        stack.append(symbol)
        stack.append(next_state)
        index += 1
        previous_symbol = symbol

    elif action.startswith('reduce'):
        _, goto_grammar = action.split()
        stack.pop()
        if int(goto_grammar) == 1:
            if '+' in stack:
                del stack[-5:]
            else:
                print("INVALID string entered. SYNTAX ERROR!")
            stack.append('E')
            ETF = 'E'
            previous_symbol = 'E'
        elif int(goto_grammar) == 3:
            if '*' in stack:
                del stack[-5:]
            else:
                print("INVALID string entered. SYNTAX ERROR!")
            stack.append('T')
            ETF = 'T'
            previous_symbol = 'T'
        elif int(goto_grammar) == 5:
            if '(' in stack and ')' in stack:
                del stack[-5:]
            else:
                print("INVALID string entered. SYNTAX ERROR!")
            stack.append('F')
            ETF = 'F'
            previous_symbol = 'F'
        else:
            if previous_symbol == 'id':
                stack.pop() * 2
            else:
                stack.pop()
            ETF = grammar.get((int(goto_grammar), previous_symbol))
            previous_symbol = ETF
            stack.append(ETF)
        goto_table = int(stack[-2])
        next_state = table.get((int(goto_table), stack[-1]))
        stack.append(next_state)