# API

DripDash uses two main endpoints for it's API.
- [`/collect` for the collector endpoint](#collectid).
- [`/api` for everything else](#api-1), via GraphQL.

Endpoints that require authentication have a padlock symbol (:closed_lock_with_key:).

## `/collect/:id/`

Used for data submissions from connected devices.
The collector endpoint accepts data from devices via either `get` or `post`.

##### Parameters

* `id` - A unique identifier of the device that is connecting. Typically this follows the format `DeviceType-MacAddress`, for example `WaterElf-AABBCCDDEEFF`.

##### Body

The body of the request should contain the current state of the device. Omitting fields is allowed.
```JSON
{
  "waterTemp": Float,
  "airTemp": Float,
  "humidity": Float,
  "light": Float,
  "ph": Float,
  "rssi": Float,
  "beds": [
    { "status": Int, "level": Float }
  ]__
}
```

## `/api`

The main GraphQL API.
* **Mutations** - Update, create and delete data.
* **Queries** - Read data, with the fields you supply.

##### Authorization
Some endpoints require an Authorization header token. This token can be obtained from the `login` mutation.

The header should be set as follows:
```
Authorization: <token received from login>
```

Tokens are signed JSON Web Tokens (JWTs).

The token expiry is encoded into the JWT as the number of seconds since UNIX epoch.
A token that is nearing expiry (but not yet expired) can be exchanged for a new token by using the `refresh` mutation. This allows the authentication to be extended without prompting the user for their credentials.

If a token is not supplied, or is otherwise invalid, queries and mutations will return null.

### Mutations

#### `login(username: String!, password: String)!: String`
Login a user and return an authorization token used to access secured endpoints.

##### Parameters
* `username` (String, required) - The username of the user attempting to log in.
* `password` (String, required) - The password of the user attempting to log in.

##### Response
If the credentials match, an `Authorization` JSON Web Token (JWT) is returned.  
If the credentials do not match a user, no token is returned.

#### `register(username: String!, password: String!): Boolean`
Register a new user.

##### Parameters
* `username` (String, required) - The username of the user to register.
* `password` (String, required) - The password of the user to register.

##### Response
If a user is created successfully, `True` is returned.
If there is already a user registered with the given username, `False` is returned.

#### `refresh: String` :closed_lock_with_key:
Refresh the authorization token. Requires a valid token to be set in the Authorization header.

##### Response
If the authorization token in the header is valid, a new token is returned with a later expiry.
If an invalid or expired token is passed, `null` is returned.

#### `createGroup(name: String!): Group` :closed_lock_with_key:
Create a group.

##### Parameters
* `name` (String, required) - The name of the group to create.

##### Response
Returns the newly created `Group` if the group is created, else `null`.

#### `leaveGroup(id: Int!): Group` :closed_lock_with_key:
Leave a group.

##### Parameters
* `id` (Integer, required) - The ID of the group to leave.

##### Response
Returns the `Group` you just left. Else `null`. If you were the last member of the group, the group is deleted automatically.

#### `addUserToGroup(username: String!, groupId: Int!): Group` :closed_lock_with_key:
Add the specified user to a group.

##### Parameters
* `username` (String, required) - The username of the user you wish to add to the group.
* `groupId` (Integer, required) - The ID of the group to add the user to.

##### Response
Returns the `Group` after the new user has been added, else `null`.

#### `addDeviceToGroup(deviceId: Int!, groupId: Int!): Group` :closed_lock_with_key:
Add the specified device to a group.

##### Parameters
* `deviceId` (Integer, required) - The ID of the device you wish to add to the group.
* `groupId` (Integer, required) - The ID of the group to add the device to.

##### Response
Returns the `Group` after the device has been added, else `null`.

#### `removeDeviceToGroup(deviceId: Int!, groupId: Int!): Group` :closed_lock_with_key:
Remove the specified device from a group.

##### Parameters
* `deviceId` (Integer, required) - The ID of the device you wish to remove from the group.
* `groupId` (Integer, required) - The ID of the group to remove the device from.

##### Response
Returns the `Group` after the device has been removed, else `null`.

#### `addDevice(id: String!): Device` :closed_lock_with_key:
Add a device to DripDash. The owner is the person who adds the device.

##### Parameters
* `id` (String, required) - The ID of the device to be added.

##### Response
Returns the created `Device`, else `null`.

#### `removeDevice(id: String!): Boolean` :closed_lock_with_key:
Remove a device from DripDash.

##### Parameters
* `id` (String, required) - The ID of the device to be removed.

##### Response
Returns `True` if the device is removed successfully, else `False`.

#### `renameDevice(id: String!, name: String!): Device` :closed_lock_with_key:
Rename a device. If a device name is empty, the UI should default to using the ID.

##### Parameters
* `id` (String, required) - The ID of the device to rename.
* `name` (String, required) - The new name for the device.

##### Response
Returns the `Device` with it's new name.

### Queries

TODO

```
type Query {
  user(id: Int): User!
  device(id: String): Device!
  group(id: Int): Group!
  unregisteredDevices: [UnregisteredDevice]!
  self: User
}
```

### Types

TODO

```
type User {
  id: Int!
  username: String!
  location: Location
  devices: [Device]!
  groups: [Group]!
}

type Location {
  latitude: Float!
  longitude: Float!
}

type Device {
  id: String!
  name: String
  owner: User!
  status: Status!
  glances: [Glance]!
  location: Location
  data(from: DateTime): [DataEntry]!
  latest: DataEntry
}

type Glance {
  status: Status!
  title: String!
  text: String
}

type Group {
  id: Int!
  name: String!
  members: [User]!
  devices: [Device]!
}

type DataEntry {
  id: Int!
  timestamp: DateTime!
  device: Device!

  waterTemp: Float
  airTemp: Float
  humidity: Float
  light: Float
  ph: Float
  rssi: Float
  beds: [BedEntry]!
}

type BedEntry {
  id: Int!
  dataEntry: DataEntry!
  status: Int
  level: Float
}

type UnregisteredDevice {
  id: String!
}
```