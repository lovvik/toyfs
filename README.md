# toyfs
Exppérimentation sur système de fichiers sur disque  


## Principe :
Le but était de créer un "coffre-fort", un dossier empêchant l'accès des données qu'il contient , à un personne non-autorisée.
J'utilise pour cela FUSE qui permet de créer un système de fichiers personnalisé. 

##  Fonctionnement : 
Un dossier à protéger "Folder" est monté en un second dossier "Gate" ( attention : ce dernier doit être vide).
    
```
$ pyton3 myfs.py Folder Gate
```
    
on accède désormais aux fichiers de Folder via Gate. Le programme va créer des versions chiffrées des fichiers de Folder. Ils porteront l'extension ".enc"
Cela se fait grâce au chiffrement par bloc vu plus tôt dans l'année.

Vous remarquerez qu'un mot de de passe est demandé au montage. Si le bon mdp est renseigné, l'utilisateur pourra interagir normalement avec les fichiers.
Sinon, il recevra les chiffrés, chaque fois qu'il cherchera à accéder à tel ou tel fichier.

Le mot de passe est écrit en dur dans le code, il s'agit de "password" 


## Dépendances
les packages python suivants sont nécessaires  

os  
sys  
errno  
fusepy  

[Libfuse](https://github.com/libfuse/libfuse) le sera peut-être aussi.

