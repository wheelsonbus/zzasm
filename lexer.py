from constant import *


# Token data structure
class Token:
    def __init__(self, t, s):
        self.t = t  # Type
        self.s = s  # String


# Lexer class provides abstraction with which to split up and through individual tokens of an assembly file
class Lexer:
    def __init__(self, path):
        self.f = open(path, 'r')

    def __del__(self):
        self.f.close()

    # Consumes and returns the next character in the stream
    def get_char(self):
        return self.f.read(1)

    # Returns next the character in the stream without consuming it
    def peek_char(self):
        c = self.f.read(1)
        self.f.seek(self.f.tell() - 1)
        return c

    # Consumes and returns the next complete token in the stream
    # TODO: Needs expanded opcode handling
    # TODO: Needs comment and label handling
    def get_token(self):
        while True:
            s = self.get_char()

            # End of file
            if s == '':
                return Token(C.T_EOF, s)
            # Newline
            elif s == '\n':
                return Token(C.T_NEWLINE, s)
            # Opcodes and alphanumerical identifiers
            elif s.isalpha() or s == '.':
                while self.peek_char().isalnum():
                    s += self.get_char()
                match s:
                    case 'hlt':
                        return Token(C.T_HLT, s)
                    case 'mov':
                        return Token(C.T_MOV, s)
                    case 'inc':
                        return Token(C.T_INC, s)
                    case 'dec':
                        return Token(C.T_DEC, s)
                    case 'add':
                        return Token(C.T_ADD, s)
                    case 'sub':
                        return Token(C.T_SUB, s)
                    case 'and':
                        return Token(C.T_AND, s)
                    case 'or':
                        return Token(C.T_OR, s)
                    case 'xor':
                        return Token(C.T_XOR, s)
                    case 'not':
                        return Token(C.T_NOT, s)
                    case 'cmp':
                        return Token(C.T_CMP, s)
                    case 'jmp':
                        return Token(C.T_JMP, s)
                    case 'a' | 'b' | 'c' | 'd':
                        return Token(C.T_REGISTER, s)
                    case _:
                        return Token(C.T_IDENTIFIER, s)
            # Immediates
            elif s.isnumeric():
                if s == '0':
                    c = self.peek_char()
                    if c == 'b' or c == 'd' or c == 'x':
                        s += self.get_char()
                        while self.peek_char().isnumeric():
                            s += self.get_char()
                        return Token(C.T_IMMEDIATE, s)
                while self.peek_char().isnumeric():
                    s += self.get_char()
                return Token(C.T_IMMEDIATE, s)
            # Memory literals
            elif s == '$':
                while self.peek_char().isalnum():
                    s += self.get_char()
                return Token(C.T_ADDRESS, s)
            # Whitespace
            elif s == ' ':
                pass
            # Unknown tokens
            else:
                return Token(C.T_UNKNOWN, s)
