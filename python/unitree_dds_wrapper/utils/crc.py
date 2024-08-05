def crc32(data):
    bit = 0
    crc = 0xFFFFFFFF
    polynomial = 0x04c11db7

    for i in range(len(data)):
        bit = 1 << 31
        current = data[i]

        for b in range(32):
            if crc & 0x80000000:
                crc = (crc << 1) & 0xFFFFFFFF
                crc ^= polynomial
            else:
                crc = (crc << 1) & 0xFFFFFFFF

            if current & bit:
                crc ^= polynomial

            bit >>= 1
    
    return crc