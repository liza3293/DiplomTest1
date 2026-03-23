import re
from typing import Literal
from pydantic import BaseModel, Field, model_validator


def is_camel_case(s: str) -> bool:
    return bool(re.match(r"^[a-z]+([A-Z][a-z0-9]+)*$", s))

def is_kebab_case(s: str) -> bool:
    return bool(re.match(r"^[a-z]+(-[a-z0-9]+)*$", s))

class OptionSpec(BaseModel):
    value: str = Field(..., min_length=1)
    label: str = Field(..., min_length=1)


class FieldSpec(BaseModel):
    key: str = Field(..., min_length=1)
    type: Literal["text", "select"]
    label: str = Field(..., min_length=1)
    required: bool = False
    placeholder: str | None = None
    options: list[OptionSpec] | None = None

    @model_validator(mode="after")
    def validate_field_logic(self):
        if self.type == "select" and not self.options:
            raise ValueError("Field with type 'select' must have non-empty options.")

        if self.type == "text" and self.options is not None:
            raise ValueError("Field with type 'text' must not contain options.")

        if not is_camel_case(self.key):
            raise ValueError(f"Field key '{self.key}' must be in camelCase.")

        return self


class SectionSpec(BaseModel):
    id: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    layout: Literal["one-column", "two-column"]
    fields: list[FieldSpec] = Field(..., min_length=1)

    @model_validator(mode="after")
    def validate_section(self):
        if not is_kebab_case(self.id):
            raise ValueError(f"Section id '{self.id}' must be in kebab-case (e.g. patient-identity).")

        return self