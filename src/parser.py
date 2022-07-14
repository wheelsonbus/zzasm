import constant
import lexer


class Parser:
    def __init__(self, path):
        self.lexer = lexer.Lexer(path)

    def run(self):
        while (t := self.lexer.get_token()).t != constant.T_EOF:
            print(t.t + ": ", t.s)
