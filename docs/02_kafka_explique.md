# 02 - Apache Kafka expliqué

## 1. Qu'est-ce que Kafka ?

Kafka est un système de messagerie distribué, utilisé pour envoyer, stocker et recevoir des flux de données en temps réel.

### Explication simple   
Imagine un système de messagerie ultra rapide, où plein de personnes (applications, machines) peuvent envoyer et recevoir des messages dans des "boîtes" spéciales.

---

## 2. Les composants clés de Kafka

| Terme      | Explication simple                      | Description technique courte                       |
|------------|---------------------------------------|--------------------------------------------------|
| **Topic**  | Une boîte aux lettres thématique      | Canal logique où les messages sont publiés       |
| **Partition** | Une sous-boîte pour distribuer le contenu | Un segment du topic qui permet la scalabilité   |
| **Producer** | L’expéditeur de message               | L’application qui écrit des messages dans un topic |
| **Consumer** | Le lecteur de message                 | L’application qui lit les messages d’un topic    |
| **Broker** | Le gardien des messages                | Serveur Kafka qui stocke et transmet les messages |
| **Offset** | Le numéro du message                   | Position unique d’un message dans une partition  |

---

## 3. Comment Kafka gère-t-il les messages ?

- Les messages sont stockés dans des partitions, ordonnés par offset.
- Les producteurs écrivent dans les partitions.
- Les consommateurs lisent à partir d’un offset donné.
- Chaque partition est un journal immuable (append-only log).

---

## 4. Pourquoi Kafka ?

- **Scalabilité** : Plusieurs partitions permettent de répartir la charge.
- **Tolérance aux pannes** : Les données sont répliquées entre brokers.
- **Durabilité** : Les messages sont conservés même après lecture.
- **Faible latence** : Parfait pour le streaming en temps réel.

---

## 5. Concepts avancés (à découvrir plus tard)

- Groupes de consommateurs (consumer groups)
- Offsets commit (pour garantir la lecture une fois)
- Retention policies (durée de conservation des messages)
- Compression des messages

---

## 6. Kafka vs autres systèmes

| Système      | Cas d’usage principal             | Différence clé                       |
|--------------|---------------------------------|-----------------------------------|
| RabbitMQ     | Messaging classique, file d’attente | Orienté messages, moins scalable   |
| Amazon Kinesis | Streaming cloud géré             | Service cloud, similaire à Kafka   |
| MQTT         | IoT, faible bande passante       | Protocol léger, pas conçu pour gros volume |

---

## 7. Résumé

Kafka est un outil puissant pour gérer des flux de données volumineux et rapides. Il est la colonne vertébrale de beaucoup de pipelines streaming modernes.

---

