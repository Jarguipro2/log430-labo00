## Rapport laboratoire 00
### Guillaume Jarry  - JARG6630201
### LOG430


### Question 1 
~~~
Si l'un des tests échoue à cause d'un bug, comment pytest signale-t-il l'erreur et aide-t-il à la localiser ? Rédigez un test qui provoque volontairement une erreur, puis montrez la sortie du terminal obtenue.
~~~
pytest montre l'erreur en spécifiant le fichier de test et le nom de la fonction avec le test qui échoue avec une sortie style breadcrumbs ou il est possible de voir l'erreur directement dans la console.
![q1.png](screenshots/q1.png)