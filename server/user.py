from enum import Enum

class PartyEnum(Enum):
    REPUBLICAN = "republican"
    DEMOCRAT = "democrat"


class PoliticalUser:
    def __init__(self, party_name: PartyEnum, country="United States of America", state=None, county=None):
        self.party_name = party_name
        self.state, self.county = state, county
        self.country = country




def build_user_prompt(user: PoliticalUser):
    prompt = f"I am someone from the party {user.party_name}."
    if user.country:
        prompt += f"You are from the country {user.country}"
    if user.state:
        prompt += f"I belong to the state {user.state}."
    if user.country:
        prompt += f"And I look after the county - {user.country}."

    return prompt