import os

path = os.path.join('data','test','tan_spot_test')

count = 0
for i in os.listdir(path):
    src_path = os.path.join(path,i)
    os.rename(src=src_path,dst=os.path.join(path,f'tan_spot_test_{count}.png'))
    count = count + 1