class foo_e:
    def __str__(self):
        return "foo-e-object!"

    def __call__(self, *args, **kwargs):
        print("foo-e-object was called")


class bar_e:
    def __str__(self):
        return "bar-e-object!"

    def __call__(self, *args, **kwargs):
        print("bar-e-object was called")
