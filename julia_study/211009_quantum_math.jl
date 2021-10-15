# https://www.youtube.com/watch?v=3RGEYYJmMtU&ab_channel=Josh%27sChannel

# the qubit state is defined by a vector of complex numbers

a1 = 1
b2 = 1
a2 = 1
b2 = 1

complex_1 = a1 + b2*im
complex_2 = a2 + b2*im

qbit_state = [complex_1, complex_2]

typeof(qbit_state)

function get_magnitude_complex_number(complex_number)
    # complex_number = 2 + 3im
    complex_number

    result =
    √(
    real(complex_number)^2 +
    imag(complex_number)^2)

    return result
end


get_magnitude_complex_number(complex_1)

get_magnitude_complex_number(2 + 3im)
