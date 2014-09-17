from simpleinjector import InjectorConfiguration, inject


def one():
    return "xxx"


def two(value):
    assert(value == "xxx")
    InjectorConfiguration.post_ran = True

InjectorConfiguration.add_static_arg("static", "static")
InjectorConfiguration.add_runtime_arg("runtime", one, two)


class TestClass:

    @inject
    def test(self, static, runtime):
        assert(static == "static")
        assert(runtime == "xxx")

TestClass().test()

assert(InjectorConfiguration.post_ran)
