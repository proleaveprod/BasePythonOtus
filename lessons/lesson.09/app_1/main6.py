from users import (
    USERS_MAGIC_CONST,
    create,
    update,
    delete,
)

from products import create, update


def main():
    print("Hello main!")
    print("Users magic const:", USERS_MAGIC_CONST)
    bob = create("Bob")
    alice = create("Alice")

    update("Bob", email="bob@abc.com")

    delete("Alice")

    create("Smartphone")
    create("Laptop")
    update("Laptop", description="Lightest Laptop")


if __name__ == "__main__":
    main()