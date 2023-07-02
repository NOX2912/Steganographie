# Steganography Python Script

This Python script allows you to hide a text message within an image using steganography techniques. It also provides functionality to extract and retrieve the hidden message from the image.

## Requirements
- Python 3.x
- Pillow library (install using `pip install pillow`)
- bitarray

## Usage

1. Clone the repository or download the script `main.py` to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install pillow
   pip install bitarray
   ```
   

3. Prepare the image and the text message:
   - Choose an image file (in formats supported by Pillow) that you want to use for hiding the message.
   - Create a text file (.txt) containing the message you want to hide within the image. Make sure the text file is in the same directory as the script.

4. Open a terminal or command prompt and navigate to the directory containing the script.

5. To hide the text message within the image, run the following command:
   ```
   python main.py hide <image_file> <message_file> <output_file>
   ```
   Replace `<image_file>` with the path to the image file you chose, `<message_file>` with the path to the text file containing the message, and `<output_file>` with the desired name and path for the output image file.

   For example:
   ```
   python main.py hide input_image.png message.txt output_image.png
   ```

6. The script will process the image and embed the message within it. The output image file with the hidden message will be saved at the specified path.

7. To extract the hidden message from the image, run the following command:
   ```
   python main.py seek <image_file> <extracted_message_file>
   ```
   Replace `<image_file>` with the path to the image file containing the hidden message and `<extracted_message_file>` with the path to the text file where to save the secret text.

   For example:
   ```
   python main.py seek output_image.png
   ```

8. The script will read the hidden message from the image and display it in the terminal.

## Important Notes

- The capacity of the image to hide a message depends on its size and color depth. Larger images with more colors have higher capacity. Extremely large messages may not fit within the image.
- For best results, choose images with complex patterns or high entropy, as plain backgrounds or solid colors might make the hidden message more noticeable.
- Keep in mind that steganography is not foolproof and can be detected by advanced analysis techniques. It is not suitable for highly sensitive or confidential information.
- Always respect privacy and legal boundaries when using steganography techniques.
