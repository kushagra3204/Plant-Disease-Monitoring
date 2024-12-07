import os

PATH = os.path.join('data')
COUNT = 0

if __name__ == '__main__':
    # For Arranging the data in the correct format (will be easier to map & store in labels.csv)
    for test_or_train in os.listdir(PATH):
        class_path = os.path.join(PATH,test_or_train)
        for individual_class in os.listdir(class_path):
            image_path = os.path.join(class_path,individual_class)
            print(individual_class)
            for image in os.listdir(image_path):
                img_path = os.path.join(image_path,image)
                individual_class = individual_class.replace(' ', '_').lower()
                os.rename(src=img_path,dst=os.path.join(image_path,f'{individual_class}_{COUNT}.png'))
                COUNT = COUNT + 1
            COUNT = 0