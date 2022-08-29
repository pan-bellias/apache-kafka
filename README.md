# Apache Kafka - Python Temperature

## Kafka / Kafka Connect Deployment using helm and kubernetes
Install helm by
```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
# or 
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```
```bash
helm install zookeeper bitnami/zookeeper --set replicaCount=1 --set auth.enabled=false --set allowAnonymousLogin=true --set persistence.enabled=false
helm install kafka bitnami/kafka --set zookeeper.enabled=false --set replicaCount=1 --set externalZookeeper.servers=zookeeper.default.svc.cluster.local --set persistence.enabled=false --set readinessProbe.initialDelaySeconds=60 --set livenessProbe.initialDelaySeconds=60
# kafka-0.kafka-headless.default.svc.cluster.local:9092 / kafka.default.svc.cluster.local:9092
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=kafka,app.kubernetes.io/instance=kafka,app.kubernetes.io/component=kafka" -o jsonpath="{.items[0].metadata.name}")

kubectl --namespace default exec -it $POD_NAME -- kafka-topics.sh  --create --bootstrap-server kafka-0.kafka-headless.default.svc.cluster.local:9092 --replication-factor 1 --partitions 1 --topic my-topic-a
kubectl --namespace default exec -it $POD_NAME -- kafka-topics.sh  --create --bootstrap-server kafka-0.kafka-headless.default.svc.cluster.local:9092 --replication-factor 1 --partitions 1 --topic my-topic-b

kubectl run kafka-client --restart='Never' --image docker.io/bitnami/kafka:2.8.0-debian-10-r43 --namespace default --command -- sleep infinity

kubectl exec --tty -i kafka-client --namespace default -- bash
```

Inside pod for testing
```bash
kafka-console-producer.sh --broker-list kafka-0.kafka-headless.default.svc.cluster.local:9092 --topic my-topic-a # or my-topic-b
kafka-console-consumer.sh --bootstrap-server kafka.default.svc.cluster.local:9092 --topic my-topic-a --from-beginning # or my-topic-b
```

## Run Example

### dotenv variables
```bash
cp .env.example .env
```
```nano
TOPIC_A='my-topic-a'
TOPIC_B='my-topic-b'
BOOTSTRAP_SERVER='kafka:9092'
```

### Execute scripts
```bash
python3 -m venv .venv
```
and
```bash
source .venv/bin/activate
pip install -r requirements.txt
python IoT_scripts/script-3-consumer.py
```
in other shell run
```bash
source .venv/bin/activate
python IoT_scripts/script-2-consumer-producer.py
```
and in other shell run
```bash
source .venv/bin/activate
python IoT_scripts/script-1-producer.py
```
to see the magic!
