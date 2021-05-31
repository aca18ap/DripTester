# Installation & Usage

## Prerequisites

Before installing DripDash, you need `nodejs` and `git`. 
```bash
sudo apt-get install nodejs git
```

DripDash is built for Node v10 or higher.

Planning on using DripDash with a PostgreSQL database? You'll also need a database server setup and the connection string handy. PostgreSQL is not required for development.

## Installation

1. To install DripDash, firstly clone this repository.  

```bash
# Clone via SSH (recommended)
git clone git@gitlab.com:unphone/dripdash.git

# Clone via HTTPS
git clone https://gitlab.com/unphone/dripdash.git
```

2. Navigate into the `dripdash` folder then install the required dependencies.

```bash
cd dripdash
npm install
```

3. Create `prisma/.env` and add your database credentials, or use the example.  
  We recommend [PostgreSQL](https://www.postgresql.org) for production, or
  SQLite for development. The example is already setup for development with SQLite.

```bash
cp prisma/.env.example prisma/.env
nano prisma/.env
```

4. Migrate the database (creating the required tables and relations).

```bash
npx prisma migrate up --experimental
```

Dripdash is now installed and ready to rock! Jump to [Usage](#usage)

### Updating
To update DripDash, pull the latest changes then install & migrate.

```bash
git pull
npm install
npx prisma migrate up --experimental
```

### Database Configuration

DripDash is setup out-of-the box to support SQLite for development.

If you're running a PostgreSQL database on the same server as DripDash, check out
the instructions [here](postgresql-setup.md).

If you're using a hosted PostgreSQL instance (e.g. AWS), place the connection
string in `prisma/.env`. For more information, view prisma's
[setup guide for PostgreSQL](https://www.prisma.io/docs/getting-started/setup-prisma/start-from-scratch-prisma-migrate-node-postgres#connect-your-database).

## Running DripDash

### Development

Run the development server (including the API and collector).
```bash
npm run serve
```

Run code linting and highlight any errors.
```bash
npm run lint
```

### Production

Create a production-ready build of DripDash
```bash
npm run build
```

Run the production build, on the default port.
```bash
npm run production
```

Run the production build, on a custom port.
```bash
PORT=1234 npm run production
```

> Note: We don't recommend using DripDash with `sudo`, or directly on port 80.  
> Instead, [use a web server such as `nginx` or `apache` as a proxy](nginx-setup.md).

### Backup
The easiest way to backup DripDash completely is to dump the database. The following instructions are for PostgreSQL.
```bash
# Dump the 'dripdash' database to dripdash.bak
sudo -u postgres pg_dump dripdash > dripdash.bak

# Restore from a .bak (into an existing, but empty database)
sudo -u postgres psql dripdash_restored < database.bak
```
### HTTPS
DripDash (and the external collector if enabled) use HTTP by default.  
To use HTTPS, we recommend using NGINX or Apache as a HTTPS proxy, and Let's Encrypt as the CA.

Here's a brief guide to [setting up DripDash on port 80, with HTTPS](nginx-setup.md).
