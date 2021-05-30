from pylisk.main import hello_world


def test_hello_world(name='Python Guru'):
    greetings = hello_world(name)
    print(greetings)

