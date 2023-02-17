#Image captioning using a Encoder-Decoder with Keras
#https://iq.opengenus.org/image-captioning-using-keras/

#Load captions
def load_doc(filename):
    with open(filename) as file:
        text = file.readlines()
        return text

filename = "Flickr8k_text/Flickr8k.token.txt" ### UPDATE THIS
text = load_doc(filename)
    
#Mapping image with captions using dictionary
def image_to_captions(text):
    hash_map = {}
    for line in text:
        token = line.split()
        image_id = token[0].split('.')[0] # separating with '.' to extract image id (removing .jpg)
        image_caption = ' '.join(token[1: ])
    
    #Add imageID and Image caption to hash map
        if(image_id not in hash_map):
                hash_map[image_id] = [image_caption]
        else:
            hash_map[image_id].append(image_caption)
        
    return hash_map

#Create a map img to captions object
map_img_to_captions = image_to_captions(text)

def preprocess(map_img_to_captions):
    preprocessed_captions = []
    for key in map_img_to_captions.keys():
        for idx in range(len(map_img_to_captions[key])):
            tokens = map_img_to_captions[key][idx].split()
            tokens = [token.lower() for token in tokens if len(token)>1 if token.isalpha()]
            map_img_to_captions[key][idx] = ' '.join(tokens)
            
    return map_img_to_captions

preprocessed_map = preprocess(map_img_to_captions)

def create_vocabulary(preprocessed_map):
    vocabulary = set()
    for img_captions in preprocessed_map.values(): # list of 5 captions for each image
        for caption in img_captions:
            for token in caption.split():
                vocabulary.add(token)    
    return print(type(vocabulary))

