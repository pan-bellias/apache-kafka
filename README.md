# Apache Kafka - Python Temperature

## Kafka Docker Deployment
```bash
docker-compose up -d

# create topics my-topic-a and my-topic-b
docker exec kafka kafka-topics --bootstrap-server kafka:9092 --create --topic my-topic-a
docker exec kafka kafka-topics --bootstrap-server kafka:9092 --create --topic my-topic-b
```

### dotenv variables
```bash
cp .env.example .env
```
```nano
TOPIC_A='my-topic-a'
TOPIC_B='my-topic-b'
BOOTSTRAP_SERVER='localhost:9092'
```

## Kafka K8S Deployment
```bash
kubectl apply -f k8s
kubectl port-forward <KAFKA-POD-NAME> 9092 -n kafka

# create topics using:
kubectl exec --tty -i <KAFKA-POD-NAME> -n kafka -- opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic <TOPIC-NAME>
```

## Run Example
```bash
python3 -m venv .venv
```
and
```bash
source .venv/bin/activate
pip install -r requirements.txt
python consumer.py
```
in other shell run
```bash
source .venv/bin/activate
python producer-consumer.py
```
and in other shell run
```bash
source .venv/bin/activate
python producer.py
```
to see the magic!
