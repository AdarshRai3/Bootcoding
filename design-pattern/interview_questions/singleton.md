🏆 Top 10 Singleton Interview Questions
1. What is the Singleton design pattern?

Answer:

Ensures only one instance of a class exists in the program.

Provides a global access point to that instance.

Used for logging, configuration, DB connections.

2. How do you implement Singleton in Python?

Answer:

Naive way (not thread-safe): override __new__.

Thread-safe: metaclass with threading.Lock.

Async environment: factory with asyncio.Lock.

👉 Example (thread-safe):

import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

3. How do you implement Singleton in Go?

Answer:
Use sync.Once for thread-safe, lazy initialization.

var once sync.Once
var inst *Config

func GetConfig() *Config {
    once.Do(func() {
        inst = &Config{DBURL: "postgres://"}
    })
    return inst
}

4. Difference between Singleton and Global Variable?

Answer:

Global variable: can be reassigned, no lifecycle control.

Singleton: enforces one object creation, can ensure thread-safety, lazy init, and hide implementation details.

Singleton can also be extended with interfaces for mocking.

5. Is Singleton a creational or structural pattern?

Answer:

Creational pattern (controls how an object is created).

6. How do you make Singleton thread-safe?

Answer:

Python: use threading.Lock or functools.cache (internally locked).

Go: use sync.Once (guaranteed once execution).

7. What are the drawbacks of Singleton?

Answer:

Hidden dependencies (hard to test/mock).

Global state → tight coupling.

Hard to parallelize (esp. in multiprocessing).

Violates SRP (class handles lifecycle + logic).

8. How do you prevent Singleton from being cloned or copied?

Answer:

Python: override __copy__, __deepcopy__, and __reduce__ for pickle.

Go: no copy constructor, but avoid exposing struct fields for copying.

9. Can Singleton break in multiprocessing or distributed systems?

Answer:

Yes. Singleton ensures one instance per process, not across processes or machines.

In distributed systems, you’d need a service registry or coordination system (e.g., ZooKeeper, Consul, Redis lock).

10. When would you use Singleton in a real-world system?

Answer:
✅ Good:

DB connection pool

Logger

Configuration manager

Metrics/Telemetry client

❌ Bad:

Core business logic

Where multiple instances are natural (e.g., multiple users, multiple connections).

⚡ Bonus “Trick” Questions (sometimes asked at FAANG)

How do you reset Singleton for unit tests?

Python: clear _instances dict.

Go: expose ResetForTest() with build tag.

Difference between Singleton, Monostate (Borg), and Dependency Injection?

Singleton → one object.

Monostate → many objects sharing one state.

DI → don’t hard-code Singleton; pass dependencies explicitly.