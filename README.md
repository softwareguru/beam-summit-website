## Overview
This repo contains the code and data for the [Beam Summit website](beamsummit.org) and is based on [Project Hoverboard](https://github.com/gdg-x/hoverboard) created by the [GDG Lviv](https://www.meetup.com/GDG-Lviv/) team.
=======
Project Hoverboard is the conference website template that helps you to set up a mobile-first conference website with blog, speaker and schedule management in a few minutes.

The template is created based on 7 years of [GDG Lviv](https://www.meetup.com/GDG-Lviv/) team experience of running conferences and feedback from more than 500 event organizers from all around the world who were using previous Hoverboard versions.

Our goal is to allow event organizers to set up a professional conference website with minimum resources. To get started you need only basic knowledge of web technologies and a free Firebase account.

## Features
| Feature | Description |
|---|---|
| **Fast and optimized** | 91/100 PWA on [Lighthouse](https://www.webpagetest.org/lighthouse.php?test=180111_1P_027a041bc5102982f074014807320a86&run=3) |
| **Works offline** | shitty WiFi on the venue is not a problem anymore |
| **Mobile-first** | layouts optimized for small screens, Hoverboard can be installed as a native app on your phone |
| **Push notifications** | remind about sessions in My schedule, session feedback or target users with a custom message |
| **SEO optimized** | index all content and get to the top in search results |
| **Speakers and schedule management** | keep and update all information in the  Firebase |
| **My schedule** | let attendees save sessions they want to visit |
| **Customizable theme** | change colors to match your style |
| **Blog** | post announcements, updates and useful information |
>>>>>>> upstream/master

## HOW TO USE (see much from below).
Structure:
* Master branch will be used to keep up-to-date with Hoverboard
* needing to add a 'main'/'landing-page' branch which will be a to-be-developed landing page
* branches will exist for each summit
* Each branch will be used to setup independant auto-build processes.  


## Getting Started
1. [Fork repository](https://github.com/gdg-x/hoverboard/fork) and clone your fork locally
1. Install [Node.js (v10+)](https://nodejs.org/en/download/)
1. Install project dependencies: `npm install` or `yarn`
1. Create [Firebase account](https://console.firebase.google.com) and login into [Firebase CLI](https://firebase.google.com/docs/cli/): `firebase login`
1. Update [config](/config) and [Resources](/data)
=======
1. Create [Firebase account](https://console.firebase.google.com) and login into [Firebase CLI](https://firebase.google.com/docs/cli/): `npx firebase login`
1. Update [Hoverboard config](/config) and [Resources](/data)
>>>>>>> upstream/master
1. Import initial data to the Firebase Database
    * Generate `serviceAccount.json` file
      - Go to [console.firebase.google.com](https://console.firebase.google.com) -> Project settings -> Service accounts
      - Ensure that **Node.js** is selected and press **Generate new private key**
      - Read the warning and press **Generate key**
      - Save the file as `serviceAccount.json` and to the root of your hoverboard directory (❗Do NOT commit this file to the public repository)
    * Enable Firestore in web console at [console.firebase.google.com](https://console.firebase.google.com) -> Database -> Cloud Firestore -> Create database. Select **locked mode** and press **Enable**
    * [Optional] You can edit `docs/default-firebase-data.json)` file using your own data
	  * Select your Firebase project `npx firebase use <YOUR_PROJECT_ID>`
    * Run `npm run firestore:init` or `yarn firestore:init`
1. Run locally
   * `npm start` or `yarn start`
1. Build and deploy
   * `npm run build` or `yarn build`
   * `npm run deploy` or `yarn deploy`

*NOTE:* By default command using configurations from `/configs/development.json`.
To serve locally or deploy the production app use `yarn start:prod` and `yarn deploy:prod` respectively.

:book: Read the [Full Setup Guide](/docs/).

=======
### Docker-based development environment

If you don't want to bother with the dependencies, you can use the docker container for development.

:book: Read more in [docker docs](/docs/tutorials/05-docker.md).

>>>>>>> upstream/master
## Updating
Here is a git workflow for updating your fork (or downloaded copy) to the latest version:

```console
git remote add upstream https://github.com/gdg-x/hoverboard.git
git fetch upstream
git merge upstream/master
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

=======
## Technology Stack

* Polymer 2
* Redux
* Firebase
* Service Worker
* CSS Grid

## Contributing

Awesome! Contributions of all kinds are greatly appreciated. To help smoothen the process we have a few non-exhaustive guidelines to follow which should get you going in no time.

### Good First Issue

Issues labeled [`good first issue`](https://github.com/gdg-x/hoverboard/labels/good%20first%20issue) are a great way to ease into development on this project.

### Help Wanted Label

Any other issue labeled [`help wanted`](https://github.com/gdg-x/hoverboard/labels/help%20wanted) is ready for a PR.

### Using GitHub Issues

* Feel free to use GitHub issues for questions, bug reports, and feature requests
* Use the search feature to check for an existing issue
* Include as much information as possible and provide any relevant resources (Eg. screenshots)
* For bug reports ensure you have a reproducible test case
* A pull request with a breaking test would be super preferable here but isn't required

### Submitting a Pull Request

* Squash commits
* Lint your code with eslint (config provided)
* Include relevant test updates/additions

## Code of Conduct

Read the full version [Code of Conduct](/CODE_OF_CONDUCT.md).

>>>>>>> upstream/master
## Contributors
__Maintainer:__ [Abraham Williams](https://github.com/abraham)  
__Authors:__ [Oleh Zasadnyy](https://github.com/ozasadnyy) and [Sophie Huts](https://github.com/sophieH29).

This project exists thanks to all the [people who contribute](https://github.com/gdg-x/hoverboard/graphs/contributors). [[Contribute](CONTRIBUTING.md)].

<a href="https://github.com/gdg-x/hoverboard/graphs/contributors"><img src="https://opencollective.com/hoverboard/contributors.svg?width=890" /></a>

=======
## Sponsoring
Most of the core team members, hoverboard contributors and contributors in the ecosystem do this open-source work in their free time. If you like this project and it makes your life easier, please donate.
<a href="https://opencollective.com/hoverboard#backers" target="_blank"><img src="https://opencollective.com/hoverboard/backers.svg?width=890"></a>

>>>>>>> upstream/master
## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fgdg-x%2Fhoverboard.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fgdg-x%2Fhoverboard?ref=badge_large)

The project is published under the [MIT license](/LICENSE.md).
Feel free to clone and modify repo as you want, but don't forget to add a reference to authors :)

_GDG[x] is not endorsed and/or supported by Google, the corporation._
