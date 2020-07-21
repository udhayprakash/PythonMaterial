from time import sleep


def task():
    sleep(.001)


for j in range(2000):
    print('\t', j, end='\r')
    task()

from tqdm import tqdm

for j in tqdm(range(2000)):
    task()


def work(n):
    for j in range(n):
        task()
        yield


for i in tqdm(work(2000)):
    pass

for i in tqdm(work(2000), total=2000):
    pass

# for HTML 5 progress bar in jupyter notebook
#       from tqdm import tqdm_notebook as tqdm
