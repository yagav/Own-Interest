from PIL import Image

def encode(data, source):
    # Opening/loading the image 
    try:
        image = Image.open(source)
    except:
        return "Choose a appropriate image file"

    # Getting height and width variable
    width, height = image.size

    total_pix = width*height
    if len(data)*9 > total_pix:
        return "The text you have entered is exceding the amount of pixels, choose a larger image or shorten the text"
    # Getting the pixle data of the image
    val = image.getdata()
    # Changing the tuple into a list to edit the pixel data
    val = [list(x) for x in val]
    #Passing the data to convert it into binary form
    Conv_data = StrToBin(data)
    #Passing values to encode the text inside the image
    edited_val = EditPixelData(val,Conv_data)
    #Changing the edited pixel values into tuples 
    #So we can convert it into an image

    tup = [tuple(cell) for cell in edited_val]

    #Passing the tuples or the edited pixel value to form a image
    img = Image.new(image.mode, (width, height))
    img.putdata(tup)

    #Saving the edited image
    img.save("output.png")

#pix = pixel data ; bindata = binary data that needs to be encoded in image
def EditPixelData(pix, bindata):
    LenBin = len(bindata)
    pix_count = 0
    #Starting a loop to alter pixel data
    for count in range(LenBin):
        #Splitting the binary string eg: 0110 as ['0', '1', '1', '0'] 
        bin_val = [x for x in bindata[count]]
        #every binary number needs 3 cells or pixel to be stored 
        for t in range(3):
            #every pixel has r,g,b so we are altering it
            for i in range(3):
                #Checking weather it is the last value in the last pixel
                #So we can change it into ODD(if no other binary number or character is there) 
                #or EVEN(if there is still binary number or character needs to be enceoded left)
                if t==2 and i == 2:
                    if count<(LenBin-1):
                        if pix[pix_count][i]%2 != 0:
                            if pix[pix_count][i] != 255:
                                pix[pix_count][i]+=1
                            else:
                                pix[pix_count][i]-=1
                    else:
                        if pix[pix_count][i]%2 != 1:
                            if pix[pix_count][i] != 0:
                                pix[pix_count][i]-=1
                            else:
                                pix[pix_count][i]+=1
                
                #Altering value to store 1 or 0 in form of ODD or EVEN
                else:
                    #poping the first digit of the binary number
                    bin_val_num = bin_val.pop(0)
                    #if 0 the part of the pixel will be made EVEN 
                    if bin_val_num == "0":
                        if pix[pix_count][i]%2 != 0:
                            if pix[pix_count][i] != 225:
                                pix[pix_count][i]+=1
                            else:
                                pix[pix_count][i]-=1
                    #if 1 the part of the pixel will be made ODD
                    else:
                        if pix[pix_count][i]%2 !=1:
                            pix[pix_count][i]+=1
            
            #increamenting the pixel count by 1
            pix_count+=1
    
    #Finally returning the altered pixel data
    return pix

#Converting user inputted data into binary form
def StrToBin(data):
    bin_values = []
    #Splitting a string into a list of characters
    string = [char for char in data]

    for char in string:
        #changing char in the string to ascii value
        ascii_val = ord(char)
        #changing the ascii value into binary form(eg:10101010)
        bin_val = bin(ascii_val)
        bin_val = bin_val.replace('b',"")

        if len(bin_val) == 7:
            bin_val = [x for x in bin_val]
            bin_val.insert(0,"0")
            bin_values.append(''.join(bin_val))
        #Appending them to a list
        else:
            bin_values.append(bin_val)

    return bin_values


#Converting the decoded binary data into character form
def BinToStr(data):
    string = ""
    for bin_val in data:
        #Changing the binary value into integer and then to character
        char = chr(int(bin_val, 2))
        #appending the converting character to the variable
        string+=char
    
    return string


#Decoding the image to retrieve data or hidden info
def decode(source="output.png"):
    #Opening/Loading the image
    try:
        img = Image.open(source)
    except:
        return "Image not valid"
    #Getting pixel data from it and changing it into a list
    pixels = img.getdata()
    pixels = [list(pixel) for pixel in pixels]
    #passing pixel value to find the stored info
    info = [str(x).replace("9","") for x in ReadPixels(pixels)]

    return BinToStr(info)

#go through the pixels and find the hidden info
def ReadPixels(pixels):
    #initialising count variables
    NumOfChar = 1
    pix_count = 0
    hidden_bin_vals = []
    while NumOfChar>0:
        #if the first value is zero it will not being appended 
        hidden_bin_val = ["9"]
        for t in range(3):
            for i in range(3):
                #checking if there is any character remaining
                if t==2 and i==2:
                    if pixels[pix_count][i]%2 == 0:
                        NumOfChar+=1
                #checking the pixel is EVEN or ODD and accordingly appending
                # 0 for EVEN and 1 for ODD
                else:
                    if pixels[pix_count][i]%2 == 0:
                        hidden_bin_val.append("0")
                    else:
                        hidden_bin_val.append("1")
            
            pix_count+=1
        #appending to the final binary value list
        hidden_bin_vals.append(int(''.join(hidden_bin_val)))
        NumOfChar-=1
    
    #Returning the values
    return hidden_bin_vals
    
