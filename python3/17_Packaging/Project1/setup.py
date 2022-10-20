import setuptools

setuptools.setup(
    name="hello_world",
    version="0.1.0",
    entry_points={
        "console_scripts": [
            "hello_world=hello_world:say_hi",
        ]
    },
)
