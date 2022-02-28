from resources import config, tokenizer, model
from pydantic import BaseModel

class Description(BaseModel):
    description: str

def get_code(text):
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    codes = [config.id2label[ids] for ids in output.logits.detach().cpu().numpy()[
        0].argsort()[::-1][:5]]
    return codes
