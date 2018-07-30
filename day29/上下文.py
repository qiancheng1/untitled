class Foo:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("1")
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print("exit")

with Foo("a.txt") as f:
    print(f)
    print(f.name)
