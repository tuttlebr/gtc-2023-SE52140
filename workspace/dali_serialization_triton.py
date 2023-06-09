import nvidia.dali.fn as fn
import nvidia.dali.types as types
from nvidia.dali import pipeline_def

SAVE_AS = "/workspace/triton_models/facenet_preprocess/1/model.dali"


class FacenetPipeline:
    """Grayscale Image whose values in RGB channels are the same. 736 X 416 X 3
    Channel Ordering of the Input: NCHW, where N = Batch Size, C = number of
    channels (3), H = Height of images (416), W = Width of the images (736)
    Input scale: 1/255.0 Mean subtraction: None
    https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/facenet
    """

    def __init__(self):
        self.raw_image_tensor = fn.external_source(name="input_image_data")
        self.shapes = fn.peek_image_shape(self.raw_image_tensor)
        self.one_over_255 = 1 / 255.0

    def load_images(self):
        self.image_tensor = fn.decoders.image(
            self.raw_image_tensor, output_type=types.GRAY, device="mixed"
        )

    def color_space_conversion(self):
        self.image_tensor = fn.color_space_conversion(
            self.image_tensor, image_type=types.GRAY, output_type=types.RGB
        )

    def resize_images(self):
        self.image_tensor = fn.resize(
            self.image_tensor,
            resize_x=736,
            resize_y=416,
            interp_type=types.DALIInterpType.INTERP_LANCZOS3,
        )

    def transpose_images(self):
        self.image_tensor = fn.transpose(self.image_tensor, perm=[2, 0, 1])

    @pipeline_def(batch_size=32, num_threads=8)
    def facenet_reshape(self):
        self.load_images()
        self.color_space_conversion()
        self.resize_images()
        self.transpose_images()

        return self.image_tensor * self.one_over_255, self.shapes


if __name__ == "__main__":
    facenet_pipeline = FacenetPipeline()
    _ = facenet_pipeline.facenet_reshape().serialize(filename=SAVE_AS)
