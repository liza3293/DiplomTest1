from models import SectionSpec

example = {
    "id": "patient-identity",
    "title": "Patient identity",
    "layout": "two-column",
    "fields": [
        {
            "key": "patientId",
            "type": "text",
            "label": "Patient ID",
            "required": True,
            "placeholder": "e.g. P-00123"
        },
        {
            "key": "externalId",
            "type": "text",
            "label": "External ID",
            "placeholder": "Hospital / registry ID"
        },
        {
            "key": "gender",
            "type": "select",
            "label": "Gender",
            "required": True,
            "options": [
                {"value": "male", "label": "Male"},
                {"value": "female", "label": "Female"},
                {"value": "other", "label": "Other"}
            ]
        }
    ]
}

section = SectionSpec(**example)

print("Python object:")
print(section)

print("\nJSON output:")
print(section.model_dump_json(indent=2, exclude_none=True, ensure_ascii=False))