from comfy_api.torch_helpers import set_torch_compile_wrapper
from .ray_patch_decorator import ray_patch


class RayTorchCompileModel:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ray_actors": ("RAY_ACTORS",),
                "backend": (["inductor", "cudagraphs"],),
            }
        }

    RETURN_TYPES = ("RAY_ACTORS",)
    RETURN_NAMES = ("ray_actors",)
    FUNCTION = "patch"
    CATEGORY = "Raylight/extra"

    @ray_patch
    def patch(self, model, backend):
        print(f"Compiler {backend} registered")
        m = model.clone()
        set_torch_compile_wrapper(model=m, backend=backend)
        return m


NODE_CLASS_MAPPINGS = {
    "RayTorchCompileModel": RayTorchCompileModel,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RayTorchCompileModel": "Torch Compile Model (Ray)",
}
