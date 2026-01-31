from typing_extensions import TypedDict


class AgentState(TypedDict):
    input: str
    route: str
    response: str

