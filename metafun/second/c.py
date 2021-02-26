class foo_c:
    def __str__(self):
        return "foo-c-object!"

    def __call__(self, *args, **kwargs):
        print("foo-c-object was called")


class bar_c:
    def __str__(self):
        return "bar-c-object!"

    def __call__(self, *args, **kwargs):
        print("bar-c-object was called")