import string
import random
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.digits,k=8))

@dataclass
class Student:
    name: str
    age: int
    student_id: str=field(default_factory=generate_id)

    def acquaintance(self, student: object) -> str:
        return f"{self.name} acquianted with {student.name}"