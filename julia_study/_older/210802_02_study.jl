
# initialize several variables
a = b = c = 4

n, m = 1, 2

area = (r = 3; π*r^2)

x = begin
        a = 2
        b = 3
        a + b
    end

body_temp = 38.5

if body_temp > 38
        println("this person has fever")
elseif 35 < body_temp <= 37
        println("this person has normal temperature")
else
        println("this person has hypothermia")
end

n = 10; m = 15
# max =   if n > m   n
#         else       m
#         end

# max = n > m ? n : m
# the above does not work
# it does not work because max is a reserved keyword


# https://discourse.julialang.org/t/style-question-ternary-operator-or-short-circuit-operator-or-if-end/34224

# how to assign in a ternary fassion?
a = -20
a < 0 && (a=0)

a = -20
a = max(0, a)

a = -20
a < 0 ? a = 0 : nothing

n = 10; m = 15
# below are two ways to do the same thing
n > m ? max1 = 10 : max1 = m
max1 = (n > m ? n : m)
# ternary operator

year = 2016
while year <= 2050
        println("increase year")
        year += 1
end


year = 2016
while year <= 2050
        println("increase year")
        year += 1
        if year == 2047
                println("reached 2047")
                break
        end
end

blood_groups = ["A","B","AB","O"]

for blg in blood_groups
        print("$blg / ")
end

for (ix, blg) in enumerate(blood_groups)
        println("Blood-group no. $ix is $blg")
end

for i in 1:5
        print("$i - ")
end


# types of Exceptions in Julia

blood_groups = ["A","B","AB","O"]
code = "X"

# throw a specific error type
if code in blood_groups
        println("we have a suplly of this blood")
else
        throw(DomainError("- atention this blood group does not exist!"))
        # throw(DomainError)
end

# a generic error
if code in blood_groups
        println("we have a suplly of this blood")
else
        error("blood group unknown!")
end

# warn
if code in blood_groups
        println("we have a suplly of this blood")
else
        @warn("blood group unknown!")
end


# async
z = @async 26*78
println("In the meantime, I calculate other things!")
# println(consume(z))
# consume is deprecated

# how to deal with channels in Julia
# and async functions
# how to create data in a channel
# how to consume data from a channel

channel = Channel{Int}(1)
@async begin
                output = 26 * 78
                put!(channel, output)
        end
close(channel)
println(channel.data)
for x in channel println(x) end

# a tutorial about async and channel
# https://discourse.julialang.org/t/how-to-replace-consume-and-produce-with-channels/5125/4

chnl = Channel{Int}(1)
@async for i=1:10 put!(chnl, i) end
chnl.data

take!(chnl)
chnl.data

# for x in chnl println(x) end

chnl = Channel{Int}(1)
@async begin for i=1:10 put!(chnl, i) end; close(chnl) end
for x in chnl println(x) end

# ----------------------------------
# try and catch in Julia

try
        open("test.txt")
catch ex
        showerror(stdout, ex)
        println("")
end
println("I recovered from the exception")


# tasks
# asynchronous
