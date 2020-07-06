# -------------------------------------------------------------------------
# | start char(1) | address(2) | sequence number(4) | length(4) | payload |
# -------------------------------------------------------------------------

def frame(start_ch, addr, seqNo, msg):
    addr = str(addr).zfill(2)
    seqNo = str(seqNo).zfill(4)
    length = str(len(msg)).zfill(4)
    return chr(start_ch) + addr + seqNo + length + msg


if __name__ == "__main__":
    start_ch = 0x05
    addr = 2
    seqNo = 1
    msg = "Hello World!"

    capsule = frame(start_ch, addr, seqNo, msg)
    print(capsule)
