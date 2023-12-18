class InvalidNameError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidAgeError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class Person:
    _first_name: str
    _middle_name: str
    _last_name: str
    _age: int

    def __init__(self, first_name, middle_name, last_name, age):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age

    @property
    def first_name(self):
        return self._first_name

    @property
    def middle_name(self):
        return self._middle_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(f"Invalid age: {age}. Age should be a positive integer.")

        self._age = age

    def get_age(self):
        return self.age

    @first_name.setter
    def first_name(self, first_name):
        if first_name == "":
            raise InvalidNameError(f"Invalid name: {first_name}. Name should be a non-empty string.")

        self._first_name = first_name

    @middle_name.setter
    def middle_name(self, middle_name):
        if middle_name == "":
            raise InvalidNameError(f"Invalid text: {middle_name}. Name should be a non-empty string.")

        self._middle_name = middle_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name == "":
            raise InvalidNameError(f"Invalid text: {last_name}. Name should be a non-empty string.")

        self._last_name = last_name

    def birthday(self):
        self._age += 1


class InvalidIdError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class Employee(Person):
    _id: int

    def __init__(self, first_name, middle_name, last_name, age, id):
        super().__init__(first_name, middle_name, last_name, age)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if not isinstance(id, int) or 99999 < id < 1000000:
            raise InvalidIdError(f"Invalid age: {id}. Age should be a positive integer")

        self._id = id

    def get_level(self):
        number = self.id
        total = 0
        while number > 0:
            total += number % 10
            number /= 10

        return total % 7





    