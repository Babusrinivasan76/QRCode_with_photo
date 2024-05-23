import qrcode
from PIL import Image

def generate_qr_with_photo(data, qr_filename, photo_filename, output_filename):
    # Step 1: Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Step 2: Open the photo and resize it
    photo = Image.open(photo_filename)
    qr_width, qr_height = qr_img.size
    factor = 3  # This factor determines the size of the photo relative to the QR code
    size = qr_width // factor, qr_height // factor
    photo = photo.resize(size, Image.ANTIALIAS)

    # Step 3: Calculate the position to place the photo
    pos = ((qr_width - size[0]) // 2, (qr_height - size[1]) // 2)

    # Step 4: Embed the photo into the QR code
    qr_img = qr_img.convert("RGBA")
    photo = photo.convert("RGBA")
    qr_img.paste(photo, pos, photo)

    # Step 5: Save the final image
    qr_img.save(output_filename)

# Example usage
data = "https://www.linkedin.com/in/xxxxxxx/"
qr_filename = "qr_code.png"
photo_filename = "Your_Photo.png"
output_filename = "qr_with_photo.png"

generate_qr_with_photo(data, qr_filename, photo_filename, output_filename)
