import constant


class Token:
    def __init__(self, t, s):
        self.t = t
        self.s = s


class Lexer:
    def __init__(self, path):
        self.f = open(path, 'r')

    def __del__(self):
        self.f.close()

    def get_char(self):
        return self.f.read(1)

    def peek_char(self):
        c = self.f.read(1)
        self.f.seek(self.f.tell() - 1)
        return c

    # TODO: Needs expanded opcode handling
    # TODO: Needs comment and label handling
    def get_token(self):
        while True:
            s = self.get_char()
            if s == '':
                return Token(constant.T_EOF, s)
            elif s == '\n':
                return Token(constant.T_NEWLINE, s)
            elif s.isalpha() or s == '.':
                while self.peek_char().isalnum():
                    s += self.get_char()
                match s:
                    case 'hlt':
                        return Token(constant.T_HLT, s)
                    case 'mov':
                        return Token(constant.T_MOV, s)
                    case 'inc':
                        return Token(constant.T_INC, s)
                    case 'dec':
                        return Token(constant.T_DEC, s)
                    case 'add':
                        return Token(constant.T_ADD, s)
                    case 'sub':
                        return Token(constant.T_SUB, s)
                    case 'and':
                        return Token(constant.T_AND, s)
                    case 'or':
                        return Token(constant.T_OR, s)
                    case 'xor':
                        return Token(constant.T_XOR, s)
                    case 'not':
                        return Token(constant.T_NOT, s)
                    case 'cmp':
                        return Token(constant.T_CMP, s)
                    case 'jmp':
                        return Token(constant.T_JMP, s)
                    case 'a' | 'b' | 'c' | 'd':
                        return Token(constant.T_REGISTER, s)
                    case _:
                        return Token(constant.T_IDENTIFIER, s)
            elif s.isnumeric():
                if s == '0':
                    c = self.peek_char()
                    if c == 'b' or c == 'd' or c == 'x':
                        s += self.get_char()
                        while self.peek_char().isnumeric():
                            s += self.get_char()
                        return Token(constant.T_IMMEDIATE, s)
                while self.peek_char().isnumeric():
                    s += self.get_char()
                return Token(constant.T_IMMEDIATE, s)
            elif s == '$':
                while self.peek_char().isalnum():
                    s += self.get_char()
                return Token(constant.T_ADDRESS, s)
            elif s == ' ':
                pass
            else:
                return Token(constant.T_UNKNOWN, s)
