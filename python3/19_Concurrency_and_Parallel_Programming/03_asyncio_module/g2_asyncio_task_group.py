import asyncio


async def example(num):
    print(f"Start {num}")
    await asyncio.sleep(num)
    print(f"End   {num}")

    return f"Finished {num}"


async def run_with_gather():
    tasks = []
    for num in range(1, 5):
        task = asyncio.create_task(example(num))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    print(f"{results =}")


asyncio.run(run_with_gather())


async def run_with_group():
    results = []
    async with asyncio.TaskGroup() as tg:
        for num in range(1, 5):
            task = tg.create_task(example(num))
            results.append(task)

    print([task.result() for task in results])


asyncio.run(run_with_group())
