from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class articolo(_message.Message):
    __slots__ = ("tipo", "id")
    TIPO_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    tipo: str
    id: int
    def __init__(self, tipo: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class msg_ack(_message.Message):
    __slots__ = ("ack",)
    ACK_FIELD_NUMBER: _ClassVar[int]
    ack: bool
    def __init__(self, ack: bool = ...) -> None: ...

class msg_preleva(_message.Message):
    __slots__ = ("tipo",)
    TIPO_FIELD_NUMBER: _ClassVar[int]
    tipo: str
    def __init__(self, tipo: _Optional[str] = ...) -> None: ...
