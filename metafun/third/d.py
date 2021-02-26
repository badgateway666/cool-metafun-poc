class foo_d:
    def __str__(self):
        return "foo-d-object!"

    def __call__(self, *args, **kwargs):
        print("foo-d-object was called")


class bar_d:
    def __str__(self):
        return "bar-d-object!"

    def __call__(self, *args, **kwargs):
        print("bar-d-object was called")
