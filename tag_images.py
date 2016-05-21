import os

base_path = 'Kendall_Square_datasets/Kendall_Square_'

def create_metadata():
    data = []
    for label in ['sunny', 'cloudy']:
        file_path = './{}{}/'.format(base_path, label)
        files = os.listdir(file_path)

        for img in files:
            data.append((file_path + img, label))
    return data


if __name__ == '__main__':
    data = create_metadata()
    for i in data:
        print(i)