# Token enumeration
class C:
    T_NONE = ''
    T_UNKNOWN = '?'
    T_EOF = 'eof'
    T_NEWLINE = 'nl'
    T_HLT = 'hlt'
    T_MOV = 'mov'
    T_INC = 'inc'
    T_DEC = 'dec'
    T_ADD = 'add'
    T_SUB = 'sub'
    T_AND = 'and'
    T_OR = 'or'
    T_XOR = 'xor'
    T_NOT = 'not'
    T_CMP = 'cmp'
    T_JMP = 'jmp'
    T_REGISTER = 'r'
    T_ADDRESS = '$'
    T_IMMEDIATE = '0'
    T_IDENTIFIER = 'id'

    # Opcode bytes
    OP_HLT = b'\x00'  # Halts the program
    OP_MOV_R_R = b'\x01'  # Moves value to register from register
    OP_MOV_R_M = b'\x02'  # ...to register from memory address
    OP_MOV_R_I = b'\x03'  # ...to register from immediate
    OP_MOV_M_R = b'\x04'  # ...to memory address from register
    OP_MOV_M_I = b'\x05'  # ...to memory address from immediate
    OP_INC_R = b'\x06'  # Increments register by 1
    OP_DEC_R = b'\x07'  # Decrements register by 1
    OP_ADD_R_R = b'\x08'  # Adds value of register to destination register (first operand)
    OP_ADD_R_M = b'\x09'  # ...of memory address to destination register
    OP_ADD_R_I = b'\x0A'  # ...of immediate to destination register
    OP_SUB_R_R = b'\x0B'  # Subtracts value of register from destination register (first operand)
    OP_SUB_R_M = b'\x0C'  # ...of memory address from destination register
    OP_SUB_R_I = b'\x0D'  # ...of immediate from destination register
    OP_AND_R_R = b'\x0E'  # Bitwise-ANDs value of register with destination register (first operand)
    OP_AND_R_M = b'\x0F'  # ...of memory address with destination register
    OP_AND_R_I = b'\x10'  # ...of immediate with destination register
    OP_OR_R_R = b'\x11'  # Bitwise-ORs value of register with destination register (first operand)
    OP_OR_R_M = b'\x12'  # ...of memory address with destination register
    OP_OR_R_I = b'\x13'  # ...of immediate with destination register
    OP_XOR_R_R = b'\x14'  # Bitwise-XORs value of register with destination register (first operand)
    OP_XOR_R_M = b'\x15'  # ...of memory address with destination register
    OP_XOR_R_I = b'\x16'  # ...of immediate with destination register
    OP_NOT_R = b'\x17'  # Bitwise-NOTs value of register
    OP_CMP_R_R = b'\x18'  # Sets zero flag to true if values of register and register are equal
    OP_CMP_R_M = b'\x19'  # ...of register and memory address are equal
    OP_CMP_R_I = b'\x1A'  # ...of register and immediate are equal
    OP_JMP_I = b'\x1B'  # Unconditionally jumps to instruction at given address

    # Register bytes
    R_A = b'\x00'
    R_B = b'\x01'
    R_C = b'\x02'
    R_D = b'\x03'
