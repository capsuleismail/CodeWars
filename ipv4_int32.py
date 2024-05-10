def ip_to_int32(ip):
    octets = ip.split('.')
    
    binary_str = ''.join(format(int(octet), '08b') for octet in octets)
    
    int_val = int(binary_str, 2)
    
    return int_val
