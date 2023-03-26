import asyncio
import csv

from aiohttp import web


def create_dummy_file():
    with open("data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "email", "phone"])
        writer.writerow(["1", "John Doe", "john.doe@example.com", "555-1234"])
        writer.writerow(["2", "Jane Smith", "jane.smith@example.com", "555-5678"])


async def read_data():
    with open("data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
        return data


async def create_data(request):
    data = await request.post()
    new_row = [data["id"], data["name"], data["email"], data["phone"]]
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_row)
    return web.Response(text=f"Created row with id {data['id']}")


async def update_data(request):
    data = await request.post()
    new_row = [data["id"], data["name"], data["email"], data["phone"]]
    rows = []
    with open("data.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == data["id"]:
                rows.append(new_row)
            else:
                rows.append(row)
    with open("data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    return web.Response(text=f"Updated row with id {data['id']}")


async def delete_data(request):
    id = request.match_info["id"]
    rows = []
    with open("data.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != id:
                rows.append(row)
    with open("data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    return web.Response(text=f"Deleted row with id {id}")


async def handle_data(request):
    data = await read_data()
    return web.json_response(data)


async def main():
    app = web.Application()
    app.add_routes(
        [
            web.get("/", lambda _: web.Response(text="Hello, world!")),
            web.get("/data", handle_data),
            web.post("/data", create_data),
            web.put("/data", update_data),
            web.delete("/data/{id}", delete_data),
        ]
    )
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8080)
    await site.start()


if __name__ == "__main__":
    # create_dummy_file()
    asyncio.run(main())
