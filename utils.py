from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# Load the Ghibli-style diffusion model
pipe = StableDiffusionPipeline.from_pretrained("Yntec/GhibliDiffusion", torch_dtype=torch.float32)
pipe = pipe.to("cpu")
pipe.enable_attention_slicing()

def generate_ghibli_image(prompt, height=512, width=512, num_inference_steps=45):
    final_prompt = f"{prompt} in Ghibli studio themed style"
    result = pipe(final_prompt, num_inference_steps=num_inference_steps, height=height, width=width)
    return result.images[0]



def test():
    prompt = input("Enter prompt: ")
    image = generate_ghibli_image(prompt)
    image.save("ghibli_output.png")

if __name__ == "__main__":
    test()