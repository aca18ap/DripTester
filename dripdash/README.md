**⚠️ DripDash is still a work in progress, check back for updates.**

![DripDash Header](public/drip-dash-header.svg)

DripDash is an all-in-one aquaponics monitoring, control and data logging tool,
built with Vue on Node.js.

## :memo: About DripDash

Aquaponics is hard. It's a three-way ecosystem with plants, bacteria and fish
living in balanced symbiosis. DripDash, along with the rest of the unPhone project,
aims to make aquaponics easier.

DripDash is constructed in three parts:
- The frontend, constructed with Vue.js for control and monitoring.
- The backend, integrating express, the database and GraphQL API.
- The collector, a separate endpoint for communicating WaterElf devices.

DripDash is part of the [unPhone Project](https://unphone.net/).

## :bookmark_tabs: Documentation

- [Installation & Usage](docs/installation.md)
- [Tech Stack](docs/tech-stack.md)
- [API](docs/API.md)

## :zap: Quick Start Guide

For more detailed instructions, check out the **[Documentation](docs/README.md)**.

```bash
# Assuming nodejs and git are already present.

# 1 - Clone the repository.
git clone git@gitlab.com:unphone/dripdash.git
cd dripdash

# 2 - Install dependencies.
npm install

# 3 - Connect the database. (Set the connection string in prisma/.env)
cp prisma/.env.example prisma/.env

# 3.1 - Create the required structure in the database.
npx prisma migrate up --experimental

# 4a - Start for development.
npm run serve

# 4b - Alternatively, start for production.
npm run build
npm run production
```

## :beetle: Issues & Bugs

Found a bug? Feel free to raise an issue or submit a PR and we'll take a look at it.


## :wave: Contributors & Thanks

DripDash is built and maintained by:
- Edward (onfe) - https://onfe.uk