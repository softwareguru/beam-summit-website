## Overview
This repo contains the code and data for the [Beam Summit website](beamsummit.org) and is based on [Project Hoverboard](https://github.com/gdg-x/hoverboard) created by the [GDG Lviv](https://www.meetup.com/GDG-Lviv/) team.

## HOW TO USE (see much from below).
Structure:
* Master branch will be used to keep up-to-date with Hoverboard
* needing to add a 'main'/'landing-page' branch which will be a to-be-developed landing page
* branches will exist for each summit
* Each branch will be used to setup independant auto-build processes.  


## Getting Started
1. [Fork repository](https://github.com/gdg-x/hoverboard/fork) and clone it locally
1. Setup Environment
   * Install [Node.js (v8.9.4 or above)](https://nodejs.org/en/download/)
   * Install Firebase CLI: `npm i -g firebase-tools` or `yarn global add firebase-tools`
1. Install project dependencies: `npm install` or `yarn`
1. Create [Firebase account](https://console.firebase.google.com) and login into [Firebase CLI](https://firebase.google.com/docs/cli/): `firebase login`
1. Update [config](/config) and [Resources](/data)
1. Import initial data to the Firebase Database
    * Generate `serviceAccount.json` file
      - Go to https://console.firebase.google.com/project/%YOUR_PROJECT_ID%/settings/serviceaccounts/adminsdk
      - Ensure that **Node.js** is selected and press **GENERATE NEW PRIVATE KEY** 
      - Save the file as `serviceAccount.json` and to the root of your hoverboard directory (❗Do NOT commit this file to the public repository)
    * [Optional] You can edit `docs/default-firebase-data.json)` file using your own data
    * Run `npm run firestore:init` or `yarn firestore:init`
1. Run locally
   * `npm run serve` or `yarn serve`
1. Build and deploy
   * `npm run build` or `yarn build`
   * `npm run deploy` or `yarn deploy`
   
*NOTE:* By default command using configurations from `/configs/development.json`.
To serve locally or deploy the production app use `yarn serve:prod` and `yarn deploy:prod` respectively.

:book: Read the [Full Setup Guide](/docs/).

## Updating
Here is a git workflow for updating your fork (or downloaded copy) to the latest version:
```console
git remote add upstream https://github.com/gdg-x/hoverboard.git
git fetch upstream
git merge upstream/hoverboard
# resolve the merge conflicts in your editor
git add . -u
git commit -m 'Updated to the latest version'
```

## Documentation

The [Getting Started guide](#getting-started) is probably a good first point of call! <br>
:book: [Full documentation](/docs/).

## Compatibility

:white_check_mark: Compatible with **latest two** version of Chrome, Chrome for Android, Firefox, Opera, Safari, Edge.<br>
:x: IE and Opera Mini aren't supported.

## Contributors
__Maintainer:__ [Oleh Zasadnyy](https://github.com/ozasadnyy) and [Sophie Huts](https://github.com/sophieH29).

This project exists thanks to all the [people who contribute](https://github.com/gdg-x/hoverboard/graphs/contributors). [[Contribute](CONTRIBUTING.md)].

<a href="graphs/contributors"><img src="https://opencollective.com/hoverboard/contributors.svg?width=890" /></a>

## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fgdg-x%2Fhoverboard.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fgdg-x%2Fhoverboard?ref=badge_large)

Project is published under the [MIT license](/LICENSE.md).  
Feel free to clone and modify repo as you want, but don't forget to add reference to authors :)

_GDG[x] are not endorsed and/or supported by Google, the corporation._
