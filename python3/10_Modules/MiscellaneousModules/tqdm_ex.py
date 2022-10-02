from time import sleep

from tqdm import tqdm


def task():
    sleep(0.001)


for j in range(2000):
    print("\t", j, end="\r")
    task()


for _ in tqdm(range(2000)):
    task()


def work(n):
    for _ in range(n):
        task()
        yield


for _ in tqdm(work(2000)):
    pass

for _ in tqdm(work(2000), total=2000):
    pass

# for HTML 5 progress bar in jupyter notebook
#       from tqdm import tqdm_notebook as tqdm


k = 0
for _ in tqdm(range(20), desc="outer loop", leave=True):
    for _ in tqdm(range(10_000_000), desc="inner loop", leave=False):
        k += 100
