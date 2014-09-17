pysimpleinjector
================

An extremely simple framework-independent dependency injector.

Usage
-----

pysimpleinjector injects values into decorated methods based on argument names.
Supose your system has an instance of some class called ```SessionManager```
, which you injected intoseveral different arguments.

Instead of passing the instance all over the place and keeping dozens of
references, you can decorate methods that require that with ```@inject```:

    @inject
    def(self, arg0, arg1, arg2, session_manager)

Now you need to tell the injector what to inject as ```session_manager```.
To do this, simple configure the injector with you the value it should inject.
Injection is done simply based on argument names, so all you need to do is name
your argument the same in every decorated method. If a particular method does
not have an argument named ```session_manager``` it won't be injected.

    manager_instance = SessionManager(some, args)
    InjectorConfiguration.add_static_arg("session_manager", manager_instance)

Done!

You also have a different type of injectable values: runtime injectable values.
In this case, instead of defining a static value that will be injected to
decorated methods, you can pass functions that will return the value you need
injected. This way, you an, following the above example, pass a SessionFactory,
that would inject a different session each time.

    factory = SessionFactory(some, config, values)
    InjectorConfiguration.add_runtime_arg("session_manager", SessionFactory)

For more details, please check the docstring of ```InjectorConfiguration``` and
```@inject``` .

Copyright (c) 2014 Hugo Osvaldo Barrera <hugo@barrera.io>
