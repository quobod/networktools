SYN_FLAG = "S"
ACK_FLAG = "A"
RST_FLAG = "R"
ACK_RST_FLAG = "AR"
SYN_ACK_FLAG = "SA"
FIN_FLAG = "F"
D_FLAG = "D"
D_FIN_FLAG = "DF"

FLAGS = {
    "s": SYN_FLAG,
    "a": ACK_FLAG,
    "r": RST_FLAG,
    "d": D_FLAG,
    "f": FIN_FLAG,
    "df": D_FIN_FLAG,
    "ar": ACK_RST_FLAG,
    "sa": SYN_ACK_FLAG,
}
