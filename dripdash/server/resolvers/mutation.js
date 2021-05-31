const { PrismaClient } = require("@prisma/client");
const prisma = new PrismaClient();

const bcrypt = require("bcryptjs");
const { context } = require("../api");
const tokens = require("../tokens");

const Mutation = {
  register: async (_, {username, password}) => {
    const passHash = await bcrypt.hash(password, 11);
    const result = await prisma.user.create({
      data: {
        username,
        passHash
      }
    });

    return !!result;
  },

  login: async (_, {username, password}) => {
    const user = await prisma.user.findOne({
      where: {
        username
      }
    });

    // if the user exists and the password matches, create an auth token.
    if (user && await bcrypt.compare(password, user.passHash)) {
      return tokens.create(user);
    } else {
      return null;
    }
  },

  refresh: (_, {}, ctx) => {
    // Old (but still valid) token is in the header.
    // if it's not present, or has already expired, return null.
    if (!(ctx.user && ctx.user.id && ctx.user.id)) return null;
    return tokens.create(ctx.user);
  },

  createGroup: async (_, { name }, ctx) => {
    if (!ctx.user) return null;
    if (name.length === 0) return null;
    const group = await prisma.group.create({
      data: {
        name,
        members: {
          connect: { id: ctx.user.id }
        }
      }
    })
    return group;
  },
  leaveGroup: async (_, { id }, ctx) => {
    if (!ctx.user) return null;
    const group = await prisma.group.update({
      where: { id },
      data: {
        members: {
          disconnect: [ { id: ctx.user.id }]
        } 
      },
      include: {
        members: {
          select: {
            id: true
          }
        }
      }
    }).catch( () => {
      return null;
    });

    // if the group is now empty, delete it.
    if (group && group.members.length === 0) {
      await prisma.group.delete({ where: { id }});
    }
    return group;
  },

  addUserToGroup: async (_, { username, groupId }) => {
    return await prisma.group.update({
      where: { id: groupId },
      data: {
        members: {
          connect: { username }
        }
      }
    })
  },

  addDeviceToGroup: async (_, { deviceId, groupId }) => {
    return await prisma.group.update({
      where: { id: groupId },
      data: {
        devices: {
          connect: { id: deviceId }
        }
      }
    })
  },

  removeDeviceFromGroup: async (_, { deviceId, groupId }) => {
    return await prisma.group.update({
      where: { id: groupId },
      data: {
        devices: {
          disconnect: [{ id: deviceId }]
        }
      }
    })
  },

  addDevice: async (_, { id }, ctx) => {
    if (!ctx.user) return null;
    
    await prisma.unregisteredDevice.delete({
      where: { id }
    })

    return await prisma.device.create({
      data: {
        id,
        owner: {
          connect: { id: ctx.user.id }
        }
      }
    })
  },

  removeDevice: async (_, { id }) => {
    await prisma.bed.deleteMany({
      where: {
        dataEntry: {
          deviceId: id
        }
      }
    })
    await prisma.dataEntry.deleteMany({ where: { deviceId: id}})
    const result = await prisma.device.delete({ where: { id } })
    return !!result;
  },

  renameDevice: async (_, { id, name }) => {
    return await prisma.device.update({
      where: { id },
      data: { name }
    })
  }
}

module.exports = Mutation;