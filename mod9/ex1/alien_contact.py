from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                'Contact ID must start with "AC" (Alien Contact)')
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError(
                'Physical contact reports must be verified')
        if (self.contact_type == ContactType.TELEPATHIC
           and self.witness_count < 3):
            raise ValueError(
                'Telepathic contact requires at least 3 witnesses'
            )
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                'Strong signals (> 7.0) should include received messages'
            )
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    date = "2026-11-27 01:31:00"
    ac = AlienContact(
        contact_id="AC_2024_001",
        contact_type=ContactType.RADIO,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="'Greetings from Zeta Reticuli'",
        timestamp=date)  # type: ignore[arg-type]
    print("Valid contact report:")
    print(f"ID: {ac.contact_id}")
    print(f"Type: {ac.contact_type}")
    print(f"Location: {ac.location}")
    print(f"Signal: {ac.signal_strength}")
    print(f"Duration: {ac.duration_minutes}")
    print(f"Witnesses: {ac.witness_count}")
    print(f"Message: {ac.message_received}")
    print()
    print("======================================")
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="'Greetings from Zeta Reticuli'",
            timestamp=date)  # type: ignore[arg-type]
    except ValidationError as e:
        print(e.errors()[0]['ctx']['error'])


if __name__ == "__main__":
    main()
