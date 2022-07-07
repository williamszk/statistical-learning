import requests
from bs4 import BeautifulSoup
from time import sleep

def fetch_raw(recipe_url):
    html = None
    print('Processing..{}'.format(recipe_url))
    try:
        r = requests.get(recipe_url, headers=headers)
        if r.status_code == 200:
            # print(r.text)
            html = r.text
    except Exception as ex:
        print('Exception while accessing raw html')
        print(str(ex))
    finally:
        return html.strip()


def get_recipes():
    recipies = []
    salad_url = 'https://www.allrecipes.com/recipes/96/salad/'
    url = 'https://www.allrecipes.com/recipes/96/salad/'
    print('Accessing list')

    try:
        r = requests.get(salad_url, headers=headers)
        # print(r.status_code)
        if r.status_code == 200:
            html = r.text
            soup: BeautifulSoup = BeautifulSoup(html, 'lxml')

            # send print to a file
            with open("soup_output.xml", "w") as f:
                print(f"{soup = }", file=f)
            # links = soup.select('.fixed-recipe-card__h3 a')
            # links = soup.select('.card__titleLink a')
            links = soup.select('.child-link ')
            
            idx = 0
            if len(links) == 0:
                print("Warning: the links is an empty list.")
            else:
                print(f"The len of links is: {len(links)}")
            for link in links:
                sleep(2)
                recipe = fetch_raw(link['href'])
                recipies.append(recipe)
                idx += 1
                if idx > 2:
                    # here we control the quantity of links
                    # that we will process
                    break
    except Exception as ex:
        print('Exception in get_recipes')
        print(str(ex))
    finally:
        return recipies


def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    # https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html
    # https://kafka-python.readthedocs.io/en/master/usage.html
    from kafka import KafkaProducer
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer
    


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Pragma': 'no-cache'
    }
    all_recipes = get_recipes()
    if len(all_recipes) > 0:
        kafka_producer = connect_kafka_producer()
        for recipe in all_recipes:
            publish_message(kafka_producer, 'raw_recipes', 'raw', recipe.strip())
        if kafka_producer is not None:
            kafka_producer.close()

# Accessing list
# Processing..https://www.allrecipes.com/recipes/1310/breakfast-and-brunch/eggs/breakfast-burritos/
# Processing..https://www.allrecipes.com/recipes/144/breakfast-and-brunch/breakfast-casseroles/
# Processing..https://www.allrecipes.com/recipes/147/breakfast-and-brunch/crepes/
# Message published successfully.
# Message published successfully.
# Message published successfully.

# start the cli consumer to see the messages passed
"""
bin/kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic raw_recipes --from-beginning

# Note that here we need pass the correct name of the topic
"""


