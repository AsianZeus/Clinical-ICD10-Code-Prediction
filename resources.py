from transformers import AutoTokenizer, BertForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("AkshatSurolia/ICD-10-Code-Prediction")
model = BertForSequenceClassification.from_pretrained("AkshatSurolia/ICD-10-Code-Prediction")
config = model.config