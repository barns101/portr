from pydantic import BaseModel

from portr_admin.models.user import Role


class GithubUserSchema(BaseModel):
    github_avatar_url: str


class UserSchema(BaseModel):
    email: str
    first_name: str | None
    last_name: str | None
    is_superuser: bool


class UserSchemaForCurrentUser(UserSchema):
    github_user: GithubUserSchema | None


class TeamUserSchemaForCurrentUser(BaseModel):
    id: int
    secret_key: str
    role: Role

    user: UserSchemaForCurrentUser


class TeamUserSchemaForTeam(BaseModel):
    id: int
    role: Role

    user: UserSchemaForCurrentUser


class TeamUserSchemaForConnection(BaseModel):
    id: int

    user: UserSchema


class UserUpdateSchema(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
