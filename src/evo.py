import transformers

# config = transformers.AutoConfig.from_pretrained("arcinstitute/evo2_1b_base", trust_remote_code=True)
# model = transformers.AutoModel.from_pretrained("arcinstitute/evo2_1b_base", config=config, trust_remote_code=True)
# print(model)

"""
This doesn't work. Evo2 is a custom model that seems to require e.g. NVIDIA GPUs that support Transformer Engine FP8,
Vortex inference, etc. Getting it to work locally would be cool, but I'm moving this to a lower priority while the RNA
competition is still active. Switching to a notebook environment for now.
"""