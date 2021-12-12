import os
# from PIL import Image
import hashlib
import json

exported_folder = r'E:\Photos\Exported\test flutter'
photos_folder = r'E:\Photos'
compacted_folder = r'E:\Photos\Exported\test flutter\compacted'

# basewidth = 300
# img = Image.open('fullsized_image.jpg')
# wpercent = (basewidth / float(img.size[0]))
# hsize = int((float(img.size[1]) * float(wpercent)))
# img = img.resize((basewidth, hsize), Image.ANTIALIAS)
# img.save('resized_image.jpg')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class Encodable:
    def from_dict(dict):
        raise NotImplementedError()
    def get_encodable_dict(self):
        return self.__dict__

    @classmethod
    def from_json(cls, json_text):
        return cls.from_dict(json.loads(json_text))

    def to_json(self):
        return json.dumps(self.__dict__)

class Photo_Data(Encodable):

    def __init__(self, file_path):
        self.file_path = file_path
        self.name = os.path.basename(file_path)
        self.checksum = 0

    def update_checksum(self):
        self.checksum = get_checksum(self.file_path)

    def from_dict(dict):
        photo_data = Photo_Data('')
        photo_data.__dict__.update(dict)
        return photo_data

class Map_List:
    dic = {}
    def register_value(self, key, vale):
        list = self.dic.get(key)
        if list is None:
            list = []
            self.dic[key] = list
        list.append(vale)

count = 0
def read_images(folder, map_list):
    global count
    # print(folder)
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        # print(file_path)
        if os.path.isdir(file_path):
            read_images(file_path, map_list)
        else:
            # print(filename,filename.endswith(".CR3"))
            # if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".CR3"):
            if filename.endswith(".CR3") or filename.endswith(".CR2") or filename.endswith(".jpg") or filename.endswith(".png"):
                photo_data = Photo_Data(file_path)
                map_list.register_value(filename, photo_data)
                # photo_data.update_checksum()
                # photo_data_json = photo_data.to_json()
                # photo_data_copy = Photo_Data.from_json(photo_data_json)
                print(file_path)
                count += 1
                # print(photo_data_json)
                # print(json.dumps(photo_data_copy.__dict__))
            else:
                continue

def resize_image():
    print('Hi')
    for filename in os.listdir(exported_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print(os.path.join(exported_folder, filename))
        else:
            continue

def get_checksum(file_name):
    md5_hash = hashlib.md5()
    a_file = open(file_name, "rb")
    content = a_file.read()
    a_file.close()
    md5_hash.update(content)
    return md5_hash.digest().hex()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # list = []
    photo_data = Photo_Data('')

    # list.append(photo_data)
    map_list = Map_List()
    # map_list.register_value('a name', 'a value')
    read_images('E:\Photos', map_list)
    print(count)
    print(len(map_list.dic))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

