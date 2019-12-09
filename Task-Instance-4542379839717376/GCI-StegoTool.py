from PIL import Image
import argparse

def generateData(data):
	new_data = []
	for i in data:
		new_data.append(format(ord(i), '08b'))
	return new_data 

def modifyPixel(pixel, data):
	data_list = generateData(data)
	lendata = len(data_list)
	imgdata = iter(pixel)
	
	for i in range(lendata):
		pixel = [value for value in imgdata.__next__()[:3]+imgdata.__next__()[:3]+imgdata.__next__()[:3]]
		for j in range(0, 8):
			if(data_list[i][j]=='0') and (pixel[j]% 2 != 0):
				if(pixel[j]% 2 != 0):
					pixel[j] -= 1
			elif(data_list[i][j] == '1') and (pixel[j] % 2 == 0):
				pixel[j] -= 1
		
		if(i == lendata - 1):
			if(pixel[-1] % 2 == 0):
				pixel[-1] -= 1
		else:
			if(pixel[-1] % 2 != 0):
				pixel[-1] -= 1
		pixel = tuple(pixel)
		yield pixel[0:3]
		yield pixel[3:6]
		yield pixel[6:9]

def encode2(new_img, data):
	w = new_img.size[0]
	x,y = 0,0
	
	for pixel in modifyPixel(new_img.getdata(), data):
		new_img.putpixel((x, y), pixel)
		if(x == w - 1):
			x = 0
			y += 1
		else:
			x += 1

def encode(img):
	image = Image.open(img, 'r')
	data = input("Enter data to be encoded : ")
	if(len(data) == 0):
		raise ValueError('Data is empty')
	new_img = image.copy()
	encode2(new_img, data)
	new_img_name = input("Enter the name of new image(with extension): ")
	new_img.save(new_img_name, str(new_img_name.split(".")[1].upper()))

def decode(img):
	image = Image.open(img, 'r')
	data = ''
	imgdata = iter(image.getdata())
	while(True):
		pixels = [value for value in imgdata.__next__()[:3]+imgdata.__next__()[:3]+imgdata.__next__()[:3]]
		binstr = ''
		for i in pixels[:8]:
			if(i % 2 == 0):
				binstr += '0'
			else:
				binstr += '1'
		data += chr(int(binstr, 2))
		if(pixels[-1] % 2 != 0):
			return data

def main():
	if(a == 1):
		encode()
	elif(a == 2):
		print("Decoded word- " + decode())
	else:
		raise Exception("Enter correct input")  

def argument():
    help_text = "		$ python GCI-StegoTool.py -e <Image> to Encode data.\n		$ python GCI-StegoTool.py -d <Image> to Decode data."
    parser = argparse.ArgumentParser(description=help_text)
    parser.add_argument('-e', '--encode', type=str, help='Encode data in file <Image>')
    parser.add_argument('-d', '--decode', type=str, help='Decode data from file <Image>')
    args = parser.parse_args()
    
    if(args.encode):
        return args.encode,1
    elif(args.decode):
        return args.decode,2
    else:
        print(help_text)
        raise Exception("No Argument Provided")
        exit(1)
        
if __name__ == '__main__':
    arg,flg = argument()
    if(flg==1):
        encode(arg)
    elif(flg==2):
        print("Decoded Data : ", decode(arg))
