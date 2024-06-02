from options import TestOptions
import data
import models
import os
from evaluation import GroupEvaluator


# os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# os.environ["TORCH_CUDA_ARCH_LIST"] = "8.6"  # Replace with your GPU's compute capability
# os.environ["NVCCFLAGS"] = "-allow-unsupported-compiler"

# opt = TestOptions().parse()
# dataset = data.create_dataset(opt)
# evaluators = GroupEvaluator(opt)

# model = models.create_model(opt)

# evaluators.evaluate(model, dataset, opt.resume_iter)


def get_transform(opt):
    def transform(x):
        # Example transformation logic
        return x

    return transform


if __name__ == "__main__":
    os.environ["TORCH_CUDA_ARCH_LIST"] = (
        "8.6"  # Replace with your GPU's compute capability
    )
    os.environ["NVCCFLAGS"] = "-allow-unsupported-compiler"

    opt = TestOptions().parse()
    opt.transform = get_transform(opt)  # Use the transform function
    dataset = data.create_dataset(opt)
    dataset_size = len(dataset)
    print("Number of training images = %d" % dataset_size)

    model = models.create_model(opt)
    model.setup(opt)
    model.eval()
