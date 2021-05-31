# PostgreSQL Local Setup

If you're using PostgreSQL (pg) on the same machine as DripDash, here's how to get it installed and configured.

## Installation

Firstly, let's install pg and create a user and database:

```bash
# First, install PostgreSQL using your package manager. For example:
sudo apt-get install postgresql

# Create the user 'dripdash'.
sudo -u postgres createuser dripdash

# Create the database 'dripdash'.
sudo -u postgres createdb dripdash

# Login to psql as postgres.
sudo -u postgres psql
```

Now, within the PostgreSQL prompt:

```sql
-- Grant 'dripdash' permission to edit the 'dripdash' db.
GRANT ALL PRIVILEGES ON DATABASE dripdash TO dripdash;

-- Change the password, here we'll assume you set it to password.
\password dripdash

-- Exit the prompt.
\q
```

Just to be safe it's a good idea to restart the `postgresql` service: `sudo service postgresql restart`.

## `.env` configuration

If you've setup PostgreSQL locally as shown above, your `prisma/.env` will look like this:

```
DATABASE_URL=postgresql://dripdash:password@localhost:5432/dripdash
```

## Storage location

By default pg creates it's data store at `/var/lib/postgresql/<version>/main`. Depending on your system, you may want to move it elsewhere.

```bash
# Open psql from your terminal:
sudo -u postgres psql

# Now, in psql:
SHOW data_directory;
```

Now you know for certain where it is, we can move it. We need to stop it first, to prevent data corruption.

```bash
sudo systemctl stop postgresql
```

To move the directory, use `rsync` (to preserve permissions), then remove the old store.

```bash
rsync -av /var/lib/postgresql /home/ubuntu/data/db
```

Edit `/etc/postgresql/<version>/main/postgresql.conf`

```
data_directory = '/path/to/new/main'
```

Finally, restart `postgresql` and check everything is where you expect it to be.

