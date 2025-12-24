def encode_text(nam1):
    return nam1.encode("utf-8")

en = encode_text("سلام چطوری")
print(en)


def decode_text(nam2):
    return nam2.decode("utf-8")

de = en.decode( "utf-8" )
print(de)





