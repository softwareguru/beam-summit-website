# Useful commands

## Firebase

Delete path: 
- One document: firebase firestore:delete <<path>>
- Whole collection:  firebase firestore:delete -r <<path>>

Load data: yarn firestore:copy fileToLoad.json destinationPath

## Switch between environments

1. firebase use <<project-name>>
2. Change serviceAccount.json to the right environment