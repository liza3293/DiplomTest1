from models import SectionSpec

bad_example = {
    "id": "patient-identity",
    "title": "Patient identity",
    "layout": "two-column",
    "fields": [
        {
            "key": "gender",
            "type": "select",
            "label": "Gender",
            "required": True
        }
    ]
}

section = SectionSpec(**bad_example)
print(section)