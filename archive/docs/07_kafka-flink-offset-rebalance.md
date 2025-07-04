EN

# Kafka Offsets and Rebalance Handling in a Flink Pipeline

## 1. Offsets in Kafka and Flink

- Kafka stores messages in partitions, each message has a unique **offset**, which is its position in the partition.
- Consumers (like Flink) read messages following these offsets.
- Flink uses **checkpoints** to save its progress, including the Kafka offsets it has processed.
- This allows Flink to **resume reading without data loss or duplication** if it restarts.

---

## 2. Why Offset Management Matters

- Without proper offset handling, you risk **processing messages multiple times (duplicates)** or **losing messages**.
- Flink relies on Kafka to guarantee **at-least-once** processing.
- With advanced mechanisms, Flink can guarantee **exactly-once** processing semantics.

---

## 3. Kafka Rebalance and Its Impact on Flink

- A rebalance happens when a consumer joins or leaves a consumer group (for example, if Flink restarts or changes parallelism).
- Kafka redistributes partitions among the active consumers.
- Flink handles rebalance smoothly thanks to its checkpoints, allowing it to continue reading correctly.
- During rebalance, consumption briefly pauses, which can cause small latencies.

---

## 4. Summary and Impact on Our Project

- Flink ensures **continuity and correctness** of processing even during rebalance or crashes by managing offsets through checkpoints.
- In our local Codespaces setup, we simulate this behavior to prepare for real production environments.
- We don’t manually commit offsets — Flink handles it automatically.

---

## 5. Next Steps to Explore

- Learn how Flink implements **checkpoints** and **state management**.
- Observe in the project how Kafka consumption is connected to Flink processing.
- Test restarting the Flink job to see how it resumes from saved offsets.

---

## Questions to Think About

- What happens inside Flink if the job is stopped while processing?
- How does Flink ensure each message is processed only once?
- What are the limitations of this offset management in a local environment?

---



FR
# Gestion des Offsets et Rebalance Kafka dans un Pipeline Flink

## 1. Offsets dans Kafka et Flink

- Kafka stocke les messages dans des partitions, chaque message a un **offset** unique, qui est sa position dans la partition.
- Les consommateurs (ici Flink) lisent les messages en suivant ces offsets.
- Flink utilise **des checkpoints** pour sauvegarder où il en est dans le traitement, incluant les offsets Kafka.
- Cela permet à Flink de **reprendre la lecture sans perte ni duplication** en cas de redémarrage.

---

## 2. Pourquoi gérer les offsets est important ?

- Sans gestion précise, on risque de **retraiter les messages (duplication)** ou de **perdre des messages**.
- Flink s’appuie sur Kafka pour garantir une lecture **au moins une fois** (at-least-once).
- Avec des mécanismes avancés, Flink peut garantir une lecture **exactement une fois** (exactly-once).

---

## 3. Rebalance Kafka et son impact sur Flink

- Le rebalance survient quand un consommateur rejoint ou quitte un groupe (par exemple si Flink redémarre ou change de parallélisme).
- Kafka redistribue les partitions entre les consommateurs.
- Flink gère ce rebalance grâce à ses checkpoints pour continuer la lecture proprement.
- Pendant le rebalance, la consommation est brièvement suspendue, ce qui peut créer de petites latences.

---

## 4. Résumé et impact sur notre projet

- Flink garantit la **continuité et la cohérence** du traitement même lors de rebalance ou crash, grâce à la gestion des offsets via ses checkpoints.
- En local dans Codespaces, on simule ce comportement, ce qui prépare à comprendre la robustesse en production.
- On ne gère pas manuellement les commits d’offset, Flink s’en charge automatiquement.

---

## 5. Pour aller plus loin

- Comprendre comment Flink réalise ses **checkpoints** et **state management**.
- Observer dans notre projet comment la lecture Kafka est connectée à Flink.
- Tester les redémarrages du job Flink pour voir la reprise à partir des offsets sauvegardés.

---

## Questions à se poser

- Que se passe-t-il dans Flink si on stoppe le job en plein traitement ?
- Comment Flink assure-t-il que chaque message est traité une fois ?
- Quelles sont les limites de cette gestion dans un environnement local ?

---
