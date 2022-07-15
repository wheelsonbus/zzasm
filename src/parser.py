import constant
import lexer


class Parser:
    def __init__(self):
        self.f = None

    def __del__(self):
        if self.f:
            self.f.close()

    @staticmethod
    def parse_register(s):
        match s:
            case 'a':
                return constant.R_A
            case 'b':
                return constant.R_B
            case 'c':
                return constant.R_C
            case 'd':
                return constant.R_D
            case _:
                raise Exception('Invalid register identifier: ' + s)

    @staticmethod
    def parse_address(s):
        a = -1
        try:
            a = int(s[1:2], 16)
        except:
           raise Exception('Invalid address identifier: ' + s)

        if len(s) == 3 and s[0] == '$' and 255 >= a >= 0:
            return bytes([a])
        raise Exception('Invalid address identifier: ' + s)

    @staticmethod
    def parse_immediate(s):
        i = -1
        if s[:2] == '0b':
            try:
                i = int(s[2:], 2)
            except:
               raise Exception('Invalid immediate identifier: ' + s)
        elif s[0:2] == '0d':
            try:
                i = int(s[2:], 10)
            except:
               raise Exception('Invalid immediate identifier: ' + s)
        elif s[0:2] == '0x':
            try:
                i = int(s[2:], 16)
            except:
               raise Exception('Invalid immediate identifier: ' + s)
        else:
            try:
                i = int(s, 10)
            except:
               raise Exception('Invalid immediate identifier: ' + s)

        if 255 >= i >= 0:
            return bytes([i])
        raise Exception('Invalid address identifier: ' + s)

    def parse(self, path_in, path_out):
        l = lexer.Lexer(path_in)
        self.f = open(path_out, 'wb')

        while (t := l.get_token()).t != constant.T_EOF:
            instruction = b''
            match t.t:
                case constant.T_HLT:
                    instruction = constant.OP_HLT

                case constant.T_MOV:
                    d = l.get_token()
                    s = l.get_token()
                    if d.t == constant.T_REGISTER:
                        if s.t == constant.T_REGISTER:
                            instruction = constant.OP_MOV_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == constant.T_ADDRESS:
                            instruction = constant.OP_MOV_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == constant.T_IMMEDIATE:
                            instruction = constant.OP_MOV_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    elif d.t == constant.T_ADDRESS:
                        if s.t == constant.T_REGISTER:
                            instruction = constant.OP_MOV_M_R + self.parse_address(d.s) + self.parse_register(s.s)
                        elif s.t == constant.T_IMMEDIATE:
                            instruction = constant.OP_MOV_M_I + self.parse_address(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)

                case constant.T_INC:
                    r = l.get_token()
                    if r.t == constant.T_REGISTER:
                        instruction = constant.OP_INC_R + self.parse_register(r.s)
                    else:
                        print('Invalid token for register: ' + r.s)
                case constant.T_DEC:
                    r = l.get_token()
                    if r.t == constant.T_REGISTER:
                        instruction = constant.OP_INC_R + self.parse_register(r.s)
                    else:
                        print('Invalid token for register: ' + r.s)

                case constant.T_ADD:
                    d = l.get_token()
                    s = l.get_token()
                    if d.t == constant.T_REGISTER:
                        if s.t == constant.T_REGISTER:
                            instruction = constant.OP_ADD_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == constant.T_ADDRESS:
                            instruction = constant.OP_ADD_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == constant.T_IMMEDIATE:
                            instruction = constant.OP_ADD_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)
                case constant.T_SUB:
                    d = l.get_token()
                    s = l.get_token()
                    if d.t == constant.T_REGISTER:
                        if s.t == constant.T_REGISTER:
                            instruction = constant.OP_SUB_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == constant.T_ADDRESS:
                            instruction = constant.OP_SUB_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == constant.T_IMMEDIATE:
                            instruction = constant.OP_SUB_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)
                case constant.T_AND:
                    d = l.get_token()
                    s = l.get_token()
                    if d.t == constant.T_REGISTER:
                        if s.t == constant.T_REGISTER:
                            instruction = constant.OP_AND_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == constant.T_ADDRESS:
                            instruction = constant.OP_AND_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == constant.T_IMMEDIATE:
                            instruction = constant.OP_AND_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)
                case constant.T_OR:
                    d = l.get_token()
                    s = l.get_token()
                    if d.t == constant.T_REGISTER:
                        if s.t == constant.T_REGISTER:
                            instruction = constant.OP_OR_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == constant.T_ADDRESS:
                            instruction = constant.OP_OR_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == constant.T_IMMEDIATE:
                            instruction = constant.OP_OR_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)
                case constant.T_XOR:
                    d = l.get_token()
                    s = l.get_token()
                    if d.t == constant.T_REGISTER:
                        if s.t == constant.T_REGISTER:
                            instruction = constant.OP_XOR_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == constant.T_ADDRESS:
                            instruction = constant.OP_XOR_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == constant.T_IMMEDIATE:
                            instruction = constant.OP_XOR_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)
                case constant.T_NOT:
                    r = l.get_token()
                    if r.t == constant.T_REGISTER:
                        instruction = constant.OP_NOT_R + self.parse_register(r.s)
                    else:
                        print('Invalid token for register: ' + r.s)
                case constant.T_CMP:
                    d = l.get_token()
                    s = l.get_token()
                    if d.t == constant.T_REGISTER:
                        if s.t == constant.T_REGISTER:
                            instruction = constant.OP_CMP_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == constant.T_ADDRESS:
                            instruction = constant.OP_CMP_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == constant.T_IMMEDIATE:
                            instruction = constant.OP_CMP_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)
                case constant.T_JMP:
                    i = l.get_token()
                    if i.t == constant.T_IMMEDIATE:
                        instruction = constant.OP_JMP_I + self.parse_immediate(i.s)
                    else:
                        print('Invalid token for immediate: ' + i.s)

            if l.get_token().t != constant.T_NEWLINE:
                raise Exception("Expected newline after instruction: " + str(instruction))

            print(instruction)
            self.f.write(instruction)

        self.f.close()
