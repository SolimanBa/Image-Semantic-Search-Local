from transformers import AutoProcessor, AutoModelForCausalLM

model_name = "microsoft/Florence-2-base"

processor = AutoProcessor.from_pretrained(
    model_name,
    trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    trust_remote_code=True
)

print("Model downloaded successfully!")