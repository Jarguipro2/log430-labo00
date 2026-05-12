# Labo 00 – Infrastructure (Git, Docker, CI/CD)

<img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Ets_quebec_logo.png" width="250">    
ÉTS - LOG430 - Architecture logicielle - Chargé de laboratoire: Gabriel C. Ullmann.

## 🎯 Objectifs d'apprentissage

- Apprendre à créer un projet **Python** conteneurisé avec **Docker** à partir de zéro.
- Apprendre à écrire et exécuter des tests automatisés avec **pytest**.
- Mettre en place un pipeline **CI/CD** avec les ressources à notre disposition.

---

## ⚙️ Setup

Dans ce laboratoire, vous travaillerez sur une application calculatrice. Cette calculatrice est volontairement très simple afin que nous puissions nous concentrer sur la configuration et la structure du projet, ainsi que sur la création d'un pipeline CI/CD.

Vous allez créer la structure du projet vous-même à partir de zéro, en créant le `requirements.txt`, `Dockerfile`, `docker-compose.yml` et `.env`. Chaque activité vous guidera dans une étape de setup, puis l'implémentation. Il est très important de réaliser ce laboratoire car :

- Les concepts que vous apprendrez ici (ex. le setup Python et Docker, les approches de test et déploiement, etc.) vous aideront à mieux comprendre **TOUS** les laboratoires suivants.
- Les concepts architecturaux et les pratiques de développement que vous apprenez ici peuvent être appliqués au projet, **dans n'importe quel langage de programmation ou framework**.

Dans les prochains laboratoires, nous verrons des architectures plus complexes et nous travaillerons avec une variété d'outils logiciels et de concepts architecturaux.

> ⚠️ **ATTENTION** : Si vous ne l'avez pas déjà fait, nous vous recommandons d'installer **VS Code**, **Python 3+**, **Docker Desktop** et **MySQL Workbench** avant de commencer.

> ⚠️ **IMPORTANT** : Avant de commencer le setup et les activités, veuillez lire la documentation architecturale dans le répertoire `/docs/arc42/docs.pdf` pour comprendre quel type d'application nous serons en train de développer.

### 1. Clonez le dépôt

```bash
git clone < lien à votre dépôt GitHub >
cd log430-labo0
```

### 2. Créez votre fichier requirements.txt

Le fichier `requirements.txt` contient la liste des dépendances Python que vous avez besoin pour exécuter votre projet et qui seront installées via [pip](https://www.w3schools.com/python/python_pip.asp) dans votre environnement. Vous aurez besoin d'une seule dépendance pour ce projet : `pytest` (pour exécuter les tests unitaires). Créez un fichier `requirements.txt` dans le répertoire racine de votre projet :

```sh
pytest>=7.0
```

### 3. Créez votre Dockerfile

Un fichier `Dockerfile` est une recette permettant de créer une image de conteneur Docker. Un conteneur est une machine virtuelle simplifiée qui s'exécutera dans votre environnement de développement local, mais qui peut également s'exécuter dans un environnement de production si vous le souhaitez. Créez un fichier `Dockerfile` dans le répertoire racine de votre projet :

```sh
FROM python:3.11-slim
WORKDIR /app
COPY src/ ./src/
COPY requirements.txt ./
ENV PYTHONPATH=/app/src
RUN pip install --no-cache-dir -r requirements.txt
```

### 4. Créez votre docker-compose.yml

Un fichier `docker-compose.yml` décrit quels conteneurs (également appelés services) seront créés en utilisant votre image de conteneur Docker comme base. Dans notre cas, nous voulons uniquement exécuter notre calculatrice. Créez un fichier `docker-compose.yml` dans le répertoire racine de votre projet :

```yml
services:
  calculator:
    build: .
    volumes:
      - .:/app
    stdin_open: true
    tty: true
```

### 5. Créez votre .env

Un fichier `.env` est utilisé pour garder les variables d'une application qui sont distinctes pour chaque instance et que nous ne voulons pas écrire dans le code pour des raisons de sécurité et de flexibilité. Par exemple, une application de gestion de magasin aura une base de données différente pour chaque magasin, avec un nom d'utilisateur et un mot de passe également distincts et qui ne doivent pas être partagés dans le code. Ici, dans ce très simple cas, nous garderons simplement le nom de l'utilisateur de la calculatrice. Créez un fichier `.env` dans le répertoire racine de votre projet avec une seule ligne :

```sh
CALCULATOR_USERNAME=YourName
```

Une fois le fichier `.env` créé et la variable définie, l'application dans `/src/calculator.py` est déjà préparée pour lire le `.env`, extraire la variable `CALCULATOR_USERNAME` et l'utiliser. Si vous faites votre propre application à partir de zéro, vous devriez écrire vous-même le code pour lire le `.env`, ou utiliser une librairie telle que [dotenv](https://www.geeksforgeeks.org/python/using-python-environment-variables-with-python-dotenv/) pour vous aider.

### 6. Démarrez le conteneur

Dans le terminal, exécutez :

```sh
docker compose build
docker compose up -d
```

Ensuite, cliquez sur votre conteneur dans la liste dans Docker Desktop, sélectionnez l'onglet `Exec` et exécutez :

```sh
python src/calculator.py
```

> 📝 **NOTE** : l'autocomplétion en appuyant sur Tab et les flèches du clavier ne marchent pas dans Docker Desktop, parce qu'il utilise une interface Bash simplifiée. Si vous n'aimez pas cela, vous pouvez également exécuter les commandes via [docker exec](https://docs.docker.com/reference/cli/docker/container/exec/) à partir de votre machine hôte (hors Docker).

---

## 🧪 Activités

### 1. Écrivez les tests

Dans le fichier `test_calculator.py`, écrivez des tests pour les fonctions définies dans `calculator.py`.

```python
def test_addition():
    assert addition(2, 3) == 5
```

Pour lancer les tests :

```bash
pytest
```

> 💡 **Question 1** : Si l'un des tests échoue à cause d'un bug, comment pytest signale-t-il l'erreur et aide-t-il à la localiser ? Rédigez un test qui provoque volontairement une erreur, puis montrez la sortie du terminal obtenue.

### 2. Vérifier les étapes à la pipeline CI (Intégration Continue)

Le fichier `.github/workflows/.github-ci.yml` est déjà préparé pour que GitHub exécute les tests automatiquement à chaque push. Veuillez lire le fichier pour vous familiarizer avec les étapes (steps).

> ⚠️ **IMPORTANT** : Il n'est pas recommandé d'écrire les noms d'utilisateur et les mots de passe en « plain text » dans un fichier tel que `.github/workflows/.github-ci.yml`. Veuillez utiliser les [secrets](https://docs.github.com/fr/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets) dans un [environnement GitHub](https://docs.github.com/fr/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments#creating-an-environment) **si vous avez besoin** de gérer des informations d'authentification.

### 3. Versionnez votre code

Si tous les tests passent :

```bash
git add .
git commit -m "Tests pour calculator.py"
git push
```

GitHub exécutera les tests sur son serveur, et ils devront passer également s'ils sont corrects.

> 💡 **Question 2** : Que fait GitHub pendant les étapes de « setup » et « checkout » ? Veuillez inclure la sortie du terminal GitHub CI dans votre réponse.

### 4. Réfléchissez à comment déployer votre code en production

Déployer en production signifie copier votre dépôt et faire le setup de votre application en dehors de votre environnement de développement, dans un autre serveur. Ce serveur pourrait être, par exemple :

- Un serveur physique dans une entreprise/école
- Un serveur en nuage (ex. Azure, AWS, etc.)
- Une machine virtuelle (VM) dans un serveur

Dans le cours LOG430, nous utiliserons des VMs créées dans [LXD](https://canonical.com/lxd), une application de gestion de VMs et conteneurs. Nous utiliserons une instance LXD hébergée par l'école.

### 5. Installez lxc

Nous utiliserons [lxc](https://documentation.ubuntu.com/lxd/latest/reference/manpages/lxc/), un client LXD disponible pour Windows, macOS et Linux.

Installez sur Windows via `chocolatey` :
```sh
choco install lxc
```

Installez sur Windows (WSL) ou Linux via `snap` :
```sh
snap install lxd
```

Installez sur macOS via `brew` :
```sh
brew install lxc
```

Pour ajouter les serveurs LXD, connectez-vous au **VPN** et exécutez :
```sh
lxc remote add fiware-1 fiware-1.logti.etsmtl.ca
```

Ces commandes demanderont un jeton chacune. Demandez votre jeton au chargé de lab.

> 📝 **NOTE** : Ce sont des jetons à usage unique. Par conséquent, lorsqu'une personne intègre un serveur dans son client LXD, le jeton est annulé et ne peut plus être utilisé pour ajouter un second client.

Ensuite, configurez votre profil dans `lxc`. Il ne faudra le faire qu'une seule fois, les VMs subséquentes suivront déjà ces configurations :

```bash
# Voir les profils disponibles
lxc profile list

# Ajouter un device root au profil default
lxc profile device add default root disk path=/ pool=default size=20GB

# Définir une limite de mémoire (4GB recommandé, max 8GB selon quotas)
lxc profile set default limits.memory=4GB
```

#### 5.1. Créez une VM
Pour créer une VM sur le serveur `fiware-1.logti.etsmtl.ca`, exécutez `lxc launch`. Dans l'exemple ci-dessus, remplacez `<nom-vm>` par le nom que vous voulez donner à votre VM :
```sh
lxc launch ubuntu:22.04 fiware-1:<nom-vm> --vm
```

> 📝 **NOTE** : Pour les noms de VMs, préférez les noms en kebab-case. Par exemple: `vm-gabriel-log430`.

> ⚠️ **IMPORTANT** : C'est crucial d'utiliser le flag `--vm` parce que, sans ce flag, LXD créera un conteneur au lieu d'une VM, et Docker ne pourra pas fonctionner.

Pour voir la liste des machines virtuelles sur le serveur avec leur adresse IP et leur statut :

```bash
lxc list
```

Voici un exemple de sortie attendue :
```sh
+--------------------+---------+------+-----------------------------------------------+-----------------+-----------+
|       NAME         |  STATE  | IPV4 |                     IPV6                      |      TYPE       | SNAPSHOTS |
+--------------------+---------+------+-----------------------------------------------+-----------------+-----------+
| <nom-vm>           | RUNNING |      | fd42:e706:c40b:f0b7:216:3eff:fe35:9940 (eth0) | VIRTUAL-MACHINE | 0         |
+--------------------+---------+------+-----------------------------------------------+-----------------+-----------+
```

Si la colonne `IPV4` est vide pour vous ou si vous obtenez une erreur de réseau, ne vous inquiétez pas, parce que nous allons configurer le réseau dans les prochaines étapes.

#### 5.2. Changez les configurations de réseau de la VM

Par défaut, la VM est dans un autre réseau, isolé du réseau où `fiware-1.logti.etsmtl.ca` et votre ordinateur se trouvent. Pour permettre l'accès SSH depuis votre ordinateur, vous devez configurer la VM sur l'interface bridge `br0`.

```bash
#  Ajouter l'interface br0 au profil 
lxc profile device add default eth0 nic nictype=bridged parent=lxdbr0
lxc config device override fiware-1:<nom-vm> eth0
lxc config device set fiware-1:<nom-vm> eth0 parent=br0

# Redémarrer la VM
lxc restart fiware-1:<nom-vm>
```

Veuillez attendre 30-40 secondes que la VM redémarre.

#### 5.3. Configurez une adresse IP statique
Pour définir une IP statique pour votre VM, exécutez la commande ci-dessus. Remplacez `<VOTRE_IP>` par une adresse IP de la plage `10.194.32.155` à `10.194.32.253`. Cela veut dire que nous avons 99 IPs disponibles.

> 🚫 **ATTENTION** : Il est **strictement interdit** d'utiliser des adresses autres que celles réservées (de `10.194.32.155` à `10.194.32.253`). Si quelqu'un abuse et décide d'attribuer une adresse qui est en dehors de la plage comme `10.194.32.34`, l'accès aux serveurs sera révoqué pour la personne fautive et ses machines seront arrêtées.
> ⚠️ **IMPORTANT** : Pour éviter des conflits d'adresse IP avec vos camarades, choisissez une adresse et enregistrez votre nom dans [ce document](https://docs.google.com/spreadsheets/d/1R9xkjllqm20-4k7mT3_JpbhTqQcAbhKceuWu98zOlG8/edit?usp=sharing) afin de les informer.

```bash
# Créer le fichier de configuration netplan
lxc exec fiware-1:<nom-vm> -- bash -c "cat > /etc/netplan/50-cloud-init.yaml <<'EOF'
network:
  version: 2
  ethernets:
    enp5s0:
      dhcp4: no
      addresses:
        - <VOTRE_IP>/24
      routes:
        - to: default
          via: 10.194.32.1
      nameservers:
        addresses:
          - 10.162.8.10
          - 10.162.8.11
EOF"

# Appliquer la configuration
lxc exec fiware-1:<nom-vm> -- netplan apply
```

> 📝 **NOTE** : Le warning "Cannot call Open vSwitch: ovsdb-server.service is not running" est normal et sans conséquence.

Pour vérifier l'IP :
```bash
lxc exec fiware-1:<nom-vm> -- ip addr show enp5s0
```

Résultat attendu :
```bash
2: enp5s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:16:3e:16:17:40 brd ff:ff:ff:ff:ff:ff
    inet <VOTRE_IP>/24 brd 10.194.32.255 scope global enp5s0
       valid_lft forever preferred_lft forever
```

Pour vérifier la connectivité depuis votre ordinateur, exécutez `ping`. Remplacez `<VOTRE_IP>` pour l'IP de la VM (ATTENTION: ceci n'est pas l'IP à votre ordinateur) :
```bash
ping -c 3 <VOTRE_IP>
```

#### 5.4. Configurez l'accès via SSH
Même si on peut se connecter aux VMs via `lxc`, ce n'est pas idéal parce que nous dépendons toujours d'un ordinateur avec le client `lxc` installé et cela ne nous permet pas de communiquer entre les VMs, ou avec certains services qui n'utilisent pas `lxc` (ex. des outils CI/CD). Ainsi, nous devons configurer l'accès SSH dans les VM à partir de notre ordinateur :

```bash
# Installer openssh-server dans la VM
lxc exec fiware-1:<nom-vm> -- bash -c "apt update && apt install -y openssh-server"

# Créer un keypair (clé privée + clé publique)
ssh-keygen -t rsa -b 4096 -f ~/.ssh/lxd_key

# Créer le dossier .ssh dans la VM
lxc exec fiware-1:<nom-vm> -- mkdir -p /root/.ssh

# Copier la clé publique à la VM
lxc file push ~/.ssh/lxd_key.pub fiware-1:<nom-vm>/root/.ssh/authorized_keys

# Définir les permissions
lxc exec fiware-1:<nom-vm> -- bash -c "chmod 700 /root/.ssh && chmod 600 /root/.ssh/authorized_keys"

# Tester la connexion
ssh -i ~/.ssh/lxd_key -o StrictHostKeyChecking=accept-new root@<VOTRE_IP> hostname
ssh -i ~/.ssh/lxd_key root@<VOTRE_IP>
```

### 6. Déployez votre application manuellement

Connectez-vous à votre VM et déployez l'application Calculatrice une première fois sur la VM manuellement. N'oubliez pas d'installer Docker et toute autre dépendance nécessaire sur la VM :

```sh
git clone < lien à votre dépôt GitHub >
cd log430-labo0
```

> 📝 **NOTE** : Si vous avez une VM très lente ou bloquée, essayez de l'arrêter et de la redémarrer, ou de la recréer. Pour connaître quelques commandes utiles pour créer/supprimer/déboguer des VMs, consultez le fichier `COMMANDS.md`. Si cela ne fonctionne pas, parlez au chargé de lab.

> 💡 **Question 3** : Quel type d'informations pouvez-vous obtenir via la commande `top` ? Veuillez donner quelques exemples. Veuillez inclure la sortie du terminal dans votre réponse.

### 7. Automatisez le déploiement continu (CD)

Plusieurs alternatives existent pour le CD : déploiement par SSH déclenché par webhooks dans GitHub, ou dans un outil CI/CD (ex. ArgoCD). Cependant, dans ce labo, nous vous recommandons d'utiliser un [GitHub Runner auto-hébergé (self-hosted)](https://docs.github.com/fr/actions/how-tos/manage-runners/self-hosted-runners/add-runners).

Nous vous recommandons le GitHub Runner parce que c'est l'approche la plus simple et moins dépendante d'une configuration spécifique de réseau (ex. il n'est pas nécessaire d'ouvrir des ports dans le pare-feu, ou d'utiliser une approche événementielle). Voici quelques [exemples](https://docs.github.com/fr/actions/how-tos/manage-runners/self-hosted-runners/use-in-a-workflow) de workflow CI.

**Résultat attendu** : à chaque fois que vous faites `push` à GitHub, votre serveur fera `pull` automatiquement et mettra l'application en marche.

---

## 📦 Livrables

- Code compressé en `.zip` contenant **l'ensemble du code source** du projet Labo 00.
- Rapport `.pdf` répondant aux 3 questions présentées dans ce fichier. Il est **obligatoire** d'ajouter du code ou des sorties de terminal pour illustrer chacune de vos réponses.

Vous avez des questions sur le format de soumission ? [Voici un exemple](https://drive.google.com/file/d/12ss6zSayGCjHCydf9fRJ3wvqsOQNMBa9/view?usp=sharing). Veuillez respecter cette même structure de dossiers pour **toutes** vos soumissions de laboratoire. Cela nous permet de corriger vos laboratoires plus rapidement et plus correctement.
