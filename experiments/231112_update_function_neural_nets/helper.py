def error_pred_real(pred_vec, real_vec):
    error_vec = []
    for pred, real in zip(pred_vec, real_vec):
        error = real - pred
        error_vec.append(error)

    return error_vec


def step_function(y):
    if y >= 1:
        return 1
    else:
        return 0


def predictions(x_inputs, weights):
    if len(x_inputs) != len(weights):
        raise Exception(
            f"Length difference problem '{len(x_inputs)=}' and '{len(weights)}='"
        )
    # weights = [0,0]
    # y = x1*weights[0] + x2*weights[1]
    y = sum([x * w for x, w in zip(x_inputs, weights)])

    # activation function
    # now is a step function
    y1 = step_function(y)

    return y1


def update(weight_n, learning_rate, input_value, error):
    return weight_n + learning_rate * input_value * error
