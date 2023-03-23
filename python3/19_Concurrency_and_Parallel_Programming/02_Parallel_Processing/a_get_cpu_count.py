import multiprocessing as mp

result = """There are {} processors, in number, in this \
          computer""".format(
    mp.cpu_count()
)
print(result)

print(dir(mp))

print(mp.current_process())
