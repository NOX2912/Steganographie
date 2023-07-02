from PIL import Image
import bitarray
import argparse


def file_to_bitarray(path: str) -> bitarray.bitarray:
    # This function reads binary data from a file and returns it as a bitarray object.
    result = bitarray.bitarray()
    with open(path, 'rb') as file:
        result.fromfile(file)
    return result


def bitarray_to_file(path: str, bits) -> None:
    # This function writes the bits (a bitarray object) to a file in binary mode.
    with open(path, 'wb') as file:
        bits.tofile(file)


def set_last_bit(value: int, integer: int) -> int:
    # This function takes an integer and replaces its least significant bit with the specified value. It returns the modified integer.
    bits = '{0:b}'.format(integer)
    return int(bits[0:len(bits) - 1] + str(value), 2)


def get_last_bit(integer: int) -> int:
    # This function returns the least significant bit of the given integer.
    bits = '{0:b}'.format(integer)
    return int(bits[len(bits) - 1])


def hide(input_file: str, secret: str, output_file: str) -> None:
    # Hides a messsage in an image.
    image = Image.open(input_file)
    picture = image.load()
    width, height = image.size
    to_hide = file_to_bitarray(secret)

    k = 0
    l = len(to_hide)
    for y in range(height):
        for x in range(width):
            pixel = picture[x, y]

            r = set_last_bit(to_hide[k % l], pixel[0])
            k += 1
            g = set_last_bit(to_hide[k % l], pixel[1])
            k += 1
            b = set_last_bit(to_hide[k % l], pixel[2])
            k += 1

            picture[x, y] = (r, g, b)

    image.save(output_file)


def seek(input_file: str, output_file: str) -> None:
    # Save the hidden message in the output file.
    image = Image.open(input_file)
    picture = image.load()
    width, height = image.size
    bits = ''

    for y in range(height):
        for x in range(width):
            pixel = picture[x, y]
            bits += str(get_last_bit(pixel[0]))
            bits += str(get_last_bit(pixel[1]))
            bits += str(get_last_bit(pixel[2]))

    bitarray_to_file(output_file, bitarray.bitarray(bits))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hide or seek information in an image.')
    subparsers = parser.add_subparsers(dest='command')

    hide_parser = subparsers.add_parser('hide', help='Hide information in an image.')
    hide_parser.add_argument('input_file', type=str, help='Path to the input image file.')
    hide_parser.add_argument('secret', type=str, help='Path to the secret file to hide.')
    hide_parser.add_argument('output_file', type=str, help='Path to the output image file.')

    seek_parser = subparsers.add_parser('seek', help='Seek hidden information in an image.')
    seek_parser.add_argument('input_file', type=str, help='Path to the input image file.')
    seek_parser.add_argument('output_file', type=str, help='Path to the output file to store the hidden information.')

    args = parser.parse_args()

    if args.command == 'hide':
        hide(args.input_file, args.secret, args.output_file)
    elif args.command == 'seek':
        seek(args.input_file, args.output_file)
    else:
        print('Invalid command.')

