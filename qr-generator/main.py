import qrcode
url = input("Enter the url you want to create a QR: ")
file_name = input("Enter the name of the file to want to save it as: ")

image = qrcode.make(url)
if not(file_name.endswith(".png")):
    file_name = file_name + ".png"
image.save(f"qr-generator/{file_name}")