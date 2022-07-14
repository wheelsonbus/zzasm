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
            elif s == ',':
                return Token(constant.T_COMMA, s)
            elif s.isalpha() or s == '.':
                while self.peek_char().isalnum():
                    s += self.get_char()
                if s == 'hlt':
                    return Token(constant.T_HLT, s)
                elif s == 'mov':
                    return Token(constant.T_MOV, s)
                elif s == 'a' or s == 'b' or s == 'c' or s == 'd':
                    return Token(constant.T_REGISTER, s)
                else:
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
