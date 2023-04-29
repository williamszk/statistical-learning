
#==============================================================================
filename=curl_test_$(date +%Y-%m-%d_%H-%M-%S).txt
touch $filename

for i in {1..100}
do
    curl -s -w '%{time_total}s\n' -o . http://localhost:5000 >> $filename
done

#==============================================================================