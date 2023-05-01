#==============================================================================
# this test is running on a ubuntu container inside my thinkpad 
# let's uses gunicorn in here
# this command will start the gunicorn server
gunicorn --workers=5 --bind 0.0.0.0:5000 wsgi:app

# run the autocannon to measure performance
autocannon -c 100 -d 5 -p 10 http://127.0.0.1:5000

# what -c means? 
# it means concurrent, there are 100 clients making the request at the same time
# -d 5 : means the durantion of the test in seconds
# -p 10 : means that autocannon will make 10 requests at the same time 

#==============================================================================
# comparing with and without gunicorn
# using gunicorn clearly improve the performance of the application
# the throughput and req/s increase it is almost 100 times higher
# I wonder how changing the number of workers/or cores change this number
# req/s increase 800 times 
# although the measured latency is higher using gunicorn

# ----------------------- #
# the median latency is 2466ms (more than 2 seconds)
# compared to the last run test_230501_01
# the median latency was 189ms
# the latency using gunicorn was much worse
# 
# let's compare throughput (bytes/s)
# compare median
# this:     341 kB
# previous: 0B , the debug server can only handle 1 connection...
# 
# the average
# this:     313 kB
# previous: 3.7 kB
# using gunicorn makes the through put increase
# it is aroud 90 times higher

# let's compare req/s
# compare avg
# this:     1923 req/s
# previous: 20 req/s
# with gunicorn req/s increase 800 times

# let's compare number of errors
# this:     851
# previous: NA
# strange why there are no information about erros in the previous test?

#==============================================================================
# We could try to increase the number of workers to see what happens
# We could try to use a machine with more cores 
# What else could we try to do?
#==============================================================================
# 0 http://127.0.0.1:5000
# Running 5s test @ http://127.0.0.1:5000
# 100 connections with 10 pipelining factor

# ┌─────────┬────────┬─────────┬─────────┬─────────┬───────────┬────────────┬─────────┐
# │ Stat    │ 2.5%   │ 50%     │ 97.5%   │ 99%     │ Avg       │ Stdev      │ Max     │
# ├─────────┼────────┼─────────┼─────────┼─────────┼───────────┼────────────┼─────────┤
# │ Latency │ 252 ms │ 2466 ms │ 4347 ms │ 4408 ms │ 2429.9 ms │ 1226.49 ms │ 4509 ms │
# └─────────┴────────┴─────────┴─────────┴─────────┴───────────┴────────────┴─────────┘
# ┌───────────┬────────┬────────┬────────┬────────┬────────┬────────┬────────┐
# │ Stat      │ 1%     │ 2.5%   │ 50%    │ 97.5%  │ Avg    │ Stdev  │ Min    │
# ├───────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┤
# │ Req/Sec   │ 1480   │ 1480   │ 2091   │ 2239   │ 1923   │ 307.09 │ 1480   │
# ├───────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┤
# │ Bytes/Sec │ 241 kB │ 241 kB │ 341 kB │ 365 kB │ 313 kB │ 50 kB  │ 241 kB │
# └───────────┴────────┴────────┴────────┴────────┴────────┴────────┴────────┘

# Req/Bytes counts sampled once per second.
# # of samples: 5

# 107k requests in 5.09s, 1.57 MB read
# 851 errors (0 timeouts)

#==============================================================================
# let's do another run

# 0 http://127.0.0.1:5000
# Running 5s test @ http://127.0.0.1:5000
# 100 connections with 10 pipelining factor

# ┌─────────┬────────┬─────────┬─────────┬─────────┬────────────┬────────────┬─────────┐
# │ Stat    │ 2.5%   │ 50%     │ 97.5%   │ 99%     │ Avg        │ Stdev      │ Max     │
# ├─────────┼────────┼─────────┼─────────┼─────────┼────────────┼────────────┼─────────┤
# │ Latency │ 310 ms │ 2487 ms │ 4300 ms │ 4400 ms │ 2413.31 ms │ 1188.65 ms │ 4483 ms │
# └─────────┴────────┴─────────┴─────────┴─────────┴────────────┴────────────┴─────────┘
# ┌───────────┬────────┬────────┬────────┬────────┬────────┬─────────┬────────┐
# │ Stat      │ 1%     │ 2.5%   │ 50%    │ 97.5%  │ Avg    │ Stdev   │ Min    │
# ├───────────┼────────┼────────┼────────┼────────┼────────┼─────────┼────────┤
# │ Req/Sec   │ 1233   │ 1233   │ 1793   │ 1957   │ 1715.8 │ 265.64  │ 1233   │
# ├───────────┼────────┼────────┼────────┼────────┼────────┼─────────┼────────┤
# │ Bytes/Sec │ 201 kB │ 201 kB │ 292 kB │ 319 kB │ 280 kB │ 43.3 kB │ 201 kB │
# └───────────┴────────┴────────┴────────┴────────┴────────┴─────────┴────────┘

# Req/Bytes counts sampled once per second.
# # of samples: 5

# 95k requests in 5.12s, 1.4 MB read
# 787 errors (0 timeouts)

