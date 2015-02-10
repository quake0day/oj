m = 0x1d7777c38863aec21ba2d91ee0faf51
e = 0x5abb
d = 0x1146bd07f0b74c086df00b37c602a0b

c_243 = pow(243, e, m)
c_101 = pow(101, e, m)

print pow(c_101, d, m)

cipher_multiply = 0x15c713c3db45595b17a5598471c36db * \
                      0x12314f0fe732e421017cf710dd1834c
print pow(cipher_multiply, d, m)