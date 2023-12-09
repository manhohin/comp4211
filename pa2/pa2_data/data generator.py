def gen_random_sequence():
    ''' randomly generate a sequence of a digit'''
    size = 64 - 28
    x, y, theta = random.random(), random.random(), random.random() * 2 * np.pi
    velocity_y, velocity_x = np.sin(theta), np.cos(theta) 
    seq_x, seq_y = np.zeros(20), np.zeros(20)

    for i in range(20):
        y += 0.1*velocity_y
        x += 0.1*velocity_x 

        if x <= 0:
            x = 0
            velocity_x = -velocity_x
        if x >= 1.0:
            x = 1.0
            velocity_x = -velocity_x
        if y <= 0:
            y = 0
            velocity_y = -velocity_y
        if y >= 1.0:
            y = 1.0
            velocity_y = -velocity_y
        seq_x[i], seq_y[i] = x, y

    # Scale to the size.
    seq_x = (size * seq_x).astype(np.int32)
    seq_y = (size * seq_y).astype(np.int32)
    return seq_y, seq_x

def random_mmnist():
    ''' generate frames of moving mnist. '''
    data = np.zeros((20, 64, 64), dtype=np.float32) # 10 input + 10 groundtruth = 20
    for n in range(2):
        seq_y, seq_x = gen_random_sequence()
        idx = random.randint(0, mnist_train_im.shape[0] - 1)
        mnist_image = mnist_train_im[idx]
        for i in range(20):
            # put the 2 moving digits into "data"
            data[i, seq_y[i]:seq_y[i]+28, seq_x[i]:seq_x[i]+28] = np.maximum(data[i, seq_y[i]:seq_y[i]+28, seq_x[i]:seq_x[i]+28], mnist_image)
    return data