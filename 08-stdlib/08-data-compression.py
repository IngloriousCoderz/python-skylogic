import zlib

message = b"she sells sea shells on the sea shore. the shells that she sells are sea shells i'm sure."
print(len(message))

compressed = zlib.compress(message)
print(len(compressed))

decompressed = zlib.decompress(compressed)
print(len(decompressed))
