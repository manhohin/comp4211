pretrained_main: weights of the pretrained model you need to loaded in the main tasks
bonus/k<i>_100ep: weights of the pretrained model trained with 100 epochs for different kernel sizes, i can be [3,5,7,11]
bonus/<typeofnorm>_100ep: weights of the pretrained model trained with 100 epochs for different normalizations, typeofnorm can be [layernorm, batchnorm, instancenorm, original] 

* original is the configuration described in the assignment trained with 100 epochs

You can load the weights by:
model.load_weights('<filedir>+<foldername>/<foldername>') e.g. model.load_weights('bonus/k3_100ep/k3_100ep')