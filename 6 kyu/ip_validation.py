def is_valid_IP(addr):
    if len(addr.split('.')) < 4 or ' ' in addr:
        return 0

    for i in addr.split('.'):
        try:
            if int(i) not in list(range(0, 256)) or i[0] == '0' and len(i) > 1:
                return 0
        except:
            return 0

    return 1
