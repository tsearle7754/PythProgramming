def TwistHash(text):
    h = 0x9E3779B1
    mult = 0x517CC1C7
    mask = 0xFFFFFFFF
    
    
    for c in text:
        # char code, XOR, multiplier, & mask
        char_code = ord(c)
        h = h ^ char_code
        h = (h * mult) & mask
    
    # final mix with length
    h = h ^ len(text)
    return h
        
text = input("Enter a string: ")
result = TwistHash(text)
print(f"Twist Hash result for '{text}' = '{result}'")