#the objective of this script is to create a boosting algorithm
#in Julia
#this is based on the book ISLR
#next after doing this I should read Elements and apply the methods in there.

#we'll apply this boosting example in the Auto.csv dataset

using CSV
auto = CSV.read("Auto.csv")
first(auto,5)



#transform all string variables into numeric

#lets predict horsepower based on all other variables
y = auto.horsepower
y1 = map(x->tryparse(Float64,x),y)

t1 = map(x->typeof(x),y1)
t2 = map(x->x==Float64,t1)
freqtable(t2)

#clean database from strange cases
auto2 = auto[t2,:]

#just to see what is in "origin"
freqtable(auto2.origin)

#create label variable
v1 = auto2.horsepower
v2 = parse.(Float64,v1)


#create features matrix
X = copy(auto2)
select!(X,Not([:horsepower,:name]))
#delete!(X,[:horsepower,:name]) #<== deprecated
println(first(X,5))
X2 = convert(Matrix,X)

#1st step in gradient boosting algorithm
r = v2

#define λ, the learning rate paramenter
λ = 0.01

#define a dictionary to store models
𝔉 = Dict()

using DecisionTree
#look for "julia regression tree" in cookbook
model_tree = build_tree(r,X2,max_depth==1)
v2hat = apply_tree(model_tree,X2)

#update 𝔉
#𝔉 = 𝔉 + λ*v2hat

for i in 1:1000
  global r = map((x,y)->x-y, r, λ*v2hat)
  model_tree = build_tree(r,X2,max_depth==1)
  𝔉[i] = model_tree #add model into dictionary
  global v2hat = apply_tree(model_tree,X2)
end

𝔣2 = zeros(length(v2))
for i in 1:length(𝔉)
  𝔣 = 𝔉[i]
  out1 = apply_tree(𝔣,X2)
  global 𝔣2 = map((x,y)->x+y,𝔣2,out1)
end
𝔣3 = map(x->λ*x,𝔣2)
