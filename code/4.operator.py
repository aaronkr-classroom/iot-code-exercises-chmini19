# 4_operators.py
a = 132
b = 45

fmt0 = '{:<10}'
fmt1 = '0b{:08b} 0x{:02x} {:3}'
#bit AND
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))

n= 30
print('-' * n)
print(fmt0.format('a & b'), fmt1.format(a&b,a&b,a&b))

#bit OR
print()
print(fmt0.format('\na'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))

print('-' * n)
print(fmt0.format('a | b'), fmt1.format(a|b,a|b,a|b))

#bit XOR
print()
print(fmt0.format('\na'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))

print('-' * n)
print(fmt0.format('a ^ b'), fmt1.format(a^b,a^b,a^b))

#bit not
print()
print(fmt0.format('\na'), fmt1.format(a,a,a))

print('-' * n)
print(fmt0.format('~a'), fmt1.format(~a&0xFF,~a&0xFF,~a&0xFF))

#bit 왼쪽 쉬프트
print()
print(fmt0.format('\na'), fmt1.format(a,a,a))

print('-' * n)
print(fmt0.format('a << 2'), fmt1.format(a<<2&0xFF,a<<2&0xFF,a<<2&0xFF))

#bit 오른쪽 쉬프트
print()
print(fmt0.format('\na'), fmt1.format(a,a,a))

print('-' * n)
print(fmt0.format('a >> 2'), fmt1.format(a>>2&0xFF,a>>2&0xFF,a>>2&0xFF))




