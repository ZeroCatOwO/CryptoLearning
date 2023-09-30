from Crypto.Util.number import *

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    byte_output_arr =  [long_to_bytes(i) for row in matrix for i in row]
    byte_output = b"".join(byte_output_arr)
            
    return byte_output.decode()

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))