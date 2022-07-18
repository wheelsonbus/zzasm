from constant import *
from lexer import *


# Parser class reads an assembly infile and writes a .zz machine code outfile
class Parser:
    def __init__(self):
        self.f = None

    def __del__(self):
        if self.f:
            self.f.close()

    # Returns an operand byte for a given assembly string identifying a register
    @staticmethod
    def parse_register(s):
        match s:
            case 'a':
                return C.R_A
            case 'b':
                return C.R_B
            case 'c':
                return C.R_C
            case 'd':
                return C.R_D
            case 'ha':
                return C.R_HA
            case _:
                print('Invalid register identifier: ' + s)

    # Returns an operand byte for a given assembly string identifying a memory address
    @staticmethod
    def parse_address(s):
        a = -1
        try:
            a = int(s[1:], 16)
        except:
           print('Invalid address identifier: ' + s)

        if len(s) == 3 and s[0] == '$' and 255 >= a >= 0:
            return bytes([a])
        print('Invalid address identifier: ' + s)

    # Returns an operand byte for a given assembly string identifying an immediate
    @staticmethod
    def parse_immediate(s):
        i = -1
        if s[:2] == '0b':
            try:
                i = int(s[2:], 2)
            except:
               print('Invalid immediate identifier: ' + s)
        elif s[0:2] == '0d':
            try:
                i = int(s[2:], 10)
            except:
               print('Invalid immediate identifier: ' + s)
        elif s[0:2] == '0x':
            try:
                i = int(s[2:], 16)
            except:
               print('Invalid immediate identifier: ' + s)
        else:
            try:
                i = int(s, 10)
            except:
               print('Invalid immediate identifier: ' + s)

        if 255 >= i >= 0:
            return bytes([i])
        print('Invalid address identifier: ' + s)

    # Parses a .zzasm infile producing a .zz outfile
    def parse(self, path_in, path_out):
        lexer = Lexer(path_in)
        self.f = open(path_out, 'wb')

        while (t := lexer.get_token()).t != C.T_EOF:
            instruction = b''

            match t.t:
                # Halt opcode
                case C.T_HLT:
                    instruction = C.OP_HLT

                # Move opcode
                case C.T_MOV:
                    d = lexer.get_token()
                    s = lexer.get_token()
                    if d.t == C.T_REGISTER:
                        if s.t == C.T_REGISTER:
                            instruction = C.OP_MOV_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == C.T_ADDRESS:
                            instruction = C.OP_MOV_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == C.T_IMMEDIATE:
                            instruction = C.OP_MOV_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    elif d.t == C.T_ADDRESS:
                        if s.t == C.T_REGISTER:
                            instruction = C.OP_MOV_M_R + self.parse_address(d.s) + self.parse_register(s.s)
                        elif s.t == C.T_IMMEDIATE:
                            instruction = C.OP_MOV_M_I + self.parse_address(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)

                # Increment and decrement opcodes
                case C.T_INC:
                    r = lexer.get_token()
                    if r.t == C.T_REGISTER:
                        instruction = C.OP_INC_R + self.parse_register(r.s)
                    else:
                        print('Invalid token for register: ' + r.s)
                case C.T_DEC:
                    r = lexer.get_token()
                    if r.t == C.T_REGISTER:
                        instruction = C.OP_INC_R + self.parse_register(r.s)
                    else:
                        print('Invalid token for register: ' + r.s)

                # Arithmetic opcodes
                case C.T_ADD:
                    d = lexer.get_token()
                    s = lexer.get_token()
                    if d.t == C.T_REGISTER:
                        if s.t == C.T_REGISTER:
                            instruction = C.OP_ADD_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == C.T_ADDRESS:
                            instruction = C.OP_ADD_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == C.T_IMMEDIATE:
                            instruction = C.OP_ADD_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)
                case C.T_SUB:
                    d = lexer.get_token()
                    s = lexer.get_token()
                    if d.t == C.T_REGISTER:
                        if s.t == C.T_REGISTER:
                            instruction = C.OP_SUB_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == C.T_ADDRESS:
                            instruction = C.OP_SUB_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == C.T_IMMEDIATE:
                            instruction = C.OP_SUB_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)

                # Bitwise opcodes
                case C.T_AND:
                    d = lexer.get_token()
                    s = lexer.get_token()
                    if d.t == C.T_REGISTER:
                        if s.t == C.T_REGISTER:
                            instruction = C.OP_AND_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == C.T_ADDRESS:
                            instruction = C.OP_AND_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == C.T_IMMEDIATE:
                            instruction = C.OP_AND_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)
                case C.T_OR:
                    d = lexer.get_token()
                    s = lexer.get_token()
                    if d.t == C.T_REGISTER:
                        if s.t == C.T_REGISTER:
                            instruction = C.OP_OR_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == C.T_ADDRESS:
                            instruction = C.OP_OR_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == C.T_IMMEDIATE:
                            instruction = C.OP_OR_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)
                case C.T_XOR:
                    d = lexer.get_token()
                    s = lexer.get_token()
                    if d.t == C.T_REGISTER:
                        if s.t == C.T_REGISTER:
                            instruction = C.OP_XOR_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == C.T_ADDRESS:
                            instruction = C.OP_XOR_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == C.T_IMMEDIATE:
                            instruction = C.OP_XOR_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)
                case C.T_NOT:
                    r = lexer.get_token()
                    if r.t == C.T_REGISTER:
                        instruction = C.OP_NOT_R + self.parse_register(r.s)
                    else:
                        print('Invalid token for register: ' + r.s)

                # Equality comparison opcode
                case C.T_CMP:
                    d = lexer.get_token()
                    s = lexer.get_token()
                    if d.t == C.T_REGISTER:
                        if s.t == C.T_REGISTER:
                            instruction = C.OP_CMP_R_R + self.parse_register(d.s) + self.parse_register(s.s)
                        elif s.t == C.T_ADDRESS:
                            instruction = C.OP_CMP_R_M + self.parse_register(d.s) + self.parse_address(s.s)
                        elif s.t == C.T_IMMEDIATE:
                            instruction = C.OP_CMP_R_I + self.parse_register(d.s) + self.parse_immediate(s.s)
                        else:
                            print('Invalid token for source: ' + s.s)
                    else:
                        print('Invalid token for destination: ' + d.s)

                # Jump opcodes
                case C.T_JMP:
                    i = lexer.get_token()
                    if i.t == C.T_IMMEDIATE:
                        instruction = C.OP_JMP_I + self.parse_immediate(i.s)
                    else:
                        print('Invalid token for immediate: ' + i.s)
                case C.T_JZ:
                    i = lexer.get_token()
                    if i.t == C.T_IMMEDIATE:
                        instruction = C.OP_JZ_I + self.parse_immediate(i.s)
                    else:
                        print('Invalid token for immediate: ' + i.s)
                case C.T_JNZ:
                    i = lexer.get_token()
                    if i.t == C.T_IMMEDIATE:
                        instruction = C.OP_JNZ_I + self.parse_immediate(i.s)
                    else:
                        print('Invalid token for immediate: ' + i.s)
                case C.T_JC:
                    i = lexer.get_token()
                    if i.t == C.T_IMMEDIATE:
                        instruction = C.OP_JC_I + self.parse_immediate(i.s)
                    else:
                        print('Invalid token for immediate: ' + i.s)
                case C.T_JNC:
                    i = lexer.get_token()
                    if i.t == C.T_IMMEDIATE:
                        instruction = C.OP_JNC_I + self.parse_immediate(i.s)
                    else:
                        print('Invalid token for immediate: ' + i.s)
                case C.T_JA:
                    i = lexer.get_token()
                    if i.t == C.T_IMMEDIATE:
                        instruction = C.OP_JA_I + self.parse_immediate(i.s)
                    else:
                        print('Invalid token for immediate: ' + i.s)
                case C.T_JNA:
                    i = lexer.get_token()
                    if i.t == C.T_IMMEDIATE:
                        instruction = C.OP_JNA_I + self.parse_immediate(i.s)
                    else:
                        print('Invalid token for immediate: ' + i.s)

            # Necessitates a newline after each assembly instruction
            if lexer.get_token().t != C.T_NEWLINE:
                print("Expected newline after instruction: " + str(instruction))

            # Write instruction to outfile
            self.f.write(instruction)
            print(instruction)

        self.f.close()
