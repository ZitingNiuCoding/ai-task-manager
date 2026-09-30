from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict

# Pydantic Schema。Pydantic = 用 Python 类来定义数据结构，并自动校验数据是否符合要求。
class TaskCreate(BaseModel):   # 规定：API 接收到的数据，应该长什么样
    title: str
    completed: bool = False
    description: str | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None
    description: str | None = None


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)  # 你拿到的数据不一定是 dict，也可能是一个 ORM 对象，请允许通过“属性”读取字段。

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
    user_id: int
    description: str | None

    model_config = ConfigDict(from_attributes=True)