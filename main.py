class Airport:
    def __init__(self):
        self.permission = set()
        self.landed = set()
        self.circling = []
        self.take_off = set()

    def inv(self):
        return self.landed.issubset(self.permission) \
               and all(elem in self.permission for elem in self.circling) \
               and not any(elem in self.landed for elem in self.circling) \
               and self.is_unique(self.circling)

    def is_unique(self, seq_in):
        return all(seq_in.index(seq_in[i]) == i for i in range(len(seq_in)))

    def get_permission(self):
        return self.permission

    def get_landed(self):
        return self.landed

    def get_circling(self):
        return self.circling

    def give_permission(self, craft_in):
        assert craft_in not in self.permission
        self.permission.add(craft_in)
        assert self.inv()

    def allow_to_circle(self, craft_in):
        if craft_in in self.permission and craft_in not in self.landed and craft_in not in self.circling:
            self.circling.append(craft_in)
            assert self.inv()
        elif craft_in not in self.permission:
            print("Kindly give permission first for aircraft", craft_in)

    def record_landing(self):
        assert self.circling
        landed_aircraft = self.circling.pop(0)
        self.landed.add(landed_aircraft)
        assert self.inv()

    def record_take_off(self, craft_in):
        if craft_in not in self.permission:
            print("Kindly give permission first to aircraft", craft_in)
        elif craft_in in self.circling:
            print("Aircraft", craft_in, "can't take off, it's in circling")
        elif craft_in in self.landed:
            self.landed.remove(craft_in)
            self.permission.remove(craft_in)
            self.take_off.add(craft_in)
            assert self.inv()
            print("Take off recorded for", craft_in)

    def number_waiting(self):
        return len(self.permission.difference(self.landed))

    def __str__(self):
        return "Permission: {}\nCircling: {}\nLanded: {}".format(self.permission, self.circling, self.landed)


def main():
    airport = Airport()

    while True:
        print("\nAirport Management System")
        print("1. Give Permission")
        print("2. Allow to Circle")
        print("3. Record Landing")
        print("4. Record Take Off")
        print("5. View Airport Status")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            craft_in = input("Enter aircraft you want to give permission to: ")
            airport.give_permission(craft_in)
            print("Permission granted to", craft_in)

        elif choice == '2':
            craft_in = input("Enter aircraft you want to allow to circle: ")
            airport.allow_to_circle(craft_in)

        elif choice == '3':
            airport.record_landing()
            print("Landing recorded")

        elif choice == '4':
            craft_in = input("Enter aircraft you want to record take off for: ")
            airport.record_take_off(craft_in)

        elif choice == '5':
            print("\nAirport Status:")
            print(airport)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
