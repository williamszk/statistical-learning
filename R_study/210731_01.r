
# Understanding Statistics using R
# chapter 2

# representativeness
# approximation as as we increase the number of coin tosses
# or samples that we collect

# relative frequency

# frequentist definition of probability
# the probability of an event is equal to the relative frequency
# as the number of samples increase
# this definition assumes that the relative frequency stabalizes
# as the number of trials increase


# 0.1 or 0.9 will have relative frequencies that stabilize faster than an event with
# probability close to 0.50

Probability = 0.5



rdu = function(n,k){
  # Arguments
  # n: sample size
  # k: max value
  sample(0:k,n,replace=T)
} 

set.seed(13579)
SampleFreqs = NULL
SampleSizes = seq(100,10000,10)
for (size in SampleSizes){
  sampleInstance = sample(0:1,size, replace=TRUE)
  experimentResult = mean(sampleInstance)
  SampleFreqs = c(SampleFreqs, experimentResult)
}

plot(SampleSizes, SampleFreqs,type = 'l')












