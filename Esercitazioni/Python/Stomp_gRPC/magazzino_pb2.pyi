from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class msg_articolo(_message.Message):
    __slots__ = ("id", "prod")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROD_FIELD_NUMBER: _ClassVar[int]
    id: str
    prod: str
    def __init__(self, id: _Optional[str] = ..., prod: _Optional[str] = ...) -> None: ...

class msg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class msg_ack(_message.Message):
    __slots__ = ("ack",)
    ACK_FIELD_NUMBER: _ClassVar[int]
    ack: str
    def __init__(self, ack: _Optional[str] = ...) -> None: ...
