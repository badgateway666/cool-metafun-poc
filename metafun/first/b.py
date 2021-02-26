class foo_b:
    def __str__(self):
        return "foo-b-object!"

    def __call__(self, *args, **kwargs):
        print("foo-b-object was called")


class bar_b:
    def __str__(self):
        return "bar-b-object!"

    def __call__(self, *args, **kwargs):
        print("bar-b-object was called")
