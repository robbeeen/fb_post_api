from dataclasses import dataclass


@dataclass
class UserAuthTokensDTO:
    user_id: str
    access_token: str
    refresh_token: str
    expires_in: int = None


@dataclass
class TokensDTO:
    access_token: str
    refresh_token: str
    expires_in: int


@dataclass()
class UserDto:
    name: str
    user_id: int
    profile_pic: str
