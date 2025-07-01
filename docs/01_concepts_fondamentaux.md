# 01 - Concepts Fondamentaux du Streaming et Batch

## 1. Traitement Batch vs Traitement Streaming

### Explication simple 

- **Batch** : Imagine que tu reçois une grande pile de devoirs à corriger d’un coup. Tu prends toute la pile, tu la corriges en une fois, puis tu rends les copies.
- **Streaming** : Imagine que les devoirs arrivent un par un, en continu. Tu corriges chaque devoir dès qu’il arrive, sans attendre la pile complète.

### En termes techniques

- **Batch processing** traite des données **par lots** : toutes les données sont collectées puis traitées ensemble.
- **Streaming processing** traite les données **au fur et à mesure qu’elles arrivent**, souvent avec de faibles latences.

---

## 2. Apache Kafka : le système de messagerie en streaming

### Explication simple

Kafka est comme un grand tuyau par lequel passent des messages (données). Des machines appellent “producteurs” envoient des messages dans ce tuyau, et d’autres machines appelées “consommateurs” lisent ces messages quand ils veulent.

### Termes clés

- **Topic** : Une sorte de canal dans le tuyau. Chaque type de données a son propre topic.
- **Producer** : Celui qui envoie les messages.
- **Consumer** : Celui qui lit les messages.
- **Broker** : La machine qui garde les messages et fait circuler le tuyau.

---

## 3. Apache Flink : le moteur de traitement en streaming

### Explication simple
Flink est comme un robot intelligent qui se place à la sortie du tuyau Kafka, lit chaque message dès qu’il arrive, transforme ou analyse ces messages, et peut ensuite enregistrer le résultat ailleurs.

### Concepts importants

- **Transformation** : Modifier ou analyser chaque message (exemple : filtrer, additionner, calculer une moyenne).
- **Windowing** : Regrouper les messages en blocs de temps (exemple : tous les messages reçus pendant une minute).
- **Event Time et Watermark** : Gérer les horodatages et retards dans les données.

---

## 4. Notre projet

Nous simulons un flux de données en temps réel :

- Un script Python génère des données en continu (producteur Kafka).
- Un job Flink lit ce flux, le traite en temps réel, puis sauvegarde les résultats.

Ce pipeline **simule** ce qu’on ferait avec Kinesis (Amazon) mais en local, sans cloud.

---

## 5. Pourquoi ce projet est utile ?

- Apprendre les concepts de base du streaming en big data.
- Comprendre le rôle de Kafka et Flink.
- Préparer un futur travail en data engineering ou machine learning temps réel.

---

## 6. Questions à se poser

- Quelle différence entre streaming et batch dans mon quotidien ?
- Quelles sont les latences acceptables dans mes projets ?
- Comment gérer les données qui arrivent en retard ?
