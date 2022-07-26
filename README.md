# Apache Kafka - Python Example

## Kafka Deployment using Helm charts

### Port forward
```bash
kubectl port-forward svc/kafka 9092
```

## Run Example
```bash
python3 -m venv .venv
```
and
```bash
source .venv/bin/activate
pip install -r requirements.txt
python producer.py
```
in other shell run
```bash
source .venv/bin/activate
python consumerX.py # where x is a number from 1 to 3. Every consumer is implemented with different way
```
to see the magic!