import filters

def main():
    filename = input("Enter the name image you want to edit: ")
    img = filters.load_img(filename)
    filters.save_img(img, "editedImage.jpeg")
    filteredImage = filters.obamacon(img)
    filters.show_img(filteredImage)



#MUST HAVE FOR PROGRAM TO WORK
if __name__ == "__main__":
    main()
