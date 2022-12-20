from pydantic import BaseModel, StrictStr

class ProducerResponse(BaseModel):
    name: StrictStr
    lastname: StrictStr
    status: StrictStr = ""
    topic: StrictStr


class ProducerMessage(BaseModel):
    name: StrictStr
    lastname: StrictStr = ""
    status: StrictStr = ""