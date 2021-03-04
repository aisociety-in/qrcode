import qrcode
qr=qrcode.QRCode(
	version=1,
	box_size=10,
	border=5
)

data="TN 60 T 8427"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("3.png")
