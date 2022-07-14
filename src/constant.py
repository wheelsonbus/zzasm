# Token enumeration
T_NONE = ''
T_UNKNOWN = '?'
T_EOF = 'eof'
T_NEWLINE = 'nl'
T_MOV = 'mov'
T_HLT = 'hlt'
T_REGISTER = 'r'
T_ADDRESS = '$'
T_IMMEDIATE = '0'
T_IDENTIFIER = 'id'

# Opcode bytes
OP_HLT = b'\x00'
OP_MOV_R_R = b'\x01'
OP_MOV_R_M = b'\x02'
OP_MOV_R_I = b'\x03'
OP_MOV_M_R = b'\x04'
OP_MOV_M_I = b'\x05'

# Register bytes
R_A = b'\x00'
R_B = b'\x01'
R_C = b'\x02'
R_D = b'\x03'
