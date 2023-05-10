import replicate

# Zip file containing input images, hosted somewhere on the internet
zip_url = "https://elinmolander.github.io/elin-training-content.zip"

# Train the model
lora_url = replicate.run(
    "replicate/lora-training:65b3bb55-535e-4a7b-88e6-9b1663e99ec7",
    input={"instance_data": zip_url, "task": "style"}
)

https://replicate.delivery/pbxt/nJG5nVwdEyLWA1l8Tvd2dQ0qzVelNww6vRsGQmYjzHYRxjXIA/tmpuieea88oelin-training-contentzip.safetensors


# "replicate/lora-training:b2a308762e36ac48d16bfadc03a65493fe6e799f429f7941639a6acec5b276cc",