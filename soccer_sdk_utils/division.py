from enum import Enum


class Division(Enum):
    # __order__ = "ALL DI DII DIII NAIA NJCAA"
    All = 0
    DI = 1
    DII = 2
    DIII = 3
    NAIA = 4
    NJCAA = 5

    def __repr__(self):
        return self

    def __str__(self):
        return self.name.lower()


def string_to_division(value: str) -> Division | None:
    if value is None:
        return None

    value = value.strip()
    value = value.lower()

    for current_division in Division:
        if current_division.name.lower() == value:
            return current_division

    return None


DivisionList = [Division.DI, Division.DII, Division.DIII, Division.NAIA, Division.NJCAA]


if __name__ == "__main__":
    division = Division.DI

    print(division)
    print(division.name)
    print(division.value)
    print(str(division))

    print(repr(division))
