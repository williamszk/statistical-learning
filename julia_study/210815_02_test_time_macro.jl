function dummy_function()
    result = 0.0
    n = 1_000_000
    for i in 1:n
        result += sin(rand())
    end
    return result
end

show(dummy_function())
