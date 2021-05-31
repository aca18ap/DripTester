DripDash: cloud-side data collection and browser front-end(s) for ponics tronics...
===

Ed, seed this from your repo? Below some notes from our chat... One thing I
forgot to mention was that (for development purposes and for the CI) we will
probably also need a mock backend simulating WaterElf.

TODOs:

- tech stack normalisation and documentation
  - update libraries
  - separate back and front ends more fully
  - pwa for Vue stuff? e.g. https://cli.vuejs.org/core-plugins/pwa.html
- some additional (scaffolded?) app basics to think about
  - users, groups
    - either can have devices
  - addresses
  - locations, obfuscated locations, areas
- tech stack (to document)
  - Node
  - Express
  - Sequelize (and Epilogue for REST API support for WaterElf?)
  - PostgreSQL or MariaDB or SQLite
  - Vue
  - Gitlab CI
    - ? docker?
  - AWS EC2
  - VSCode
  - Discourse
- related projects
  - MyHarvest port
  - integration experiments
    - FarmOS / OpenTEAM
    - OpenFarm
    - Discourse
    - OpenFoodNetwork
    - FarmBot (with ponics growbed? wicking bed for spuds?)
- notes for docs
  - nice gentle intro to node/express
    https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Introduction


