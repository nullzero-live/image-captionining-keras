#Image captioning using a Encoder-Decoder with Keras

#Load captions
def load_doc(filename):
    with open(filename) as file:
        text = file.readlines()
        return text

filename = "Flickr8k_text/Flickr8k.token.txt" ### UPDATE THIS
text = load_doc(filename)
for line in text[:10]:
    print(line,end='')
    
    
#Mapping image with captions using dictionary
def image_to_captions(text):
    hash_map = {}
    for line in text:
        token = line.split()

