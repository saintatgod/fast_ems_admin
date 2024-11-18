from pydantic import BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

class CustomPhoneNumber(PhoneNumber):
    default_region_code = 'CN'
    default_country_code = 86

class SchemaBase(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

