class foo_a:
    def __str__(self):
        return "foo-a-object!"

    def __call__(self, *args, **kwargs):
        print("foo-a-object was called")


class bar_a:
    def __str__(self):
        return "bar-a-object!"

    def __call__(self, *args, **kwargs):
        print("bar-a-object was called")
